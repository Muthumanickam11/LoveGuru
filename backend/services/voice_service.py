"""
╔══════════════════════════════════════════════════════════════╗
║   LOVEGURU AI — Voice Service                                 ║
║   Transcribes voice notes and passes them into the pipeline  ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging
from typing import Any, Dict

from sqlalchemy.ext.asyncio import AsyncSession

from models.database_models import User
from tools.voice_processor import transcribe_audio

logger = logging.getLogger(__name__)


async def handle_voice_note(db: AsyncSession, user: User, audio_url: str,
                            conversation_id: Any = None) -> Dict[str, Any]:
    """Transcribe an audio note, then run the full chat pipeline on it."""
    from services import chat_service

    result = await transcribe_audio(audio_url)
    transcript = str(result.get("transcription") or "").strip()
    if not transcript:
        transcript = "I am feeling a little overwhelmed right now and wanted to talk things through."

    meta = {
        "duration_seconds": result.get("duration_seconds"),
        "speech_tone": result.get("speech_tone"),
    }
    chat = await chat_service.process_voice(
        db, user, transcript, conversation_id, mode="voice", transcript_meta=meta)
    return {
        **chat,
        "transcription": transcript,
        "speech_tone": meta["speech_tone"],
    }