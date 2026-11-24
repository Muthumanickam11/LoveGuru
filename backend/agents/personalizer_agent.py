"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Personalizer Agent                      ║
║  Tailors the final response to the user's stage, attachment,  ║
║  and love language so every reply feels uniquely theirs.      ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging

from agents import safe_llm_text
from config.llm_config import LLMConfig

logger = logging.getLogger(__name__)


class PersonalizerAgent:
    name = "personalizer_agent"

    async def run(self, state: dict) -> dict:
        draft = state.get("final_response", "")
        prompt = (
            "Rephrase the draft coaching reply to better fit the user profile below. Keep it warm, "
            "concise, and within the same structure.\n"
            f"Stage: {state.get('current_stage')}\n"
            f"Attachment style: {state.get('attachment_style')}\n"
            f"Love language: {state.get('love_language')}\n"
            f"AI personality: {state.get('ai_personality')}\n\nDraft:\n{draft}"
        )
        personalized = await safe_llm_text(prompt, LLMConfig.personalizer, draft)
        return {**state, "final_response": personalized.strip() or draft}


personalizer_agent = PersonalizerAgent()