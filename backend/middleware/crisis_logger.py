"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Crisis Logger Middleware                ║
║  Logs a warning whenever a chat/emergency response signals    ║
║  elevated crisis risk so keepers can review the safety path.  ║
╚══════════════════════════════════════════════════════════════╝
"""

import json
import logging
from typing import Callable

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

logger = logging.getLogger(__name__)

_CRISIS_LEVELS = ("high", "critical")
_WATCH_PREFIXES = ("/api/v1/chat", "/api/v1/emergency")


class CrisisLoggerMiddleware(BaseHTTPMiddleware):
    """Buffers small JSON responses and flags crisis-level replies.

    Only inspects responses on chat/emergency routes to avoid overhead elsewhere.
    """

    async def dispatch(self, request: Request, call_next: Callable):
        response = await call_next(request)
        path = request.url.path

        if not any(path.startswith(p) for p in _WATCH_PREFIXES):
            return response
        if response.status_code >= 400:
            return response

        content_type = response.headers.get("content-type", "")
        if "application/json" not in content_type:
            return response

        body = b""
        try:
            body = b"".join([chunk async for chunk in response.body_iterator])
            payload = json.loads(body.decode("utf-8", errors="ignore"))
            level = payload.get("crisis_level", "safe") if isinstance(payload, dict) else "safe"
            if level in _CRISIS_LEVELS:
                user_id = getattr(request.state, "user_id", "unknown")
                logger.warning(
                    f"⚠️ CRISIS SIGNAL — level={level} path={path} user={user_id}")
        except Exception as e:  # pragma: no cover
            logger.debug(f"Crisis logger skipped: {e}")

        return Response(
            content=body,
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.media_type,
        )
