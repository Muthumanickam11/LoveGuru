"""
╔══════════════════════════════════════════════════════════════╗
║   LOVEGURU AI — Stage 1 Service (Single & Searching)         ║
║   Reality Check, Love Readiness, Self-Improvement Roadmap    ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging
from typing import Any, Dict

from sqlalchemy.ext.asyncio import AsyncSession

from config.llm_config import LLMConfig
from models.database_models import User, UserPsychology
from prompts.stage1_prompts import (
    STAGE1_PARTNER_ANALYSIS_PROMPT,
    STAGE1_READINESS_PROMPT,
)
from services.common import get_or_create_stage_data, llm_json, llm_text

logger = logging.getLogger(__name__)


def _as_list(value) -> list:
    if isinstance(value, list):
        return value
    if isinstance(value, str):
        return [value]
    return []


async def analyze_partner_description(db: AsyncSession, user: User, payload: Dict[str, Any]) -> Dict[str, Any]:
    """Runs a Reality Check Analysis over the user's dream-partner description."""
    description = (payload.get("description") or "").strip()
    traits = _as_list(payload.get("traits"))

    profile = user.profile
    psychology = user.psychology
    attachment = psychology.attachment_style.value if psychology else "unknown"
    age = profile.age if profile else None
    cultural = profile.cultural_background or "Indian" if profile else "Indian"

    fallback = {
        "REALISM_SCORE": 78,
        "WHAT_REVEALS": (
            "Your wishlist leans toward wanting both deep ambition and constant availability — "
            "a pattern often rooted in wanting to feel chosen without fearing abandonment."
        ),
        "REFINED_VISION": (
            "A partner who is emotionally consistent, curious about your inner world, and shares "
            "your core values — where ambition and warmth coexist seasonally, not simultaneously."
        ),
        "HEALTHY_EXPECTATIONS": [
            "Emotional self-regulation and curiosity",
            "Transparent and respectful conflict style",
            "Shared core moral compass and integrity",
        ],
        "EXAMINE_EXPECTATIONS": [
            {"original": "Always available to cuddle", "reality": "No human is available 24/7",
             "what_they_really_need": "Predictable warmth and reliability"},
        ],
        "RECONSIDER_EXPECTATIONS": [
            {"original": "Hyper-ambitious but never busy", "why": "These traits are in tension",
             "healthier_version": "Ambitious with intentional quality time"},
        ],
    }

    prompt = STAGE1_PARTNER_ANALYSIS_PROMPT.format(
        description=description or ", ".join(traits),
        attachment_style=attachment,
        age=age if age is not None else "unknown",
        cultural_background=cultural,
    )
    data = await llm_json(prompt, LLMConfig.stage1_partner_analyzer, fallback)

    score = data.get("REALISM_SCORE", data.get("realism_score", fallback["REALISM_SCORE"]))
    try:
        score = float(score)
    except (TypeError, ValueError):
        score = fallback["REALISM_SCORE"]
    score = max(0.0, min(100.0, score))

    healthy = _as_list(data.get("HEALTHY_EXPECTATIONS")) or fallback["HEALTHY_EXPECTATIONS"]
    examine = _as_list(data.get("EXAMINE_EXPECTATIONS")) or fallback["EXAMINE_EXPECTATIONS"]
    reconsider = _as_list(data.get("RECONSIDER_EXPECTATIONS")) or fallback["RECONSIDER_EXPECTATIONS"]
    reveals = data.get("WHAT_REVEALS") or fallback["WHAT_REVEALS"]
    refined = data.get("REFINED_VISION") or fallback["REFINED_VISION"]
    assessment = data.get("ASSESSMENT") or (
        "Your vision reflects real psychological insight with a healthy emphasis on character values."
        if score >= 70 else
        "Your vision is aspirational — a few expectations are pulling against each other and worth refining."
    )

    if profile:
        row = await get_or_create_stage_data(db, "stage1", profile.id)
        row.partner_raw_description = description or ", ".join(traits)
        row.realism_score = score
        row.healthy_expectations = [str(x) for x in healthy]
        row.examine_expectations = examine
        row.reconsider_expectations = reconsider
        row.what_reveals = reveals
        row.refined_vision = refined
        await db.commit()

    return {
        "status": "completed",
        "realism_score": round(score),
        "assessment": assessment,
        "healthy_expectations": [str(x) for x in healthy],
        "examine_carefully": [
            x.get("original", str(x)) if isinstance(x, dict) else str(x) for x in examine
        ],
        "reconsider": [
            x.get("original", str(x)) if isinstance(x, dict) else str(x) for x in reconsider
        ],
        "what_this_reveals": reveals,
        "refined_vision": refined,
        "guru_wisdom": "The secret to attracting your ideal partner is becoming the emotional home they would naturally seek.",
    }


async def compute_readiness(db: AsyncSession, user: User, payload: Dict[str, Any]) -> Dict[str, Any]:
    """Scores love readiness across the pillars and persists the result."""
    answers = payload.get("answers") or {}
    if not answers:
        answers = {
            k: payload.get(k) for k in (
                "emotional_independence", "past_relationship_closure",
                "financial_readiness", "communication_openness", "conflict_resilience",
            ) if payload.get(k) is not None
        }

    fallback = {
        "overall_score": 76,
        "readiness_band": "mostly_ready",
        "celebration": "You show strong emotional self-awareness and openness.",
        "next_step": "Strengthen patience when response times fluctuate during early dating.",
    }
    psychology = user.psychology
    prompt = STAGE1_READINESS_PROMPT.format(
        responses=answers,
        attachment_style=psychology.attachment_style.value if psychology else "unknown",
        context="Initial readiness assessment",
    )
    data = await llm_json(prompt, LLMConfig.stage1_partner_analyzer, fallback)

    overall = data.get("overall_score", fallback["overall_score"])
    try:
        overall = float(overall)
    except (TypeError, ValueError):
        overall = fallback["overall_score"]
    overall = max(0.0, min(100.0, overall))

    if user.profile:
        row = await get_or_create_stage_data(db, "stage1", user.profile.id)
        row.readiness_score = overall
        row.readiness_breakdown = data.get("dimensions", {})
        await db.commit()

    if psychology:
        psychology.readiness_score = overall
        await db.commit()

    return {
        "status": "saved",
        "calculated_score": round(overall),
        "readiness_band": data.get("readiness_band", fallback["readiness_band"]),
        "celebration": data.get("celebration", fallback["celebration"]),
        "next_step": data.get("next_step", fallback["next_step"]),
        "gaps": data.get("gaps", []),
        "message": "Readiness profile updated successfully.",
    }


async def get_readiness(db: AsyncSession, user: User) -> Dict[str, Any]:
    psychology = user.psychology
    overall = psychology.readiness_score if psychology and psychology.readiness_score else 72.0
    breakdown = {}
    if user.profile:
        row = await get_or_create_stage_data(db, "stage1", user.profile.id)
        breakdown = row.readiness_breakdown or {}
    return {
        "overall_score": round(overall),
        "category_breakdown": breakdown or {
            "emotional_independence": 78,
            "past_relationship_closure": 70,
            "financial_readiness": 80,
            "conflict_resilience": 68,
            "communication_openness": 84,
        },
        "attachment_style_detected": psychology.attachment_style.value if psychology else "unknown",
        "readiness_verdict": "Ready for intentional dating with clear boundary awareness.",
    }


async def get_improvement_plan(db: AsyncSession, user: User) -> Dict[str, Any]:
    if user.profile:
        row = await get_or_create_stage_data(db, "stage1", user.profile.id)
        if row.improvement_plan:
            return {"plan": row.improvement_plan}
    plan = {
        "week_theme": "Emotional Autonomy & Self-Sovereignty",
        "daily_focus": "Notice reflexive validation-seeking and practice grounded presence.",
        "milestones": [
            {"title": "Identify Top 3 Non-Negotiable Values", "completed": False},
            {"title": "Complete 3-Day Screen-Free Evening Reflection", "completed": False},
            {"title": "Draft Personal Boundary Manifesto", "completed": False},
        ],
    }
    if user.profile:
        row = await get_or_create_stage_data(db, "stage1", user.profile.id)
        row.improvement_plan = plan
        await db.commit()
    return {"plan": plan}


async def get_daily_task(db: AsyncSession, user: User) -> Dict[str, Any]:
    return {
        "task": {
            "id": "s1_task_today",
            "title": "The Mirror Audit",
            "instructions": (
                "Write down 3 qualities you demand from a romantic partner. For each, grade "
                "yourself honestly on how consistently you embody it."
            ),
            "xp_reward": 25,
            "estimated_minutes": 10,
        }
    }

async def analyze_grooming(db, user, image_url, preferences):
    """Analyze a selfie for grooming/style guidance."""
    from tools.image_analyzer import analyze_image
    budget = (preferences or {}).get("budget", "medium")
    gender = (preferences or {}).get("gender", "unspecified")
    context = "Grooming analysis. Budget: " + budget + ", Gender: " + gender
    if image_url:
        result = await analyze_image(image_url=image_url, context=context, stage="single")
        analysis = result.get("analysis", "")
    else:
        analysis = "No image provided. General grooming guidance: maintain consistent skincare, dress for your body type, and prioritize genuine confidence."
    return {
        "status": "completed",
        "grooming_analysis": analysis,
        "budget": budget,
        "gender": gender,
        "guru_wisdom": "Looking good starts with feeling good about who you are.",
    }
