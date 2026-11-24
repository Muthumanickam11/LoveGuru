"""
╔══════════════════════════════════════════════════════════════╗
║          LOVEGURU AI — Chat Router (Main AI Interface)       ║
║  POST /chat/text  /chat/voice  /chat/image  /chat/screenshot ║
║  GET /chat/history  /chat/sessions  DELETE /chat/session/{id}║
╚══════════════════════════════════════════════════════════════╝
"""

import uuid
import logging
import tempfile
import os
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, Form
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc
from pydantic import BaseModel
from typing import Optional, List

from config.database import get_db
from routers.auth_router import get_current_user
from models.database_models import Conversation, Message, User, CrisisLevel
from services import chat_service, voice_service
from graph.main_graph import loveguru_graph

logger = logging.getLogger(__name__)
router = APIRouter()


# ─────────────────────────────────────────────────────────────
# SCHEMAS
# ─────────────────────────────────────────────────────────────

class TextChatRequest(BaseModel):
    message: str
    conversation_id: Optional[str] = None
    mode: Optional[str] = "general"


class ChatResponse(BaseModel):
    response: str
    conversation_id: str
    message_id: str
    quick_replies: List[str] = []
    crisis_level: str = "safe"
    emotion_detected: Optional[str] = None
    stage_routed: Optional[str] = None
    latency_ms: Optional[int] = None


# ─────────────────────────────────────────────────────────────
# POST /chat/text — Main text chat endpoint
# ─────────────────────────────────────────────────────────────

@router.post("/text", response_model=ChatResponse)
async def chat_text(
    body: TextChatRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    try:
        result = await chat_service.process_text(
            db, current_user, body.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"AI pipeline error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="AI pipeline error. Please try again.")

    return ChatResponse(
        response=result["response"],
        conversation_id=result["conversation_id"],
        message_id=result["message_id"],
        quick_replies=result.get("quick_replies", []),
        crisis_level=result.get("crisis_level", "safe"),
        emotion_detected=result.get("emotion_detected"),
        stage_routed=result.get("stage_routed"),
        latency_ms=result.get("latency_ms"),
    )


# ─────────────────────────────────────────────────────────────
# POST /chat/voice — Voice note chat
# ─────────────────────────────────────────────────────────────

@router.post("/voice")
async def chat_voice(
    audio: UploadFile = File(...),
    conversation_id: Optional[str] = Form(default=None),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    suffix = os.path.splitext(audio.filename or "audio.webm")[1] or ".webm"
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
        tmp.write(await audio.read())
        tmp_path = tmp.name
    try:
        result = await voice_service.handle_voice_note(
            db, current_user, tmp_path, conversation_id)
    finally:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
    return result


# ─────────────────────────────────────────────────────────────
# POST /chat/image — Image analysis
# ─────────────────────────────────────────────────────────────

@router.post("/image")
async def chat_image(
    message: str = Form(default=""),
    image: UploadFile = File(...),
    conversation_id: Optional[str] = Form(default=None),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    suffix = os.path.splitext(image.filename or ".jpg")[1] or ".jpg"
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
        tmp.write(await image.read())
        tmp_path = tmp.name
    try:
        result = await chat_service.process_image(
            db, current_user, tmp_path, message, conversation_id)
    finally:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
    return result


# ─────────────────────────────────────────────────────────────
# POST /chat/screenshot — Dating app screenshot analysis
# ─────────────────────────────────────────────────────────────

@router.post("/screenshot")
async def analyze_screenshot(
    message: str = Form(default="Help me respond to this"),
    screenshot: UploadFile = File(...),
    conversation_id: Optional[str] = Form(default=None),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    suffix = os.path.splitext(screenshot.filename or ".png")[1] or ".png"
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
        tmp.write(await screenshot.read())
        tmp_path = tmp.name
    try:
        result = await chat_service.process_screenshot(
            db, current_user, tmp_path, message, conversation_id)
    finally:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
    return result


# ─────────────────────────────────────────────────────────────
# GET /chat/history — Get conversation messages
# ─────────────────────────────────────────────────────────────

@router.get("/history")
async def get_chat_history(
    conversation_id: str,
    limit: int = 50,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    try:
        cid = uuid.UUID(conversation_id)
    except (TypeError, ValueError):
        raise HTTPException(status_code=400, detail="Invalid conversation_id")

    result = await db.execute(
        select(Message)
        .join(Conversation)
        .where(Message.conversation_id == cid, Conversation.user_id == current_user.id)
        .order_by(Message.created_at)
        .limit(limit)
    )
    messages = result.scalars().all()
    return {
        "conversation_id": conversation_id,
        "messages": [
            {
                "id": str(m.id),
                "role": m.role.value,
                "content": m.content,
                "type": m.message_type.value,
                "emotion": m.emotion_tag,
                "crisis_level": m.crisis_level.value,
                "created_at": m.created_at.isoformat(),
            }
            for m in messages
        ],
    }


# ─────────────────────────────────────────────────────────────
# GET /chat/sessions — List user's conversation sessions
# ─────────────────────────────────────────────────────────────

@router.get("/sessions")
async def get_sessions(
    limit: int = 20,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Conversation)
        .where(Conversation.user_id == current_user.id)
        .order_by(desc(Conversation.last_message_at))
        .limit(limit)
    )
    sessions = result.scalars().all()
    return {
        "sessions": [
            {
                "id": str(s.id),
                "title": s.title or "New Conversation",
                "stage": s.stage_context.value if s.stage_context else "single",
                "message_count": s.message_count,
                "crisis_level": s.max_crisis_level.value if s.max_crisis_level else "safe",
                "started_at": s.started_at.isoformat() if s.started_at else None,
                "last_message_at": s.last_message_at.isoformat() if s.last_message_at else None,
            }
            for s in sessions
        ]
    }


# ─────────────────────────────────────────────────────────────
# DELETE /chat/session/{id}
# ─────────────────────────────────────────────────────────────

@router.delete("/session/{session_id}", status_code=204)
async def delete_session(
    session_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    try:
        sid = uuid.UUID(session_id)
    except (TypeError, ValueError):
        raise HTTPException(status_code=400, detail="Invalid session id")
    result = await db.execute(
        select(Conversation).where(
            Conversation.id == sid, Conversation.user_id == current_user.id)
    )
    convo = result.scalar_one_or_none()
    if not convo:
        raise HTTPException(status_code=404, detail="Session not found")
    await db.delete(convo)
    await db.commit()

# ---------------------------------------------------------------------------
# POST /chat/text/stream  -- Server-Sent Events streaming endpoint
# ---------------------------------------------------------------------------
import json as _json

@router.post("/text/stream")
async def chat_text_stream(
    body: TextChatRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Stream the AI response token-by-token via Server-Sent Events."""
    async def event_generator():
        try:
            message = (body.message or "").strip()
            if not message:
                yield "data: " + _json.dumps({"error": "message cannot be empty"}) + "\n\n"
                return

            profile = current_user.profile
            if not profile:
                yield "data: " + _json.dumps({"error": "User profile not found. Please complete onboarding."}) + "\n\n"
                return

            convo = await chat_service.get_or_create_conversation(
                db, current_user.id, body.conversation_id,
                profile.current_stage.value, body.mode or "general")
            session_messages = await chat_service.get_session_messages(db, convo.id)
            await db.commit()

            psychology = current_user.psychology
            graph_input = chat_service._build_graph_input(
                current_user, profile, psychology, convo, message, "text", session_messages)

            final_state = None
            async for event in loveguru_graph.astream_events(graph_input, version="v2"):
                kind = event.get("event", "")
                if kind == "on_chat_model_stream":
                    chunk = event.get("data", {}).get("chunk")
                    if chunk and hasattr(chunk, "content") and chunk.content:
                        yield "data: " + _json.dumps({"token": chunk.content}) + "\n\n"
                elif kind == "on_chain_end" and event.get("name") == "LangGraph":
                    final_state = event.get("data", {}).get("output")

            if final_state:
                ai_msg = await chat_service._persist_pair(db, convo, current_user, message, final_state, MessageType.TEXT)
                crisis_level = final_state.get("crisis_assessment", {}).get("level", "safe")
                yield "data: " + _json.dumps({
                    "done": True,
                    "conversation_id": str(convo.id),
                    "message_id": str(ai_msg.id),
                    "quick_replies": final_state.get("quick_replies", []),
                    "crisis_level": crisis_level,
                    "emotion_detected": final_state.get("primary_emotion"),
                    "stage_routed": final_state.get("routed_stage"),
                }) + "\n\n"
            else:
                yield "data: " + _json.dumps({"done": True, "error": "No final state"}) + "\n\n"
        except Exception as e:
            logger.error(f"Streaming error: {e}", exc_info=True)
            yield "data: " + _json.dumps({"error": "AI pipeline error. Please try again."}) + "\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")
