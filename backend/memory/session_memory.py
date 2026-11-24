"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Session Memory & Streak Engine         ║
║         Tracks streaks, XP awards, and active sessions       ║
╚══════════════════════════════════════════════════════════════╝
"""

import uuid
import logging
from typing import Optional
from datetime import datetime, timezone, date, timedelta
from sqlalchemy import select
from config.database import AsyncSessionLocal
from models.database_models import Streak, StreakType

logger = logging.getLogger(__name__)

_STREAK_MAP = {
    "app_checkin": StreakType.APP_CHECKIN,
    "no_contact": StreakType.NO_CONTACT,
    "daily_challenge": StreakType.DAILY_CHALLENGE,
    "journaling": StreakType.JOURNALING,
}


def _to_uuid(value) -> uuid.UUID:
    if isinstance(value, uuid.UUID):
        return value
    try:
        return uuid.UUID(str(value))
    except (ValueError, TypeError, AttributeError):
        return uuid.uuid4()


async def update_streak(user_id: str, streak_type: str = "app_checkin") -> int:
    """Updates user streak and returns awarded XP points."""
    try:
        async with AsyncSessionLocal() as session:
            u_id = _to_uuid(user_id)
            s_type = _STREAK_MAP.get(streak_type, StreakType.APP_CHECKIN)

            stmt = select(Streak).where(Streak.user_id == u_id, Streak.streak_type == s_type)
            result = await session.execute(stmt)
            streak = result.scalar_one_or_none()

            now = datetime.now(timezone.utc).replace(tzinfo=None)
            today = now.date()
            last_date = streak.last_activity_at.date() if (streak and streak.last_activity_at) else None

            if not streak:
                streak = Streak(
                    id=uuid.uuid4(),
                    user_id=u_id,
                    streak_type=s_type,
                    current_count=1,
                    longest_count=1,
                    started_at=now,
                    last_activity_at=now,
                )
                session.add(streak)
                await session.commit()
                return 10

            if last_date == today:
                return 5  # already counted today

            if last_date == today - timedelta(days=1):
                streak.current_count += 1
                streak.longest_count = max(streak.longest_count, streak.current_count)
            else:
                streak.current_count = 1
                streak.started_at = now

            streak.last_activity_at = now
            await session.commit()
            return 10 + min(streak.current_count * 2, 50)
    except Exception as e:
        logger.error(f"Error updating streak: {e}")
        return 5
