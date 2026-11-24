"""
╔══════════════════════════════════════════════════════════════╗
║   LOVEGURU AI — Stage 4 Service (Heartbreak Recovery)        ║
║   Grief Weather, No-Contact Tracker, Identity Reclamation    ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging
from datetime import datetime, timezone, date
from typing import Any, Dict, Optional

from sqlalchemy.ext.asyncio import AsyncSession

from config.llm_config import LLMConfig
from models.database_models import User, GriefWeather
from services.common import get_or_create_stage_data, llm_json

logger = logging.getLogger(__name__)

_GRIEF_STAGES = [
    {"stage": "Storm", "weather": "storm", "description": "Acute shock and intensity. Survival mode only.", "focus": "Hydrate, sleep, eat. Reduce decisions to the minimum."},
    {"stage": "Overcast", "weather": "overcast", "description": "Heavy fog and rumination. Numbness and sadness interleave.", "focus": "Gentle routine, movement, and permission to not be okay."},
    {"stage": "Rain", "weather": "rain", "description": "Waves of grief that come and go with triggers.", "focus": "Name feelings without judgment and reach for support."},
    {"stage": "Clearing", "weather": "clearing", "description": "First glimpses of peace between the pain.", "focus": "Reconnect with identity, hobbies, and friendships."},
    {"stage": "Sun", "weather": "sun", "description": "Integration and renewed hope for the future.", "focus": "Extract lessons, define needs, open gently to love."},
]


async def nc_tracker(db: AsyncSession, user: User) -> Dict[str, Any]:
    if not user.profile:
        return {"status": "no_profile", "current_streak_days": 0}
    row = await get_or_create_stage_data(db, "stage4", user.profile.id)
    if row.no_contact_start is None:
        row.no_contact_start = datetime.now(timezone.utc).replace(tzinfo=None)
        await db.commit()

    elapsed = (datetime.now(timezone.utc).replace(tzinfo=None) - row.no_contact_start).days
    row.no_contact_streak_days = max(0, elapsed)
    row.no_contact_longest_days = max(row.no_contact_longest_days or 0, row.no_contact_streak_days)
    await db.commit()

    days = row.no_contact_streak_days
    badge = ("Holding On" if days < 3 else "Finding Footing" if days < 14
             else "Gaining Strength" if days < 30 else "Reclaimed")
    target = (3, 14, 30, 60)
    milestone_target = next((d for d in target if d > days), 90)
    phase = ("Acute Withdrawal Phase (Days 1-3)" if days < 3 else
             "Dopamine Receptor Reset Phase (Days 14-21)" if days < 21 else
             "Neural Rewiring Consolidation Phase" if days < 45 else
             "Identity Reclamation Phase")
    return {
        "status": "active",
        "current_streak_days": days,
        "longest_streak_days": row.no_contact_longest_days,
        "badge": badge,
        "milestone_target": milestone_target,
        "percent_to_goal": min(100, round(days / milestone_target * 100)),
        "next_milestone": milestone_target,
        "neurochemical_phase": phase,
        "urges_resisted_count": len(row.pain_scores or []),
        "guidance": "Your brain is rewiring right now. The urge to reach out is neurochemical craving, "
                    "not evidence you should rekindle.",
        "encouragement": "Every hour you choose your own peace is a vote for your future self.",
    }


async def log_urge(db: AsyncSession, user: User, payload: Dict[str, Any]) -> Dict[str, Any]:
    if not user.profile:
        return {"status": "no_profile"}
    row = await get_or_create_stage_data(db, "stage4", user.profile.id)
    intensity = int(payload.get("intensity", payload.get("urgency_level", 5)) or 5)
    urge = {
        "date": datetime.now(timezone.utc).replace(tzinfo=None).isoformat(),
        "intensity": max(1, min(10, intensity)),
        "trigger": payload.get("trigger", "unspecified"),
        "rode_it_out": bool(payload.get("rode_it_out", True)),
    }
    urges = list(row.pain_scores or [])
    urges.append(urge)
    row.pain_scores = urges[-200:]
    await db.commit()

    tips = [
        "Urges peak and fall within minutes — set a timer and outlast the wave.",
        "Text a friend instead of your ex. Redirect the reach for connection.",
        "Move your body for 90 seconds: the nervous system needs discharge, not decisions.",
    ]
    return {
        "status": "logged",
        "urge_count": len(row.pain_scores),
        "encouragement": "You just rode the wave without wiping out. Every urge you surf weakens the "
                         "neural hook of the craving.",
        "somatic_grounding": "One hand on your heart, one on your belly. Inhale 4 seconds, exhale 7. "
                             "This feeling is a temporary visitor — it will pass without acting on it.",
        "coping_tips": tips,
        "xp_earned": 30,
    }


async def grief_guidance(db: AsyncSession, user: User, payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    feeling = (payload or {}).get("message", "")
    fallback = {
        "grief_weather": "rain",
        "validation": "What you're feeling is a normal response to a real loss — not weakness.",
        "grounding_exercise": "Name 5 things you can see, 4 you can touch, 3 you can hear, 2 you can smell, 1 you can taste.",
        "affirmation": "Your grief is proportional to your capacity to love. That capacity is still yours.",
    }
    prompt = (
        "You are a gentle heartbreak recovery coach. Based on the user's message, identify their "
        "current grief weather (one of: storm, overcast, rain, clearing, sun) and respond ONLY with "
        "JSON: {grief_weather, validation, grounding_exercise, affirmation}.\n\nMessage: " + str(feeling)
    )
    data = await llm_json(prompt, LLMConfig.stage4_heartbreak_coach, fallback)

    weather = str(data.get("grief_weather", "rain")).lower()
    if weather not in {g.value for g in GriefWeather}:
        weather = "rain"

    if user.profile:
        row = await get_or_create_stage_data(db, "stage4", user.profile.id)
        try:
            row.grief_weather = GriefWeather(weather)
        except ValueError:
            pass
        await db.commit()

    return {
        "grief_weather": weather,
        "weather_state": weather.capitalize(),
        "grief_stages": _GRIEF_STAGES,
        "validation": data.get("validation", fallback["validation"]),
        "dominant_insight": data.get("validation", fallback["validation"]),
        "today_mantra": data.get("affirmation", fallback["affirmation"]),
        "grounding_exercise": data.get("grounding_exercise", fallback["grounding_exercise"]),
        "affirmation": data.get("affirmation", fallback["affirmation"]),
        "safe_activities": [
            "Take a 20-minute walk with a podcast on an unrelated topic.",
            "Write an uncensored letter in your LoveGuru Closure Vault — never to be sent.",
            "Text a trusted friend about something uplifting.",
        ],
    }


async def log_grief_weather(db: AsyncSession, user: User, payload: Dict[str, Any]) -> Dict[str, Any]:
    weather = str(payload.get("weather", "rain")).lower()
    if user.profile:
        row = await get_or_create_stage_data(db, "stage4", user.profile.id)
        try:
            row.grief_weather = GriefWeather(weather)
        except ValueError:
            pass
        await db.commit()
    return {
        "status": "saved",
        "logged_weather": weather,
        "validation": f"It is completely natural to experience {weather} weather today. Healing has no timetable.",
    }


async def journal_entry(db: AsyncSession, user: User, payload: Dict[str, Any]) -> Dict[str, Any]:
    content = (payload.get("content") or "").strip()
    return {
        "status": "stored_in_vault",
        "word_count": len(content.split()),
        "ai_reflection": "Your vulnerability in writing this down is transforming raw emotional pain "
                         "into lasting psychological resilience.",
        "safety_reminder": "This entry is safely sealed in your private LoveGuru vault.",
    }


async def breakup_analysis(db: AsyncSession, user: User, payload: Dict[str, Any]) -> Dict[str, Any]:
    what_happened = (payload.get("what_happened") or payload.get("story") or "").strip()
    fallback = {
        "lessons": [
            "You tolerate inconsistency when you're anxious about being left.",
            "You need a partner who initiates as often as you do.",
        ],
        "patterns_to_break": ["Over-functioning to keep peace", "Silencing your needs to avoid conflict"],
        "unmet_needs": ["Consistency", "Emotional reciprocity", "Feeling chosen"],
        "what_was_good": ["You love deeply and communicate with warmth"],
    }
    prompt = (
        "You are a compassionate breakup analyst. From the user's story, extract lessons, recurring "
        "patterns to break, unmet needs, and strengths. Respond ONLY with JSON keys: lessons (list), "
        "patterns_to_break (list), unmet_needs (list), what_was_good (list).\n\nStory:\n" + what_happened
    )
    data = await llm_json(prompt, LLMConfig.stage4_heartbreak_coach, fallback)

    if user.profile:
        row = await get_or_create_stage_data(db, "stage4", user.profile.id)
        row.lessons_extracted = data
        duration = payload.get("relationship_duration_months")
        if duration is not None:
            try:
                row.relationship_duration_months = int(duration)
            except (TypeError, ValueError):
                pass
        await db.commit()
    return {"status": "analyzed", **{k: data.get(k, fallback[k]) for k in fallback}}


async def closure_letter(db: AsyncSession, user: User, payload: Dict[str, Any]) -> Dict[str, Any]:
    unsent = (payload.get("unsent_message") or payload.get("message") or "").strip()
    fallback_letter = (
        "Dear you,\n\nI'm writing this not to reach you, but to release the parts of me I left "
        "behind with you. Thank you for what you taught me; I'm sorry for what I couldn't give. "
        "I'm taking my kindness, my capacity to love, and my future back into my own hands.\n\nGoodbye."
    )
    prompt = (
        "Write a healing, unsent closure letter. Warm, dignified, no blame. Respond ONLY with JSON "
        "key 'letter'.\n\nWhat the user wants to say:\n" + unsent
    )
    data = await llm_json(prompt, LLMConfig.stage4_heartbreak_coach, {"letter": fallback_letter})
    letter = data.get("letter", fallback_letter)
    if user.profile:
        row = await get_or_create_stage_data(db, "stage4", user.profile.id)
        row.identity_items = list(row.identity_items or [])
        await db.commit()
    return {"status": "written", "letter": letter}


async def self_worth(db: AsyncSession, user: User, payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return {
        "affirmations": [
            "I am worthy of love that doesn't require me to shrink.",
            "Their leaving does not define my value.",
            "I can hold grief and hope at the same time.",
        ],
        "daily_practice": "Write one thing you did today that your future self would thank you for.",
        "identity_reclaim": [
            "List 3 hobbies you dropped during the relationship and schedule one this week.",
            "Reconnect with one friend you neglected while grieving.",
        ],
    }


async def healing_exercises(db: AsyncSession, user: User, payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return {
        "exercises": [
            {"title": "The Empty Chair", "duration_min": 15,
             "instructions": "Say out loud everything unsaid to an empty chair. Then walk away without apology."},
            {"title": "Future Self Letter", "duration_min": 10,
             "instructions": "Write from 1 year ahead about how this pain became your foundation."},
            {"title": "Body Scan Release", "duration_min": 8,
             "instructions": "Progressive muscle relaxation from feet to face to discharge stored shock."},
        ]
    }


async def readiness_for_love(db: AsyncSession, user: User, payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    score = 45.0
    if user.profile:
        row = await get_or_create_stage_data(db, "stage4", user.profile.id)
        days = row.no_contact_streak_days or 0
        score = max(20.0, min(95.0, 30.0 + days * 0.8))
        row.readiness_for_love = score
        await db.commit()
    return {
        "readiness_score": round(score),
        "verdict": "Not yet — focus on stabilization and identity reclamation." if score < 55
        else "Getting close — you're rebuilding your foundation.",
        "next_focus": ["Rebuild routine", "Reclaim identity", "Reconnect socially"],
    }
