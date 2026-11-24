"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Physical Health Agent                   ║
║  Reads sleep / activity cues and folds gentle habits in.     ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging
import re

from agents import safe_llm_json
from config.llm_config import LLMConfig

logger = logging.getLogger(__name__)

_SLEEP_RE = re.compile(r"\bsleep|tired|exhaust|insomnia|night\b", re.IGNORECASE)
_MOOD_RE = re.compile(r"\benergy|workout|gym|walk|run\b", re.IGNORECASE)


class PhysicalHealthAgent:
    name = "physical_health_agent"

    async def run(self, state: dict) -> dict:
        message = state.get("raw_message", "")
        signals = []
        if _SLEEP_RE.search(message):
            signals.append("sleep")
        if _MOOD_RE.search(message):
            signals.append("movement")

        fallback = {
            "insight": "Physical state and emotional state are two lanes of the same road.",
            "habit_suggestion": "Before the brain decides, move the body for 90 seconds.",
            "relevant": bool(signals),
        }
        prompt = (
            "Give one physical-health insight tied to sleep, energy, or movement for someone "
            "navigating love stress. Respond ONLY with JSON {insight, habit_suggestion, relevant}.\n\n"
            "Message:\n" + message
        )
        data = await safe_llm_json(prompt, LLMConfig.personalizer, fallback)
        return {
            **state,
            "physical_health": {
                "signals": signals,
                "insight": data.get("insight", fallback["insight"]),
                "habit_suggestion": data.get("habit_suggestion", fallback["habit_suggestion"]),
            },
        }


physical_health_agent = PhysicalHealthAgent()