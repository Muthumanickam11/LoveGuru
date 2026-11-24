"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Authentication Router                  ║
║  POST /auth/register  POST /auth/login  POST /auth/google    ║
║  POST /auth/refresh   POST /auth/logout  DELETE /auth/account║
╚══════════════════════════════════════════════════════════════╝
"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
import uuid
import logging

from config.database import get_db
from config.settings import settings
from services.auth_service import (
    create_user, authenticate_user, get_user_by_email, get_user_by_id,
    create_access_token, create_refresh_token, decode_token,
)

logger = logging.getLogger(__name__)
router = APIRouter()
bearer_scheme = HTTPBearer(auto_error=False)


# ─────────────────────────────────────────────────────────────
# SCHEMAS
# ─────────────────────────────────────────────────────────────

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    display_name: Optional[str] = "Friend"

    @field_validator("password")
    @classmethod
    def validate_password(cls, v):
        if len(v) < 6:
            raise ValueError("Password must be at least 6 characters")
        return v

    @field_validator("display_name")
    @classmethod
    def validate_name(cls, v):
        if not v or len(v.strip()) < 1:
            return "Friend"
        return v.strip()


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class GoogleAuthRequest(BaseModel):
    google_token: str
    display_name: str


class RefreshRequest(BaseModel):
    refresh_token: str


class AuthResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user: dict


# ─────────────────────────────────────────────────────────────
# DEPENDENCY — current user
# ─────────────────────────────────────────────────────────────

async def get_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(bearer_scheme),
    db: AsyncSession = Depends(get_db),
):
    # Dev mode: bypass auth and return a default user
    if settings.AUTH_DISABLED:
        from services.auth_service import get_or_create_dev_user
        return await get_or_create_dev_user(db)

    if credentials is None or not credentials.credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = credentials.credentials
    payload = decode_token(token)
    if not payload or payload.get("type") != "access":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user_id = uuid.UUID(payload["sub"])
    user = await get_user_by_id(db, user_id)
    if not user or not user.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user


# ─────────────────────────────────────────────────────────────
# POST /auth/register
# ─────────────────────────────────────────────────────────────

@router.post("/register", response_model=AuthResponse, status_code=status.HTTP_201_CREATED)
async def register(body: RegisterRequest, db: AsyncSession = Depends(get_db)):
    """Register a new LoveGuru AI user."""
    existing = await get_user_by_email(db, body.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An account with this email already exists",
        )

    user, access_token, refresh_token = await create_user(
        db=db,
        email=body.email,
        display_name=body.display_name,
        password=body.password,
    )

    return AuthResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        user={
            "id": str(user.id),
            "email": user.email,
            "display_name": body.display_name,
            "onboarding_completed": False,
            "stage": "single",
        },
    )


# ─────────────────────────────────────────────────────────────
# POST /auth/login
# ─────────────────────────────────────────────────────────────

@router.post("/login", response_model=AuthResponse)
async def login(body: LoginRequest, db: AsyncSession = Depends(get_db)):
    """Login with email and password."""
    user = await authenticate_user(db, body.email, body.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    profile = user.profile
    stage = profile.current_stage.value if profile else "single"

    access_token = create_access_token(str(user.id), stage=stage)
    refresh_token = create_refresh_token(str(user.id))

    return AuthResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        user={
            "id": str(user.id),
            "email": user.email,
            "display_name": profile.display_name if profile else "",
            "onboarding_completed": profile.onboarding_completed if profile else False,
            "stage": stage,
            "ai_personality": profile.ai_personality.value if profile else "warm_friend",
        },
    )


# ─────────────────────────────────────────────────────────────
# POST /auth/refresh
# ─────────────────────────────────────────────────────────────

@router.post("/refresh")
async def refresh_token(body: RefreshRequest, db: AsyncSession = Depends(get_db)):
    """Refresh an expired access token using the refresh token."""
    payload = decode_token(body.refresh_token)
    if not payload or payload.get("type") != "refresh":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

    user_id = uuid.UUID(payload["sub"])
    user = await get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    stage = user.profile.current_stage.value if user.profile else "single"
    new_access_token = create_access_token(str(user.id), stage=stage)

    return {"access_token": new_access_token, "token_type": "bearer"}


# ─────────────────────────────────────────────────────────────
# POST /auth/logout
# ─────────────────────────────────────────────────────────────

@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(current_user=Depends(get_current_user)):
    """Logout — client should clear tokens locally. Server-side blacklist can be added via Redis."""
    # TODO: Add token blacklist via Redis for production security
    return


# ─────────────────────────────────────────────────────────────
# GET /auth/me
# ─────────────────────────────────────────────────────────────

@router.get("/me")
async def get_me(current_user=Depends(get_current_user)):
    """Get current authenticated user details."""
    profile = current_user.profile
    return {
        "id": str(current_user.id),
        "email": current_user.email,
        "display_name": profile.display_name if profile else "",
        "stage": profile.current_stage.value if (profile and profile.current_stage) else "single",
        "ai_personality": profile.ai_personality.value if (profile and profile.ai_personality) else "warm_friend",
        "onboarding_completed": profile.onboarding_completed if profile else False,
        "created_at": current_user.created_at.isoformat() if current_user.created_at else None,
    }


@router.put("/profile")
async def update_profile(body: dict, current_user=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    """Update user profile preferences."""
    profile = current_user.profile
    if profile:
        if "display_name" in body:
            profile.display_name = body["display_name"]
        if "stage" in body:
            from models.database_models import LifeStage
            try:
                profile.current_stage = LifeStage(body["stage"])
            except ValueError:
                pass
        if "ai_personality" in body:
            from models.database_models import AIPersonality
            try:
                profile.ai_personality = AIPersonality(body["ai_personality"])
            except ValueError:
                pass
        if "onboarding_completed" in body:
            profile.onboarding_completed = body["onboarding_completed"]
        await db.commit()
    return {"status": "updated", "message": "Profile updated successfully"}


@router.post("/onboarding")
async def complete_onboarding(body: dict, current_user=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    """Save onboarding selections."""
    profile = current_user.profile
    if profile:
        if "stage" in body:
            from models.database_models import LifeStage
            try:
                profile.current_stage = LifeStage(body["stage"])
            except ValueError:
                pass
        if "ai_personality" in body:
            from models.database_models import AIPersonality
            try:
                profile.ai_personality = AIPersonality(body["ai_personality"])
            except ValueError:
                pass
        if "display_name" in body:
            profile.display_name = body["display_name"]
        profile.onboarding_completed = True
        await db.commit()
    return {"status": "completed", "message": "Onboarding complete"}

