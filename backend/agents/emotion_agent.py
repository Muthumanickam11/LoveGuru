"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Emotion Agent                           ║
║  8-dimensional emotion detection on every user message.       ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging

from agents import safe_llm_json
from config.llm_config import LLMConfig

logger = logging.getLogger(__name__)

_DEFAULT_VECTOR = {
    "sadness": 0.1, "anxiety": 0.1, "anger": 0.0, "loneliness": 0.1,
    "hope": 0.6, "love": 0.4, "confusion": 0.2, "joy": 0.4,
}


class EmotionAgent:
    name = "emotion_agent"

    async def run(self, state: dict) -> dict:
        message = state.get("raw_message", "")
        fallback = {"primary_emotion": "hopeful", "intensity": 0.6, **_DEFAULT_VECTOR}
        prompt = (
            "Detect the user's emotional state. Respond ONLY with JSON: "
            "{\"primary_emotion\", \"intensity\" (0-1), \"sadness\", \"anxiety\", "
            "\"anger\", \"loneliness\", \"hope\", \"love\", \"confusion\", \"joy\" (each 0-1)}.\n\n"
            "Message:\n" + message
        )
        data = await safe_llm_json(prompt, LLMConfig.emotion_detector, fallback)
        vector = {k: data.get(k, fallback.get(k, 0.0)) for k in _DEFAULT_VECTOR}
        return {
            **state,
            "primary_emotion": data.get("primary_emotion", fallback["primary_emotion"]),
            "emotion_intensity": data.get("intensity", fallback["intensity"]),
            "emotion_vector": vector,
        }


emotion_agent = EmotionAgent()