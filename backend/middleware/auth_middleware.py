"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Auth Middleware                         ║
║  Optional JWT verification helper + guards for user endpoints.║
║  NOTE: not auto-wired globally — dependency-based auth in     ║
║  routers/auth_router.py remains the primary mechanism.        ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging
from typing import Optional

from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt

from config.settings import settings

logger = logging.getLogger(__name__)

security = HTTPBearer(auto_error=False)

_PUBLIC_PREFIXES = ("/docs", "/redoc", "/api/docs", "/api/redoc", "/api/v1/health",
                    "/api/v1/auth/register", "/api/v1/auth/login",
                    "/api/v1/auth/refresh", "/api/v1/emergency/resources")


def is_public_path(path: str) -> bool:
    return any(path.startswith(p) for p in _PUBLIC_PREFIXES)


async def get_token_from_request(
    request: Request,
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
) -> Optional[str]:
    if credentials:
        return credentials.credentials
    return None


async def verify_access_token(token: str) -> dict:
    """Decode and validate a LoveGuru access token."""
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except JWTError as e:
        raise HTTPException(status_code=401, detail="Invalid or expired token") from e


def require_auth():
    """DB-aware dependency factory that resolves the logged-in user."""
    async def dependency(
        request: Request,
        credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
    ):
        if credentials is None:
            raise HTTPException(status_code=401, detail="Not authenticated")
        payload = await verify_access_token(credentials.credentials)

        from uuid import UUID
        from config.database import AsyncSessionLocal
        from sqlalchemy import select
        from models.database_models import User
        try:
            user_id = UUID(str(payload.get("sub")))
        except (ValueError, TypeError) as e:
            raise HTTPException(status_code=401, detail="Invalid token subject") from e
        async with AsyncSessionLocal() as db:
            user = (await db.execute(
                select(User).where(User.id == user_id))).scalar_one_or_none()
        if user is None:
            raise HTTPException(status_code=401, detail="User no longer exists")
        request.state.user_id = str(user.id)
        return user

    return dependency