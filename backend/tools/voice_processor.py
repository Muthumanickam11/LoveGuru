"""
LoveGuru AI — Voice Processor Tool
Audio transcription via Groq Whisper (same API key tier as the LLM).
"""

import logging
import httpx
from typing import Dict, Any
from config.settings import settings

logger = logging.getLogger(__name__)


async def transcribe_audio(audio_url: str, language: str = None) -> Dict[str, Any]:
    """
    Transcribes an audio file using Groq's Whisper endpoint.

    Supports URLs and local file paths. Returns transcription + a
    best-effort voice-emotion hint derived from transcript length.
    """
    logger.info(f"Transcribing audio: {audio_url}")

    api_key = settings.GROQ_API_KEY
    if not api_key or api_key.startswith("placeholder"):
        logger.warning("GROQ_API_KEY not set — returning mock transcription.")
        return {
            "success": True,
            "transcription": "I am feeling a little overwhelmed right now and wanted to talk things through.",
            "duration_seconds": 12.5,
            "speech_tone": "reflective",
            "source": "mock",
        }

    try:
        # Fetch audio bytes (URL or local path)
        if audio_url.startswith("http"):
            async with httpx.AsyncClient(timeout=30) as client:
                resp = await client.get(audio_url)
                resp.raise_for_status()
                audio_bytes = resp.content
                filename = audio_url.split("/")[-1] or "audio.webm"
        else:
            with open(audio_url, "rb") as f:
                audio_bytes = f.read()
            filename = audio_url.split("/")[-1] or "audio.webm"

        # Groq Whisper transcription
        from groq import Groq
        groq_client = Groq(api_key=api_key)
        transcription = groq_client.audio.transcriptions.create(
            file=(filename, audio_bytes),
            model="whisper-large-v3",
            language=language,
            response_format="verbose_json",
        )

        text = getattr(transcription, "text", None) or str(transcription)
        duration = getattr(transcription, "duration", None) or 0.0

        # Crude voice-emotion hint (text length / pacing proxy)
        words = len(text.split())
        if words < 5:
            tone = "withdrawn"
        elif words < 20:
            tone = "reflective"
        elif "!" in text or "?" in text:
            tone = "anxious"
        else:
            tone = "steady"

        return {
            "success": True,
            "transcription": text,
            "duration_seconds": round(float(duration), 1),
            "speech_tone": tone,
            "source": "groq_whisper",
        }
    except Exception as e:
        logger.error(f"Groq Whisper transcription failed: {e}")
        return {
            "success": False,
            "transcription": "",
            "error": str(e),
            "source": "error",
        }
