"""
╔══════════════════════════════════════════════════════════════╗
║   LOVEGURU AI — Stage 3 Service (In a Relationship)          ║
║   Gottman Method, Love Languages, Conflict Scripts, Health   ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging
from datetime import datetime, timezone
from typing import Any, Dict

from sqlalchemy.ext.asyncio import AsyncSession

from config.llm_config import LLMConfig
from models.database_models import User, LoveLanguage
from prompts.stage3_prompts import STAGE3_COMMUNICATION_SCRIPT_PROMPT
from services.common import get_or_create_stage_data, llm_json

logger = logging.getLogger(__name__)


async def gottman_assessment(db: AsyncSession, user: User, payload: Dict[str, Any]) -> Dict[str, Any]:
    criticism = int(payload.get("criticism_freq", 2) or 2)
    contempt = int(payload.get("contempt_freq", 1) or 1)
    defensiveness = int(payload.get("defensiveness_freq", 2) or 2)
    stonewalling = int(payload.get("stonewalling_freq", 2) or 2)

    risk = (criticism * 2) + (contempt * 4) + (defensiveness * 2) + (stonewalling * 3)
    vitality = max(30, 100 - risk * 3)

    result = {
        "relationship_vitality_score": vitality,
        "horsemen_presence": {
            "criticism": "Mild" if criticism <= 2 else "Elevated",
            "contempt": "Low (Healthy)" if contempt <= 1 else "Warning",
            "defensiveness": "Mild" if defensiveness <= 2 else "Elevated",
            "stonewalling": "Low" if stonewalling <= 2 else "Elevated",
        },
        "gottman_antidote_focus": (
            "Gentle Start-Up Protocol: frame grievances as 'I feel… about… and what I need is…' "
            "instead of 'You always…'."
        ),
        "weekly_prescriptions": [
            "Implement a 10-minute daily Stress-Reducing Conversation without problem-solving.",
            "Express 3 specific appreciations every morning before screens.",
            "Take a 20-minute pause if heart rate climbs above 100 bpm during disagreements.",
        ],
    }

    radar = {
        "trust": max(1, 10 - contempt),
        "connection": max(1, 10 - stonewalling),
        "fun": 7,
        "conflict_resolution": max(1, 10 - defensiveness),
        "mutual_support": max(1, 10 - criticism),
        "intimacy": 7,
    }
    result["health_radar"] = radar

    if user.profile:
        row = await get_or_create_stage_data(db, "stage3", user.profile.id)
        row.relationship_health_current = radar
        scores = list(row.weekly_health_scores or [])
        scores.append({"date": datetime.now(timezone.utc).replace(tzinfo=None).isoformat(), "score": vitality})
        row.weekly_health_scores = scores[-52:]
        await db.commit()

    return result


async def conflict_script(db: AsyncSession, user: User, payload: Dict[str, Any]) -> Dict[str, Any]:
    incident = payload.get("trigger_incident", "household chores or quality time")
    feeling = payload.get("user_feelings", "unappreciated and overwhelmed")
    need = payload.get("desired_outcome", "clear shared planning and collaborative effort")
    original = payload.get("original_statement") or f"You always make me feel {feeling} about {incident}."

    fallback = {
        "FOUR_HORSEMEN_IDENTIFIED": "Criticism",
        "GENTLE_STARTUP_VERSION": (
            f"Hey love, when {incident} happened earlier, I felt {feeling}. I care deeply about us, "
            f"so what I really need is {need}. Can we find a rhythm that feels good for both of us?"
        ),
        "EXPLANATION": "Replacing blame with a feeling + specific need lowers defensiveness.",
        "ACTIVE_LISTENING_RESPONSE": "So what I hear you saying is… is that right?",
        "WHAT_TO_AVOID": ["Starting with 'You always…'", "Bringing up old, unrelated arguments"],
    }
    prompt = STAGE3_COMMUNICATION_SCRIPT_PROMPT.format(
        original_statement=original, context=incident, underlying_need=need,
    )
    data = await llm_json(prompt, LLMConfig.stage3_relationship_coach, fallback)

    script = data.get("GENTLE_STARTUP_VERSION", fallback["GENTLE_STARTUP_VERSION"])

    if user.profile:
        row = await get_or_create_stage_data(db, "stage3", user.profile.id)
        conflicts = list(row.discussed_conflicts or [])
        conflicts.append({"incident": incident, "feeling": feeling, "need": need,
                          "date": datetime.now(timezone.utc).replace(tzinfo=None).isoformat()})
        row.discussed_conflicts = conflicts[-50:]
        scripts = list(row.gottman_scripts_used or [])
        scripts.append(script)
        row.gottman_scripts_used = scripts[-50:]
        await db.commit()

    return {
        "framework": "Gottman Gentle Start-Up & Nonviolent Communication",
        "script": script,
        "explanation": data.get("EXPLANATION", fallback["EXPLANATION"]),
        "active_listening_response": data.get("ACTIVE_LISTENING_RESPONSE", fallback["ACTIVE_LISTENING_RESPONSE"]),
        "what_to_avoid": data.get("WHAT_TO_AVOID", fallback["WHAT_TO_AVOID"]),
        "repair_attempts": [
            "'I'm getting overwhelmed — can I hold your hand while we talk?'",
            "'Let me rephrase that — I didn't mean to sound harsh.'",
        ],
    }


async def problem_analysis(db: AsyncSession, user: User, payload: Dict[str, Any]) -> Dict[str, Any]:
    topic = payload.get("topic") or payload.get("problem") or "unmet needs"
    return {
        "status": "analyzed",
        "problem_types": {
            "communication": "Mismatched style or timing.",
            "expectation": "Unspoken assumptions about roles.",
            "unmet_need": "A care bid going unnoticed.",
            "external_stress": "Outside pressure leaking into the bond.",
            "values": "A deeper worldview difference.",
            "pattern": "A recurring loop that needs breaking.",
        },
        "likely_root": f"Regarding '{topic}', the friction is most likely an unspoken expectation "
                       "combined with a bid for connection that isn't landing.",
        "first_step": "Name the pattern out loud without blame, then ask what each of you needs.",
    }


async def get_love_language(db: AsyncSession, user: User) -> Dict[str, Any]:
    psychology = user.psychology
    primary = psychology.primary_love_language.value if psychology and psychology.primary_love_language else "words_of_affirmation"
    secondary = psychology.secondary_love_language.value if psychology and psychology.secondary_love_language else "quality_time"
    return {
        "user_profile": {
            "primary": primary.replace("_", " ").title(),
            "secondary": secondary.replace("_", " ").title(),
            "score_distribution": {
                "words_of_affirmation": 32, "quality_time": 28,
                "physical_touch": 16, "acts_of_service": 14, "receiving_gifts": 10,
            },
        },
        "daily_action_tip": (
            "Leave a handwritten 2-line note acknowledging something specific you admire "
            "about your partner today."
        ),
    }


async def submit_love_language(db: AsyncSession, user: User, payload: Dict[str, Any]) -> Dict[str, Any]:
    primary = payload.get("primary")
    secondary = payload.get("secondary")
    psychology = user.psychology
    if psychology:
        for attr, val in (("primary_love_language", primary), ("secondary_love_language", secondary)):
            if val:
                try:
                    setattr(psychology, attr, LoveLanguage(val))
                except ValueError:
                    pass
        await db.commit()
    return {"status": "saved", "message": "Love language profile refreshed."}


async def get_date_ideas(db: AsyncSession, user: User) -> Dict[str, Any]:
    return {
        "categories": [
            {"title": "Deep Intimacy & Vulnerability",
             "idea": "The 36 Questions That Lead to Love over homemade fondue and candlelight."},
            {"title": "Playful Novelty",
             "idea": "Mystery Cook-Off: 20-minute limit, $15 budget, one blindfolded ingredient."},
            {"title": "Restorative Peace",
             "idea": "Stargazing sound-bath picnic with zero phones allowed."},
        ]
    }


async def health_dashboard(db: AsyncSession, user: User) -> Dict[str, Any]:
    if user.profile:
        row = await get_or_create_stage_data(db, "stage3", user.profile.id)
        return {
            "current": row.relationship_health_current or {},
            "history": (row.weekly_health_scores or [])[-12:],
        }
    return {"current": {}, "history": []}
