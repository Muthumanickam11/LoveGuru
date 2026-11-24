"""
╔══════════════════════════════════════════════════════════════╗
║   LOVEGURU AI — Patterns Service                             ║
║   Surfaces and detects recurring emotional/behavioural trends ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging
import uuid
from datetime import datetime, timezone
from typing import Any, Dict, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from config.llm_config import LLMConfig
from memory import pattern_memory
from models.database_models import User, Message, MessageRole, UserPattern
from services.common import llm_json

logger = logging.getLogger(__name__)


async def get_active(db: AsyncSession, user: User) -> Dict[str, Any]:
    patterns = await pattern_memory.get_active_patterns(str(user.id))
    return {"patterns": patterns}


async def analyze(db: AsyncSession, user: User) -> Dict[str, Any]:
    msgs = (await db.execute(
        select(Message).where(Message.user_id == user.id, Message.role == MessageRole.USER)
        .order_by(Message.created_at.desc()).limit(30)
    )).scalars().all()

    transcript = "\n".join((m.content or "") for m in reversed(msgs))[:4000]
    fallback = {
        "patterns": [
            {"type": "emotional", "name": "Anxious Over-Giving",
             "description": "Tends to over-extend to secure affection.",
             "confidence": 0.55},
        ]
    }
    prompt = (
        "Analyze the user's messages for recurring emotional or dating patterns. Respond ONLY with "
        "JSON: {\"patterns\": [{\"type\", \"name\", \"description\", \"confidence\"}]}.\n\n"
        + transcript
    )
    data = await llm_json(prompt, LLMConfig.pattern_analyzer, fallback)

    detected = []
    for p in data.get("patterns", []):
        if not isinstance(p, dict) or not p.get("name"):
            continue
        await pattern_memory.record_pattern(
            user_id=str(user.id),
            pattern_type=p.get("type", "emotional"),
            pattern_name=p["name"],
            description=p.get("description", ""),
            evidence=[],
            confidence=float(p.get("confidence", 0.6) or 0.6),
        )
        detected.append(p)

    return {"status": "analyzed", "detected": detected}


async def dismiss(db: AsyncSession, user: User, pattern_id: str) -> Dict[str, Any]:
    try:
        pid = uuid.UUID(str(pattern_id))
    except (ValueError, TypeError):
        return {"status": "invalid_id"}
    row = (await db.execute(
        select(UserPattern).where(UserPattern.id == pid, UserPattern.user_id == user.id)
    )).scalar_one_or_none()
    if row is None:
        return {"status": "not_found"}
    row.is_confirmed = False
    await db.commit()
    return {"status": "dismissed"}
