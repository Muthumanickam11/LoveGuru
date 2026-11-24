"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Memory Agent                            ║
║  Writes mood logs, streaks, and pattern records from a turn.  ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging

from agents import safe_llm_text
from config.llm_config import LLMConfig
from memory import pattern_memory, session_memory as session_memory_module
from memory import user_memory as user_memory_module

logger = logging.getLogger(__name__)


class MemoryAgent:
    name = "memory_agent"

    async def run(self, state: dict) -> dict:
        user_id = state.get("user_id")
        mood_logged = False
        trend_logged = False
        if user_id:
            emotion = state.get("primary_emotion", "neutral")
            try:
                await user_memory_module.update_mood_log(
                    user_id=user_id,
                    primary_emotion=emotion or "steady",
                    intensity=float(state.get("emotion_intensity", 0.6) or 0.6),
                    stage=state.get("current_stage", "single"),
                )
                mood_logged = True
            except Exception as e:
                logger.warning(f"[MemoryAgent] mood log failed: {e}")
            try:
                await session_memory_module.update_streak(user_id, "app_checkin")
                trend_logged = True
            except Exception as e:
                logger.warning(f"[MemoryAgent] streak update failed: {e}")

        return {
            **state,
            "mood_logged": mood_logged,
            "streaks_updated": trend_logged,
            "memory_updated": mood_logged or trend_logged,
        }


memory_agent = MemoryAgent()