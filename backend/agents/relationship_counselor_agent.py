"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Relationship Counselor Agent (Stage 3)  ║
║  Gottman-informed relational coaching for couples.            ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging

from agents import safe_llm_json, safe_llm_text
from config.llm_config import LLMConfig
from prompts.stage3_prompts import STAGE3_SPECIALIST_PROMPT

logger = logging.getLogger(__name__)


class RelationshipCounselorAgent:
    name = "relationship_counselor_agent"

    async def run(self, state: dict) -> dict:
        message = state.get("raw_message", "")
        fallback = (
            "Consider naming the pattern without blame: 'I feel X when our plans shift without "
            "warning. What I need is Y. Can we adjust together?'"
        )
        prompt = STAGE3_SPECIALIST_PROMPT + (
            "\n\nRespond to the user's message with Gottman-informed, warmth-first coaching.\n"
            f"User's stage: {state.get('current_stage')}\nMessage:\n{message}"
        )
        coaching = await safe_llm_text(prompt, LLMConfig.stage3_relationship_coach, fallback)
        return {**state, "specialist_coaching": coaching}


relationship_counselor_agent = RelationshipCounselorAgent()