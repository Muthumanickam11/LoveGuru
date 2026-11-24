"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Rate Limiter Middleware                 ║
║  In-memory sliding-window limiter per client IP per route.    ║
╚══════════════════════════════════════════════════════════════╝
"""

import time
import logging
from collections import defaultdict, deque
from typing import Deque, Dict, Optional

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

from config.settings import settings

logger = logging.getLogger(__name__)


class RateLimiter:
    """Sliding-window limiter keyed per (ip, path)."""

    def __init__(
        self,
        max_requests: int = 60,
        window_seconds: int = 60,
        crisis_max_requests: int = 120,
        exempt_paths: tuple = ("/docs", "/redoc", "/api/docs", "/api/redoc", "/api/v1/health"),
        crisis_prefixes: tuple = ("/api/v1/emergency",),
    ):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.crisis_max_requests = crisis_max_requests
        self.exempt_paths = exempt_paths
        self.crisis_prefixes = crisis_prefixes
        self._hits: Dict[str, Deque[float]] = defaultdict(deque)

    def _key(self, ip: str, path: str) -> str:
        return f"{ip}:{path.split('?')[0]}"

    def _exempt(self, path: str) -> bool:
        return any(path.startswith(e) for e in self.exempt_paths)

    def _limit_for(self, path: str) -> int:
        if any(path.startswith(p) for p in self.crisis_prefixes):
            return self.crisis_max_requests
        return self.max_requests

    def allow(self, ip: str, path: str) -> bool:
        if self._exempt(path):
            return True
        key = self._key(ip, path)
        now = time.monotonic()
        window = self._hits[key]
        while window and now - window[0] > self.window_seconds:
            window.popleft()
        if len(window) >= self._limit_for(path):
            return False
        window.append(now)
        return True


rate_limiter = RateLimiter(
    max_requests=settings.RATE_LIMIT_PER_MINUTE,
    crisis_max_requests=settings.CRISIS_RATE_LIMIT_PER_MINUTE,
)


class RateLimiterMiddleware(BaseHTTPMiddleware):
    """FastAPI/Starlette middleware enforcing the shared rate limiter."""

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host if request.client else "unknown"
        path = request.url.path
        if not rate_limiter.allow(client_ip, path):
            return JSONResponse(
                status_code=429,
                content={"detail": "Too many requests. Please slow down and try again shortly."},
                headers={"Retry-After": str(rate_limiter.window_seconds)},
            )
        return await call_next(request)
