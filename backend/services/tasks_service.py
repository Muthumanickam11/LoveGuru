"""
╔══════════════════════════════════════════════════════════════╗
║   LOVEGURU AI — Tasks & Challenges Service                   ║
║   Daily growth tasks with XP, stage-aware task generation    ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging
import uuid
from datetime import datetime, timezone, timedelta
from typing import Any, Dict, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.database_models import (
    User, TaskChallenge, TaskStatus, LifeStage,
)

logger = logging.getLogger(__name__)

_STAGE_TASKS = {
    LifeStage.SINGLE: ("The Mirror Audit", "Grade yourself on the qualities you demand from a partner.", 25),
    LifeStage.FINDING: ("Opening Line Sprint", "Draft 3 tailored openers for a profile you admire.", 20),
    LifeStage.RELATIONSHIP: ("Appreciation Drop", "Tell your partner 3 specific things you appreciate today.", 20),
    LifeStage.HEARTBREAK: ("Urge Surf", "When an urge hits, ride the 90-second wave without reaching out.", 30),
}


async def today_tasks(db: AsyncSession, user: User) -> Dict[str, Any]:
    start = datetime.now(timezone.utc).replace(tzinfo=None).replace(hour=0, minute=0, second=0, microsecond=0)
    rows = (await db.execute(
        select(TaskChallenge).where(
            TaskChallenge.user_id == user.id,
            TaskChallenge.task_date >= start,
        ).order_by(TaskChallenge.task_date)
    )).scalars().all()

    if not rows:
        stage = user.profile.current_stage if user.profile else LifeStage.SINGLE
        title, desc, xp = _STAGE_TASKS.get(stage, _STAGE_TASKS[LifeStage.SINGLE])
        row = TaskChallenge(
            user_id=user.id, title=title, description=desc,
            difficulty=2, stage_context=stage, task_date=datetime.now(timezone.utc).replace(tzinfo=None),
            status=TaskStatus.PENDING, xp_reward=xp,
        )
        db.add(row)
        await db.commit()
        rows = [row]

    return {"tasks": [
        {
            "id": str(t.id),
            "title": t.title,
            "description": t.description,
            "difficulty": t.difficulty,
            "status": t.status.value,
            "xp_reward": t.xp_reward,
            "completed_at": t.completed_at.isoformat() if t.completed_at else None,
        } for t in rows
    ]}


async def _get_task(db: AsyncSession, user: User, task_id: str):
    try:
        tid = uuid.UUID(str(task_id))
    except (ValueError, TypeError):
        return None
    return (await db.execute(
        select(TaskChallenge).where(TaskChallenge.id == tid, TaskChallenge.user_id == user.id)
    )).scalar_one_or_none()


async def complete(db: AsyncSession, user: User, task_id: str) -> Dict[str, Any]:
    task = await _get_task(db, user, task_id)
    if task is None:
        return {"completed": False, "message": "Task not found."}
    task.status = TaskStatus.COMPLETED
    task.completed_at = datetime.now(timezone.utc).replace(tzinfo=None)
    await db.commit()
    return {"completed": True, "xp_earned": task.xp_reward, "message": "Well done. Small steps compound."}


async def skip(db: AsyncSession, user: User, task_id: str) -> Dict[str, Any]:
    task = await _get_task(db, user, task_id)
    if task is None:
        return {"skipped": False, "message": "Task not found."}
    task.status = TaskStatus.SKIPPED
    await db.commit()
    return {"skipped": True}


async def history(db: AsyncSession, user: User) -> Dict[str, Any]:
    rows = (await db.execute(
        select(TaskChallenge).where(TaskChallenge.user_id == user.id)
        .order_by(TaskChallenge.task_date.desc()).limit(60)
    )).scalars().all()
    return {"history": [
        {
            "id": str(t.id),
            "title": t.title,
            "status": t.status.value,
            "task_date": t.task_date.isoformat() if t.task_date else None,
            "completed_at": t.completed_at.isoformat() if t.completed_at else None,
        } for t in rows
    ]}
