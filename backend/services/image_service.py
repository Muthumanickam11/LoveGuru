"""
╔══════════════════════════════════════════════════════════════╗
║   LOVEGURU AI — Image Service                                 ║
║   Profile-photo and screenshot analysis through the pipeline ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging
from typing import Any, Dict, Optional

from sqlalchemy.ext.asyncio import AsyncSession

from models.database_models import User
from tools.image_analyzer import analyze_image

logger = logging.getLogger(__name__)


async def handle_image(db: AsyncSession, user: User, image_url: str,
                       message: str = "", conversation_id: Optional[str] = None) -> Dict[str, Any]:
    from services import chat_service
    return await chat_service.process_image(db, user, image_url, message, conversation_id)


async def handle_screenshot(db: AsyncSession, user: User, screenshot_url: str,
                            message: str = "", conversation_id: Optional[str] = None) -> Dict[str, Any]:
    from services import chat_service
    return await chat_service.process_screenshot(db, user, screenshot_url, message, conversation_id)