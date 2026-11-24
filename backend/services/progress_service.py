"""
╔══════════════════════════════════════════════════════════════╗
║   LOVEGURU AI — Progress & Analytics Service                 ║
║   Streaks, XP, Mood graphs, Patterns, Weekly synthesis       ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging
from datetime import datetime, timezone, timedelta, date
from typing import Any, Dict, List

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from models.database_models import (
    User, Message, MoodLog, DailyCheckin, Streak, StreakType,
    TaskChallenge, TaskStatus, UserPattern,
)

logger = logging.getLogger(__name__)

_LEVELS = [
    (0, "Curious Heart"), (200, "Mindful Explorer"), (500, "Grounded Seeker"),
    (1000, "Wise Lover"), (2000, "Master of the Heart"), (4000, "Love Guru"),
]


def _level_for(xp: int) -> Dict[str, Any]:
    title = _LEVELS[0][1]
    level = 1
    for i, (threshold, name) in enumerate(_LEVELS):
        if xp >= threshold:
            level = i + 1
            title = name
    return {"level": level, "level_title": title}


async def _count(db: AsyncSession, model, user_id) -> int:
    return int((await db.execute(
        select(func.count()).select_from(model).where(model.user_id == user_id)
    )).scalar() or 0)


async def _get_checkin_streak(db: AsyncSession, user_id) -> int:
    row = (await db.execute(
        select(Streak).where(Streak.user_id == user_id, Streak.streak_type == StreakType.APP_CHECKIN)
    )).scalar_one_or_none()
    return row.current_count if row else 0


async def overview(db: AsyncSession, user: User) -> Dict[str, Any]:
    checkins = await _count(db, DailyCheckin, user.id)
    msgs = await _count(db, Message, user.id)
    tasks_done = int((await db.execute(
        select(func.count()).select_from(TaskChallenge).where(
            TaskChallenge.user_id == user.id, TaskChallenge.status == TaskStatus.COMPLETED)
    )).scalar() or 0)

    xp = checkins * 15 + msgs * 2 + tasks_done * 25
    lvl = _level_for(xp)
    streak = await _get_checkin_streak(db, user.id)

    logs = (await db.execute(
        select(MoodLog).where(MoodLog.user_id == user.id).order_by(MoodLog.logged_at.desc()).limit(7)
    )).scalars().all()
    balance = round(sum(m.mood_score for m in logs) / len(logs) * 10) if logs else 75

    profile = user.profile
    return {
        "current_streak": streak,
        "total_xp": xp,
        "level": lvl["level"],
        "level_title": lvl["level_title"],
        "current_stage": (profile.current_stage.value if profile and profile.current_stage else "single"),
        "active_challenges_completed": tasks_done,
        "emotional_balance_score": balance,
        "weekly_milestone": f"Logged {checkins} check-ins and {msgs} reflections in total.",
    }


async def mood_graph(db: AsyncSession, user: User) -> Dict[str, Any]:
    since = datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(days=7)
    logs = (await db.execute(
        select(MoodLog).where(MoodLog.user_id == user.id, MoodLog.logged_at >= since)
        .order_by(MoodLog.logged_at.asc())
    )).scalars().all()

    if not logs:
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        today = datetime.now(timezone.utc).replace(tzinfo=None).weekday()
        order = days[today + 1:] + days[:today + 1]
        data = [{"day": d, "score": 7.0, "emotion": "steady", "intensity": 7} for d in order]
        return {"data": data, "average_score": 7.0, "trend": "stable"}

    data = []
    for m in logs:
        data.append({
            "day": m.logged_at.strftime("%a") if m.logged_at else "—",
            "score": float(m.mood_score),
            "emotion": (m.emoji or "neutral"),
            "intensity": m.mood_score,
        })
    avg = round(sum(m.mood_score for m in logs) / len(logs), 1)
    trend = "upward_positive" if len(logs) > 1 and logs[-1].mood_score >= logs[0].mood_score else "needs_care"
    return {"data": data, "average_score": avg, "trend": trend}


async def patterns(db: AsyncSession, user: User) -> Dict[str, Any]:
    rows = (await db.execute(
        select(UserPattern).where(
            UserPattern.user_id == user.id, UserPattern.is_confirmed.isnot(False)
        ).order_by(UserPattern.confidence.desc())
    )).scalars().all()
    if not rows:
        return {"patterns": []}
    return {"patterns": [
        {
            "id": str(p.id),
            "name": p.pattern_name,
            "type": p.pattern_type,
            "description": p.description,
            "confidence": p.confidence,
            "evidence_count": p.evidence_count,
        } for p in rows
    ]}


async def weekly_report(db: AsyncSession, user: User) -> Dict[str, Any]:
    since = datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(days=7)
    msgs = await _count(db, Message, user.id)
    logs = (await db.execute(
        select(MoodLog).where(MoodLog.user_id == user.id, MoodLog.logged_at >= since)
    )).scalars().all()
    checkins = await _count(db, DailyCheckin, user.id)
    avg = round(sum(m.mood_score for m in logs) / len(logs), 1) if logs else 7.0

    week_start = (datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(days=datetime.now(timezone.utc).replace(tzinfo=None).weekday())).strftime("%b %d")
    return {
        "report": {
            "week_title": f"Week of {week_start}",
            "executive_summary": (
                f"You showed up for yourself this week with an average mood of {avg}/10 across "
                f"{len(logs)} logs and {checkins} check-ins. Your emotional resilience is building."
            ),
            "top_wins": [
                f"Logged {len(logs)} mood check-in(s) this week",
                f"Exchanged {msgs} messages with your LoveGuru coach",
                "Continued your growth journey without judgment",
            ],
            "focus_next_week": "Keep practising gentle self-talk and consistent daily check-ins.",
            "ai_guru_blessing": "You are evolving from reacting to life toward consciously designing the love you deserve.",
        }
    }


async def checkin(db: AsyncSession, user: User, payload: Dict[str, Any]) -> Dict[str, Any]:
    now = datetime.now(timezone.utc).replace(tzinfo=None)
    checkin_type = payload.get("checkin_type", "evening")
    row = DailyCheckin(
        user_id=user.id,
        checkin_date=now,
        checkin_type=checkin_type,
        sleep_hours=payload.get("sleep_hours"),
        sleep_quality=payload.get("sleep_quality"),
        appetite_score=payload.get("appetite_score"),
        movement_done=bool(payload.get("movement_done", False)),
        sunlight_done=bool(payload.get("sunlight_done", False)),
        emotional_note=payload.get("emotional_note"),
    )
    db.add(row)

    mood = payload.get("mood_score")
    if mood is not None:
        try:
            db.add(MoodLog(user_id=user.id, mood_score=int(mood),
                           emoji=payload.get("emoji"), trigger_notes=payload.get("emotional_note")))
        except (TypeError, ValueError):
            pass

    streak = (await db.execute(
        select(Streak).where(Streak.user_id == user.id, Streak.streak_type == StreakType.APP_CHECKIN)
    )).scalar_one_or_none()
    if streak is None:
        streak = Streak(user_id=user.id, streak_type=StreakType.APP_CHECKIN,
                        current_count=1, longest_count=1, last_activity_at=now, started_at=now)
        db.add(streak)
    else:
        if streak.last_activity_at and (now - streak.last_activity_at).days >= 1:
            streak.current_count = (streak.current_count or 0) + 1
        elif streak.last_activity_at and (now - streak.last_activity_at).days == 0:
            pass
        else:
            streak.current_count = 1
        streak.longest_count = max(streak.longest_count or 0, streak.current_count or 0)
        streak.last_activity_at = now

    await db.commit()
    return {
        "status": "recorded",
        "xp_earned": 15,
        "current_streak": streak.current_count,
        "message": "Daily check-in complete. Streak maintained!",
    }


async def milestones(db: AsyncSession, user: User) -> Dict[str, Any]:
    xp = (await _count(db, DailyCheckin, user.id)) * 15 + (await _count(db, Message, user.id)) * 2
    streak = await _get_checkin_streak(db, user.id)
    profile = user.profile
    return {
        "milestones": [
            {"title": "First AI Guru Session", "achieved": (await _count(db, Message, user.id)) > 0},
            {"title": "Attachment Style Discovery", "achieved": bool(user.psychology)},
            {"title": "7-Day Consistency Badge", "achieved": streak >= 7},
            {"title": "Love Readiness Master", "achieved": xp >= 1000, "target": "Earn 1000 XP"},
        ]
    }
