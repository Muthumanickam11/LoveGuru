"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Intake Agent                            ║
║  Synthesizes onboarding answers into a personalized profile.  ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging

from agents import safe_llm_text
from config.llm_config import LLMConfig

logger = logging.getLogger(__name__)


class IntakeAgent:
    name = "intake_agent"

    async def run(self, state: dict) -> dict:
        answers = state.get("intake_answers") or state.get("onboarding_answers") or {}
        message = state.get("raw_message", "")
        prompt = (
            "Summarize this user's romantic journey into a warm 2-3 sentence personal profile "
            "that captures their stage, attachment tendencies, and what they want to work on.\n"
            f"Onboarding input:\n{answers}\nLatest message:\n{message}"
        )
        summary = await safe_llm_text(
            prompt, LLMConfig.personalizer,
            "A seeker working toward intentional, self-aware love.",
        )
        return {
            **state,
            "onboarding_summary": summary.strip(),
            "intake_completed": True,
        }


intake_agent = IntakeAgent()