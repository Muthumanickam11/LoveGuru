"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Response Builder Agent                  ║
║  Composes final reply, optional RAG summary, quick replies.   ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging

from agents import safe_llm_json
from config.llm_config import LLMConfig
from services import chat_service

logger = logging.getLogger(__name__)


class ResponseBuilderAgent:
    name = "response_builder_agent"

    async def run(self, state: dict) -> dict:
        specialist = state.get("specialist_coaching") or ""
        rag_summary = state.get("rag_context", {}).get("summary", "")
        personality = state.get("ai_personality", "warm_friend")

        # Quick replies based on stage & crisis state
        quick_replies = await chat_service.generate_quick_replies(
            state.get("current_stage", "single"),
            state.get("crisis_assessment", {}).get("level", "safe"),
        )

        final = (specialist if specialist else rag_summary) or (
            "I'm here with you in this moment. Tell me a little more about what's going on, "
            "and we'll find the clearest path together."
        )

        # Personality-aware polish (mock-friendly)
        persona = {
            "warm_friend": "I'm right here with you.",
            "wise_mentor": "Consider this carefully.",
            "gentle_coach": "Small steps still move you forward.",
            "direct_advisor": "Here's the honest next move.",
        }.get(personality, "I'm right here with you.")

        return {
            **state,
            "final_response": f"{persona} {final}".strip(),
            "quick_replies": quick_replies,
        }


response_builder_agent = ResponseBuilderAgent()