"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Screenshot Reader & Chat Decoder       ║
║         OCR and conversation dynamic extractor               ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging
from typing import Dict, Any, List
from tools.image_analyzer import analyze_image

logger = logging.getLogger(__name__)


async def parse_screenshot(screenshot_url: str, app_type: str = "dating_app") -> Dict[str, Any]:
    """Extracts conversational dialogue and provides dynamic decoding."""
    result = await analyze_image(
        image_url=screenshot_url,
        context=f"Extract dialogue flow from {app_type} screenshot. Identify response times, emotional tone, and next best replies.",
        stage="finding"
    )

    return {
        "app_detected": app_type,
        "transcription_summary": result.get("analysis", ""),
        "tactical_replies": [
            "Keep it light and reference something specific they mentioned earlier.",
            "Ask an open-ended question that invites a story, not a yes/no response.",
            "Give them space to match your investment before sending a follow-up.",
        ],
        "vibe_check": "Positive conversational bid with reciprocal curiosity.",
    }
