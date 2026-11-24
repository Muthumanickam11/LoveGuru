"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Heartbreak Coach Agent (Stage 4)        ║
║  Grief-weather-aware recovery coaching after a breakup.       ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging

from agents import safe_llm_json, safe_llm_text
from config.llm_config import LLMConfig

logger = logging.getLogger(__name__)


class HeartbreakCoachAgent:
    name = "heartbreak_coach_agent"

    async def run(self, state: dict) -> dict:
        message = state.get("raw_message", "")
        fallback = {"grief_weather": "rain", "validation": "Your feeling is a normal part of loss."}
        prompt = (
            "Identify this person's current grief weather from one of: storm, overcast, rain, "
            "clearing, sun. Respond ONLY with JSON {grief_weather, validation}.\n\nMessage:\n"
            + message
        )
        data = await safe_llm_json(prompt, LLMConfig.stage4_heartbreak_coach, fallback)
        weather = str(data.get("grief_weather", "rain")).lower()
        coaching = await safe_llm_text(
            "Give gentle, validating heartbreak-recovery coaching for someone in "
            f"'{weather}' grief weather.\nMessage:\n{message}",
            LLMConfig.stage4_heartbreak_coach,
            "You are allowed to grieve. Take small, kind steps today.",
        )
        return {
            **state,
            "grief_weather": weather,
            "specialist_coaching": coaching,
            "validation": data.get("validation", fallback["validation"]),
        }


heartbreak_coach_agent = HeartbreakCoachAgent()