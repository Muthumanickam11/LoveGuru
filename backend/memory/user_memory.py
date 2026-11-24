"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — User Memory & History Storage          ║
║         Saves messages, updates mood logs and user context   ║
╚══════════════════════════════════════════════════════════════╝
"""

import uuid
import logging
from typing import Optional, Dict, Any, List
from datetime import datetime, timezone
from config.database import AsyncSessionLocal
from models.database_models import (
    Message, MoodLog, Conversation, MessageRole, MessageType,
    CrisisLevel, LifeStage,
)

logger = logging.getLogger(__name__)


def _to_uuid(value: Any) -> uuid.UUID:
    if isinstance(value, uuid.UUID):
        return value
    try:
        return uuid.UUID(str(value))
    except (ValueError, TypeError, AttributeError):
        return uuid.uuid4()


def _map_crisis_level(level: Optional[str]) -> CrisisLevel:
    return {
        "critical": CrisisLevel.CRITICAL,
        "high": CrisisLevel.HIGH,
        "moderate": CrisisLevel.MODERATE,
    }.get((level or "safe").lower(), CrisisLevel.SAFE)


async def save_message(
    user_id: str,
    conversation_id: str,
    user_message: str,
    ai_response: str,
    emotion_tag: Optional[str] = None,
    emotion_vector: Optional[Dict[str, float]] = None,
    crisis_level: str = "safe",
    rag_used: bool = False,
    latency_ms: Optional[int] = None,
) -> Optional[str]:
    """Persists a user/assistant message turn and updates the conversation.

    Returns the assistant message id as a string (or None on failure).
    """
    try:
        async with AsyncSessionLocal() as session:
            u_id = _to_uuid(user_id)
            c_id = _to_uuid(conversation_id)
            c_level = _map_crisis_level(crisis_level)

            conv = await session.get(Conversation, c_id)
            if not conv:
                conv = Conversation(
                    id=c_id,
                    user_id=u_id,
                    title="Conversation with LoveGuru",
                    stage_context=LifeStage.SINGLE,
                    chat_mode="general",
                )
                session.add(conv)
                await session.flush()

            session.add(Message(
                id=uuid.uuid4(),
                conversation_id=c_id,
                user_id=u_id,
                role=MessageRole.USER,
                content=user_message,
                message_type=MessageType.TEXT,
                crisis_level=c_level,
                created_at=datetime.now(timezone.utc).replace(tzinfo=None),
            ))

            ai_id = uuid.uuid4()
            session.add(Message(
                id=ai_id,
                conversation_id=c_id,
                user_id=u_id,
                role=MessageRole.ASSISTANT,
                content=ai_response,
                message_type=MessageType.TEXT,
                emotion_tag=emotion_tag,
                emotion_vector=emotion_vector,
                crisis_level=c_level,
                rag_used=rag_used,
                latency_ms=latency_ms,
                created_at=datetime.now(timezone.utc).replace(tzinfo=None),
            ))

            conv.message_count = (conv.message_count or 0) + 2
            conv.last_message_at = datetime.now(timezone.utc).replace(tzinfo=None)
            if c_level in (CrisisLevel.HIGH, CrisisLevel.CRITICAL):
                conv.max_crisis_level = c_level

            await session.commit()
            logger.info(f"Saved message turn for conversation {c_id}")
            return str(ai_id)
    except Exception as e:
        logger.error(f"Error saving message in user_memory: {e}")
        return None


async def update_mood_log(
    user_id: str,
    primary_emotion: str,
    intensity: float = 0.5,
    stage: str = "single",
) -> None:
    """Records an emotional mood log entry for the user."""
    try:
        async with AsyncSessionLocal() as session:
            u_id = _to_uuid(user_id)
            score = max(1, min(10, int(round(intensity * 10))))

            mood = MoodLog(
                id=uuid.uuid4(),
                user_id=u_id,
                mood_score=score,
                trigger_notes=f"auto:{primary_emotion}",
                context_stage=LifeStage(stage) if stage in LifeStage._value2member_map_ else None,
                logged_at=datetime.now(timezone.utc).replace(tzinfo=None),
            )
            session.add(mood)
            await session.commit()
            logger.info(f"Logged mood '{primary_emotion}' (score: {score}) for user {u_id}")
    except Exception as e:
        logger.error(f"Error updating mood log: {e}")
