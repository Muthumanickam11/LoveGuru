"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Pattern Memory & Recurring Triggers   ║
║         Tracks red flags, attachment dynamics, and insights  ║
╚══════════════════════════════════════════════════════════════╝
"""

import uuid
import logging
from typing import List, Optional
from datetime import datetime, timezone
from sqlalchemy import select
from config.database import AsyncSessionLocal
from models.database_models import UserPattern

logger = logging.getLogger(__name__)


def _to_uuid(value) -> uuid.UUID:
    if isinstance(value, uuid.UUID):
        return value
    try:
        return uuid.UUID(str(value))
    except (ValueError, TypeError, AttributeError):
        return uuid.uuid4()


async def record_pattern(
    user_id: str,
    pattern_type: str,
    pattern_name: str,
    description: str,
    evidence: Optional[List[str]] = None,
    confidence: float = 0.6,
) -> None:
    """Records — or reinforces — an AI-detected pattern in user behavior."""
    try:
        async with AsyncSessionLocal() as session:
            u_id = _to_uuid(user_id)

            existing = (await session.execute(
                select(UserPattern).where(
                    UserPattern.user_id == u_id,
                    UserPattern.pattern_name == pattern_name,
                )
            )).scalar_one_or_none()

            if existing:
                existing.evidence_count = (existing.evidence_count or 0) + 1
                existing.confidence = min(0.99, (existing.confidence or 0.5) + 0.1)
                snippets = list(existing.evidence_snippets or [])
                snippets.extend(evidence or [])
                existing.evidence_snippets = snippets[-10:]
                existing.updated_at = datetime.now(timezone.utc).replace(tzinfo=None)
            else:
                session.add(UserPattern(
                    id=uuid.uuid4(),
                    user_id=u_id,
                    pattern_type=pattern_type,
                    pattern_name=pattern_name,
                    description=description,
                    evidence_snippets=evidence or [],
                    evidence_count=1,
                    confidence=confidence,
                    is_confirmed=None,
                    detected_at=datetime.now(timezone.utc).replace(tzinfo=None),
                ))

            await session.commit()
            logger.info(f"Recorded pattern '{pattern_name}' for user {u_id}")
    except Exception as e:
        logger.error(f"Error recording pattern: {e}")


async def get_active_patterns(user_id: str) -> List[dict]:
    """Returns non-dismissed patterns for a user."""
    try:
        async with AsyncSessionLocal() as session:
            u_id = _to_uuid(user_id)
            rows = (await session.execute(
                select(UserPattern)
                .where(UserPattern.user_id == u_id, UserPattern.is_confirmed.isnot(False))
                .order_by(UserPattern.confidence.desc())
            )).scalars().all()
            return [
                {
                    "id": str(p.id),
                    "type": p.pattern_type,
                    "name": p.pattern_name,
                    "description": p.description,
                    "confidence": p.confidence,
                    "evidence_count": p.evidence_count,
                    "is_confirmed": p.is_confirmed,
                    "detected_at": p.detected_at.isoformat() if p.detected_at else None,
                }
                for p in rows
            ]
    except Exception as e:
        logger.error(f"Error fetching patterns: {e}")
        return []
