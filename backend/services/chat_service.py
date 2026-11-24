"""
╔══════════════════════════════════════════════════════════════╗
║          LOVEGURU AI — Chat Service (Main AI Interface)      ║
║  Orchestrates the 12-node LangGraph pipeline for every mode  ║
║  (text, voice, image, screenshot) and persists conversations ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging
import uuid
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from config.llm_config import LLMConfig
from graph.main_graph import loveguru_graph
from models.database_models import (
    Conversation, Message, User, MessageRole, MessageType, CrisisLevel, LifeStage,
)
from services.common import llm_text

logger = logging.getLogger(__name__)


def _stage_enum(stage: str) -> LifeStage:
    try:
        return LifeStage(stage)
    except ValueError:
        return LifeStage.SINGLE


async def get_or_create_conversation(
    db: AsyncSession,
    user_id: uuid.UUID,
    conversation_id: Optional[str],
    stage: str,
    mode: str,
) -> Conversation:
    if conversation_id:
        try:
            cid = uuid.UUID(str(conversation_id))
        except (TypeError, ValueError):
            cid = None
        if cid:
            convo = (await db.execute(
                select(Conversation).where(
                    Conversation.id == cid, Conversation.user_id == user_id)
            )).scalar_one_or_none()
            if convo:
                return convo
    convo = Conversation(
        user_id=user_id,
        stage_context=_stage_enum(stage),
        chat_mode=mode,
    )
    db.add(convo)
    await db.flush()
    return convo


async def get_session_messages(db: AsyncSession, conversation_id: uuid.UUID, limit: int = 10) -> list:
    rows = (await db.execute(
        select(Message).where(Message.conversation_id == conversation_id)
        .order_by(desc(Message.created_at)).limit(limit)
    )).scalars().all()
    return [{"role": m.role.value, "content": m.content} for m in reversed(rows)]


def _build_graph_input(user, profile, psychology, convo, raw_message, message_type,
                       session_messages, image_url=None, audio_url=None) -> dict:
    return {
        "user_id": str(user.id),
        "conversation_id": str(convo.id),
        "raw_message": raw_message,
        "message_type": message_type,
        "image_url": image_url,
        "audio_url": audio_url,
        "session_messages": session_messages,
        "user_name": profile.display_name if profile else user.email.split("@")[0],
        "current_stage": profile.current_stage.value if profile else "single",
        "ai_personality": profile.ai_personality.value if profile else "warm_friend",
        "attachment_style": (psychology.attachment_style.value if psychology and psychology.attachment_style else "unknown"),
        "love_language": (psychology.primary_love_language.value if psychology and psychology.primary_love_language else "unknown"),
        "readiness_score": psychology.readiness_score if psychology else None,
        "onboarding_completed": profile.onboarding_completed if profile else False,
        "cultural_background": (profile.cultural_background or "Indian") if profile else "Indian",
        "relationship_history_summary": psychology.onboarding_summary if psychology else None,
        "nodes_executed": [],
        "crisis_triggered": False,
        "memory_updated": False,
        "mood_logged": False,
        "streaks_updated": False,
    }


async def _persist_pair(db, convo, user, raw_message, result, message_type) -> Message:
    user_msg = Message(
        conversation_id=convo.id, user_id=user.id, role=MessageRole.USER,
        content=raw_message, message_type=message_type,
    )
    level = result.get("crisis_assessment", {}).get("level", "safe")
    try:
        crisis = CrisisLevel(level)
    except ValueError:
        crisis = CrisisLevel.SAFE
    _fr = result.get("final_response", "")
    logger.info("_persist_pair: final_response len=%d" % len(_fr))
    ai_msg = Message(
        conversation_id=convo.id, user_id=user.id, role=MessageRole.ASSISTANT,
        content=_fr,
        message_type=MessageType.TEXT,
        emotion_tag=result.get("primary_emotion"),
        emotion_vector=result.get("emotion_vector"),
        crisis_level=crisis,
        rag_used=bool(result.get("rag_context", {}).get("retrieved")),
        latency_ms=result.get("total_latency_ms"),
    )
    db.add(user_msg)
    db.add(ai_msg)
    convo.message_count = (convo.message_count or 0) + 2
    convo.last_message_at = datetime.now(timezone.utc).replace(tzinfo=None)
    if level in ("high", "critical"):
        convo.max_crisis_level = crisis
    await db.commit()
    return ai_msg


async def process_text(db: AsyncSession, user: User, payload: Dict[str, Any]) -> Dict[str, Any]:
    message = (payload.get("message") or "").strip()
    conversation_id = payload.get("conversation_id")
    mode = payload.get("mode", "general")
    if not message:
        raise ValueError("message cannot be empty")

    profile = user.profile
    if not profile:
        raise ValueError("User profile not found. Please complete onboarding.")

    convo = await get_or_create_conversation(
        db, user.id, conversation_id, profile.current_stage.value, mode)
    session_messages = await get_session_messages(db, convo.id)

    await db.commit()  # release SQLite write lock before graph memory writes

    psychology = user.psychology
    graph_input = _build_graph_input(
        user, profile, psychology, convo, message, "text", session_messages)

    result = await loveguru_graph.ainvoke(graph_input)

    ai_msg = await _persist_pair(db, convo, user, message, result, MessageType.TEXT)

    crisis_level = result.get("crisis_assessment", {}).get("level", "safe")
    return {
        "response": result.get("final_response", ""),
        "conversation_id": str(convo.id),
        "message_id": str(ai_msg.id),
        "quick_replies": result.get("quick_replies", []),
        "crisis_level": crisis_level,
        "emotion_detected": result.get("primary_emotion"),
        "stage_routed": result.get("routed_stage"),
        "latency_ms": result.get("total_latency_ms"),
        "raw_result": result,
    }


async def process_voice(db: AsyncSession, user: User, message: str,
                        conversation_id: Optional[str] = None,
                        mode: str = "voice",
                        transcript_meta: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return await process_text(db, user, {
        "message": message, "conversation_id": conversation_id, "mode": mode,
        **({"transcript_meta": transcript_meta} if transcript_meta else {}),
    })


async def process_image(db: AsyncSession, user: User, image_url: str,
                        message: str = "", conversation_id: Optional[str] = None) -> Dict[str, Any]:
    from tools.image_analyzer import analyze_image
    profile = user.profile
    stage = profile.current_stage.value if profile else "finding"
    analysis = await analyze_image(image_url, context=message, stage=stage)

    combined = (message + " " + str(analysis.get("analysis", ""))).strip()
    text_result = await process_text(db, user, {
        "message": combined, "conversation_id": conversation_id, "mode": "image",
    })
    text_result["image_analysis"] = analysis
    return text_result


async def process_screenshot(db: AsyncSession, user: User, screenshot_url: str,
                             message: str = "", conversation_id: Optional[str] = None) -> Dict[str, Any]:
    from tools.screenshot_reader import parse_screenshot
    parsed = await parse_screenshot(screenshot_url, app_type="dating_app")

    combined = (message + " " + str(parsed.get("analysis", parsed.get("transcription", "")))).strip()
    text_result = await process_text(db, user, {
        "message": combined, "conversation_id": conversation_id, "mode": "screenshot",
    })
    text_result["screenshot_analysis"] = parsed
    return text_result


async def generate_quick_replies(stage: str, crisis_level: str) -> List[str]:
    if crisis_level in ("high", "critical"):
        return ["I feel unsafe", "Help me now", "I need a professional"]
    return {
        "single": ["Readiness check", "Create my blueprint", "Daily task"],
        "finding": ["Review my profile", "Analyze my chat", "Date prep"],
        "relationship": ["Health check", "Conflict script", "Love languages"],
        "heartbreak": ["NC tracker", "Grief weather", "Closure letter"],
    }.get(stage, ["Explain better", "What do you think?", "Give me a task"])