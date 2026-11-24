"""
╔══════════════════════════════════════════════════════════════╗
║   LOVEGURU AI — Stage 2 Service (Finding Love)               ║
║   Profile Review, Conversation Coach, Flags, Date Prep       ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging
from typing import Any, Dict, List

from sqlalchemy.ext.asyncio import AsyncSession

from config.llm_config import LLMConfig
from models.database_models import User
from prompts.stage2_prompts import STAGE2_PROFILE_REVIEW_PROMPT
from services.common import get_or_create_stage_data, llm_json, llm_text

logger = logging.getLogger(__name__)


async def review_profile(db: AsyncSession, user: User, payload: Dict[str, Any]) -> Dict[str, Any]:
    bio = (payload.get("bio") or payload.get("bio_text") or "").strip()
    platform = payload.get("app") or payload.get("app_name") or "Hinge"
    profile = user.profile

    fallback = {
        "FIRST_IMPRESSION_SCORE": 8,
        "FIRST_IMPRESSION": "Warm, creative, and approachable with distinct lifestyle hooks.",
        "CLICHES_FOUND": ["I love travel and coffee"] if "travel" in bio.lower() else [],
        "BIO_REWRITES": {
            "witty": "Equal parts deep philosophical chai talks and competitive board-game marathons. Bring your A-game to a trivia debate.",
            "deep": "Building a life I love — weekends exploring indie cafes, quiet trails, and vinyl playlists. Seeking an emotionally intelligent partner.",
            "casual": "Mostly here for genuine conversation, terrible puns, and someone who's kind to waiters. What's your most controversial food opinion?",
        },
        "CONVERSATION_STARTERS": [
            "What's the last thing that made you laugh out loud?",
            "Coffee or chai — and how seriously do you take that answer?",
            "What's a hobby you'd defend with your life?",
        ],
        "REMOVE_THIS": "Generic clichés that every other profile uses.",
        "ADD_THIS": "One specific, oddly-detailed fact that makes you memorable.",
    }

    prompt = STAGE2_PROFILE_REVIEW_PROMPT.format(
        bio=bio, platform=platform,
        gender=(profile.gender if profile else "unspecified") or "unspecified",
        age=(profile.age if profile else None) or "unspecified",
        cultural_background=(profile.cultural_background if profile else None) or "Indian",
    )
    data = await llm_json(prompt, LLMConfig.stage2_dating_coach, fallback)

    score = data.get("FIRST_IMPRESSION_SCORE", fallback["FIRST_IMPRESSION_SCORE"])
    try:
        score = float(score) * (10 if float(score) <= 10 else 1)
    except (TypeError, ValueError):
        score = 80.0
    score = max(0.0, min(100.0, score))

    rewrites_raw = data.get("BIO_REWRITES", fallback["BIO_REWRITES"])
    if isinstance(rewrites_raw, list):
        rewrite_options = [
            {"vibe": (r.get("vibe") if isinstance(r, dict) else "Option"), "text": (r.get("text") if isinstance(r, dict) else str(r))}
            for r in rewrites_raw
        ]
    else:
        rewrite_options = [
            {"vibe": "Witty & Playful", "text": rewrites_raw.get("witty", "")},
            {"vibe": "Authentic & Grounded", "text": rewrites_raw.get("deep", "")},
            {"vibe": "Warm & Casual", "text": rewrites_raw.get("casual", "")},
        ]

    if profile:
        row = await get_or_create_stage_data(db, "stage2", profile.id)
        row.profile_review_scores = {"overall": score, "raw": data}
        row.bio_rewrites = [r["text"] for r in rewrite_options]
        await db.commit()

    return {
        "status": "completed",
        "overall_score": round(score),
        "first_impression": data.get("FIRST_IMPRESSION", fallback["FIRST_IMPRESSION"]),
        "cliches_found": data.get("CLICHES_FOUND", fallback["CLICHES_FOUND"]),
        "rewrite_options": rewrite_options,
        "conversation_starters": data.get("CONVERSATION_STARTERS", fallback["CONVERSATION_STARTERS"]),
        "remove_this": data.get("REMOVE_THIS", fallback["REMOVE_THIS"]),
        "add_this": data.get("ADD_THIS", fallback["ADD_THIS"]),
        "photo_recommendations": [
            "Lead with a smiling eye-contact portrait in natural light.",
            "Include one unposed shot engaged in a real hobby.",
            "Keep group photos to one maximum, placed later in the stack.",
        ],
    }


async def analyze_conversation(db: AsyncSession, user: User, payload: Dict[str, Any]) -> Dict[str, Any]:
    history = (payload.get("history") or payload.get("chat_history") or "").strip()
    fallback_move = (
        "Acknowledge their story, then bridge to a real plan: 'That sounds amazing — have you "
        "checked out that new jazz lounge? We should grab a drink Thursday.'"
    )
    prompt = (
        "You are LoveGuru's dating conversation coach. Analyze this chat excerpt and respond ONLY "
        "with JSON with keys investment_ratio (string), banter_temperature (string), and "
        "recommended_next_moves (list of 3 strings).\n\nChat:\n" + history
    )
    data = await llm_json(prompt, LLMConfig.stage2_dating_coach, {
        "investment_ratio": "Balanced (48% vs 52%)",
        "banter_temperature": "Warm with steady momentum",
        "recommended_next_moves": [
            fallback_move,
            "Keep replies playful and concise to match their rhythm.",
            "Avoid multi-paragraph responses that create pressure.",
        ],
    })

    if user.profile:
        row = await get_or_create_stage_data(db, "stage2", user.profile.id)
        analyses = list(row.conversation_analyses or [])
        analyses.append({"input": history[:500], "result": data})
        row.conversation_analyses = analyses[-20:]
        await db.commit()

    return data


async def opening_message(db: AsyncSession, user: User, payload: Dict[str, Any]) -> Dict[str, Any]:
    their_profile = (payload.get("their_profile") or payload.get("profile_text") or "").strip()
    prompt = (
        "You are a witty dating coach. Based on this person's profile, generate 3 tailored opening "
        "lines (Warm, Witty, Direct) as JSON with key openers (list of {vibe, text}).\n\nProfile:\n"
        + their_profile
    )
    data = await llm_json(prompt, LLMConfig.stage2_dating_coach, {
        "openers": [
            {"vibe": "Warm", "text": "Your profile made me smile — what's the story behind your favorite photo?"},
            {"vibe": "Witty", "text": "You look like someone who takes their chai dangerously seriously. Prove me right?"},
            {"vibe": "Direct", "text": "You seem genuinely interesting. What's something you'd happily talk about for hours?"},
        ],
    })
    return {"status": "generated", "openers": data.get("openers", [])}


async def get_flags(db: AsyncSession, user: User) -> Dict[str, Any]:
    return {
        "green_flags": [
            {"flag": "Consistent communication", "significance": "Words match actions with low emotional turbulence."},
            {"flag": "Respects a polite 'no'", "significance": "Shows healthy emotional regulation and boundary comfort."},
            {"flag": "Curiosity about your mind", "significance": "Asks about your feelings, dreams, and perspectives."},
        ],
        "yellow_flags": [
            {"flag": "Slow to open up", "significance": "Could be healthy caution — watch for consistency over time."},
            {"flag": "Different texting rhythms", "significance": "A style difference, not a red flag, unless it's used punitively."},
        ],
        "red_flags": [
            {"flag": "Premature love-bombing", "significance": "Overwhelming affection in days 1-7 often masks insecurity or control."},
            {"flag": "Contempt toward service staff", "significance": "Predicts future contempt directed at you once novelty fades."},
            {"flag": "Hot-and-cold texting games", "significance": "Manufacturing artificial anxiety to create trauma bonds."},
        ],
    }


async def date_prep(db: AsyncSession, user: User, payload: Dict[str, Any]) -> Dict[str, Any]:
    venue = payload.get("venue", "a cozy cafe")
    return {
        "status": "ready",
        "outfit": "Smart-casual that reflects your personality; comfort over costume.",
        "venue_vibe_check": f"For {venue}: pick a spot with natural conversation flow and an easy exit.",
        "open_questions": [
            "What's something you've been obsessed with lately?",
            "What does a perfect ordinary weekend look like to you?",
            "What's a belief you've changed your mind about?",
            "Who in your life knows you best, and why?",
            "What's something you're quietly proud of?",
        ],
        "safety_checks": [
            "Share your location with a trusted friend.",
            "Meet in a public place and keep your own transport.",
            "Trust your gut — leave if anything feels off.",
        ],
    }


async def date_debrief(db: AsyncSession, user: User, payload: Dict[str, Any]) -> Dict[str, Any]:
    notes = (payload.get("notes") or "").strip()
    return {
        "status": "reflected",
        "gut_check": "Name how your body felt around them — calm and curious, or anxious and performing?",
        "energy_alignment": "Did you leave with more energy or less? That signal is data, not drama.",
        "date_two": "If you felt safe, seen, and genuinely curious — a low-pressure second meet is worth it.",
        "reflection": notes[:400] if notes else "Take 5 minutes to journal the highlight and one small friction point.",
    }


async def flirt_coaching(db: AsyncSession, user: User, payload: Dict[str, Any]) -> Dict[str, Any]:
    scenario = payload.get("scenario", "approaching")
    return {
        "coaching_principle": "Flirting is creating a shared conspiracy of playfulness — connection first, cleverness second.",
        "tactical_lines": [
            "Playful observation: 'I have a strong feeling you take your coffee very seriously.'",
            "Warm curiosity: 'What was the highlight of your week that had nothing to do with work?'",
            "Subtle challenge: 'I bet you can't guess my favorite hidden dessert spot in this city.'",
        ],
        "scenario": scenario,
    }


async def get_conversation_starters(db: AsyncSession, user: User) -> Dict[str, Any]:
    return {
        "starters": [
            "What's a small thing that instantly makes your day better?",
            "What's the most spontaneous thing you've done recently?",
            "If you could master one skill overnight, what would it be?",
            "What's a movie or song you'll never get tired of?",
        ]
    }
