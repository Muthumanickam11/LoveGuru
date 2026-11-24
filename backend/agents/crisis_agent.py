"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Crisis Agent (Safety Gate)              ║
║  Zero-miss detection of self-harm / harm risk in messages.    ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging
import re

from agents import safe_llm_json
from config.llm_config import LLMConfig

logger = logging.getLogger(__name__)

_HIGH_RISK = re.compile(
    r"\b(kill|die|suicid|end (my|it all)|hurt (myself|me)|self.?harm|no reason to live"
    r"|can''?t go on|don''?t want to live|better off without|hurt those|take (my own life|a knife|an overdose))\b",
    re.IGNORECASE,
)


class CrisisAgent:
    name = "crisis_agent"

    def is_high_risk(self, message: str) -> bool:
        return bool(_HIGH_RISK.search(message or ""))

    async def run(self, state: dict) -> dict:
        message = state.get("raw_message", "")
        if self.is_high_risk(message):
            assessment = {"level": "high", "confidence": 0.9, "triggers": ["self-harm language"]}
        else:
            fallback = {"level": "safe", "confidence": 0.99, "triggers": []}
            prompt = (
                "Assess the crisis risk of this message. Respond ONLY with JSON "
                "{level: 'safe'|'moderate'|'high'|'critical', confidence, triggers (list)}.\n\n"
                "Message:\n" + message
            )
            assessment = await safe_llm_json(prompt, LLMConfig.crisis_safety, fallback)
            level = str(assessment.get("level", "safe")).lower()
            if level not in ("safe", "moderate", "high", "critical"):
                level = "safe"
            assessment["level"] = level

        triggered = assessment.get("level") in ("high", "critical")
        if triggered:
            logger.warning(f"[CrisisAgent] level={assessment.get('level')}")
        return {
            **state,
            "crisis_assessment": assessment,
            "crisis_triggered": triggered,
        }


crisis_agent = CrisisAgent()