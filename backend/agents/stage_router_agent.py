"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Stage Router Agent                      ║
║  Classifies a message into one of the four love stages.       ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging

from agents import safe_llm_json
from config.llm_config import LLMConfig

logger = logging.getLogger(__name__)


class StageRouterAgent:
    name = "stage_router_agent"

    async def run(self, state: dict) -> dict:
        message = state.get("raw_message", "")
        declared = state.get("current_stage", "single")
        fallback = {"stage": declared if declared in ("single", "finding", "relationship", "heartbreak") else "single",
                    "confidence": 0.6}
        prompt = (
            "You are LoveGuru's stage router. Classify the user's message into one stage: "
            "single, finding, relationship, or heartbreak. Respond ONLY with JSON "
            "{stage, confidence, reasoning}.\n\nMessage:\n" + message
        )
        data = await safe_llm_json(prompt, LLMConfig.stage_router, fallback)
        stage = str(data.get("stage", fallback["stage"])).lower()
        if stage not in ("single", "finding", "relationship", "heartbreak"):
            stage = fallback["stage"]
        return {**state, "routed_stage": stage, "routing_confidence": data.get("confidence", 0.6)}


stage_router_agent = StageRouterAgent()