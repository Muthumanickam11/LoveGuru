"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Partner Analysis Agent (Stage 1)        ║
║  Reality-check analysis of a dream-partner description.       ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging

from agents import safe_llm_json
from agents import safe_llm_json
from config.llm_config import LLMConfig


def _as_list(value) -> list:
    if isinstance(value, list):
        return value
    if isinstance(value, str):
        return [value]
    return []

logger = logging.getLogger(__name__)


class PartnerAnalysisAgent:
    name = "partner_analysis_agent"

    async def run(self, state: dict) -> dict:
        description = state.get("partner_description") or state.get("raw_message", "")
        fallback = {
            "REALISM_SCORE": 78,
            "HEALTHY_EXPECTATIONS": ["Emotional consistency", "Shared core values"],
            "EXAMINE_EXPECTATIONS": [
                {"original": "Always available", "reality": "Humans are not available 24/7",
                 "what_they_really_need": "Predictable warmth"}],
            "RECONSIDER_EXPECTATIONS": [
                {"original": "Never busy but always ambitious", "why": "Traits in tension",
                 "healthier_version": "Ambitious with intentional time"}],
            "WHAT_REVEALS": "Your vision reflects real psychological insight.",
            "REFINED_VISION": "A partner emotionally consistent and aligned with your values.",
        }
        prompt = (
            "Generate a Reality Check Analysis for this dream partner description. Respond ONLY with "
            "JSON keys: REALISM_SCORE (0-100), HEALTHY_EXPECTATIONS (list), EXAMINE_EXPECTATIONS "
            "(list of {original, reality, what_they_really_need}), RECONSIDER_EXPECTATIONS "
            "(list of {original, why, healthier_version}), WHAT_REVEALS, REFINED_VISION.\n\n"
            "Description:\n" + description
        )
        data = await safe_llm_json(prompt, LLMConfig.stage1_partner_analyzer, fallback)
        return {
            **state,
            "realism_score": data.get("REALISM_SCORE", fallback["REALISM_SCORE"]),
            "healthy_expectations": _as_list(data.get("HEALTHY_EXPECTATIONS") or fallback["HEALTHY_EXPECTATIONS"]),
            "examine_expectations": data.get("EXAMINE_EXPECTATIONS", fallback["EXAMINE_EXPECTATIONS"]),
            "reconsider_expectations": data.get("RECONSIDER_EXPECTATIONS", fallback["RECONSIDER_EXPECTATIONS"]),
            "partner_insight": data.get("WHAT_REVEALS", fallback["WHAT_REVEALS"]),
            "refined_vision": data.get("REFINED_VISION", fallback["REFINED_VISION"]),
        }


partner_analysis_agent = PartnerAnalysisAgent()