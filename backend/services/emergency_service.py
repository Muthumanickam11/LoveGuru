"""
╔══════════════════════════════════════════════════════════════╗
║   LOVEGURU AI — Emergency & Crisis Service                    ║
║   Zero-barrier resources, SOS persistence, crisis logging     ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging
from typing import Any, Dict, Optional

from sqlalchemy.ext.asyncio import AsyncSession

from models.database_models import User, CrisisLog, CrisisLevel
from tools.crisis_resources import get_crisis_resources

logger = logging.getLogger(__name__)


async def get_resources(region: str = "india") -> Dict[str, Any]:
    return get_crisis_resources(region or "india")


async def trigger_sos(db: AsyncSession, user: User, payload: Dict[str, Any]) -> Dict[str, Any]:
    region = payload.get("region", "india")
    resources = get_crisis_resources(region)
    db.add(CrisisLog(
        user_id=user.id,
        crisis_level=CrisisLevel.CRITICAL,
        trigger_message=(payload.get("message") or "")[:500] or None,
        response_type="sos",
        helplines_shown=[h.get("name", str(h)) for h in resources["helplines"]],
    ))
    await db.commit()
    return {
        "status": "sos_activated",
        "message": "You are not alone. Please pause, take a deep breath, and connect with a compassionate professional right now.",
        "emergency_helpline_top": resources["helplines"][0],
        "all_helplines": resources["helplines"],
        "grounding_exercise": resources["grounding_exercises"][1],
        "timestamp": "immediate",
    }


async def log_crisis(db: AsyncSession, user: User, payload: Dict[str, Any]) -> Dict[str, Any]:
    level = str(payload.get("crisis_level", "high")).lower()
    if level not in {c.value for c in CrisisLevel}:
        level = "high"
    db.add(CrisisLog(
        user_id=user.id,
        crisis_level=CrisisLevel(level),
        trigger_message=(payload.get("message") or "")[:500] or None,
        response_type=payload.get("response_type", "grounding"),
    ))
    await db.commit()
    return {"logged": True, "support_note": "Emergency event noted with high-priority safety protocol."}