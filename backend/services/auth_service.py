"""
╔══════════════════════════════════════════════════════════════╗
║       LOVEGURU AI — Authentication Service                   ║
║  JWT tokens, bcrypt hashing, Google OAuth verification       ║
╚══════════════════════════════════════════════════════════════╝
"""

import uuid
from datetime import datetime, timezone, timedelta
from typing import Optional, Tuple
from jose import JWTError, jwt
import bcrypt
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import logging

from config.settings import settings
from models.database_models import User, UserProfile, UserPsychology, AIPersonality, LifeStage

logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────────────────────
# PASSWORD UTILITIES (bcrypt directly — avoids passlib/bcrypt 5.x breaks)
# ─────────────────────────────────────────────────────────────

def _pw_bytes(password: str) -> bytes:
    return password.encode("utf-8")[:72]


def hash_password(password: str) -> str:
    return bcrypt.hashpw(_pw_bytes(password), bcrypt.gensalt()).decode("utf-8")


def verify_password(plain: str, hashed: str) -> bool:
    try:
        return bcrypt.checkpw(_pw_bytes(plain), hashed.encode("utf-8"))
    except (ValueError, TypeError):
        return False


# ─────────────────────────────────────────────────────────────
# JWT UTILITIES
# ─────────────────────────────────────────────────────────────

def create_access_token(user_id: str, stage: str = "single") -> str:
    expire = datetime.now(timezone.utc).replace(tzinfo=None) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return jwt.encode(
        {"sub": user_id, "stage": stage, "type": "access", "exp": expire},
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )


def create_refresh_token(user_id: str) -> str:
    expire = datetime.now(timezone.utc).replace(tzinfo=None) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    return jwt.encode(
        {"sub": user_id, "type": "refresh", "exp": expire},
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )


def decode_token(token: str) -> Optional[dict]:
    try:
        return jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
    except JWTError as e:
        logger.warning(f"JWT decode error: {e}")
        return None


# ─────────────────────────────────────────────────────────────
# USER CRUD
# ─────────────────────────────────────────────────────────────

async def get_user_by_email(db: AsyncSession, email: str) -> Optional[User]:
    result = await db.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()


async def get_user_by_id(db: AsyncSession, user_id: uuid.UUID) -> Optional[User]:
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()


async def create_user(
    db: AsyncSession,
    email: str,
    display_name: str,
    password: Optional[str] = None,
    google_id: Optional[str] = None,
) -> Tuple[User, str, str]:
    """
    Creates a new user with profile and psychology baseline.
    Returns (user, access_token, refresh_token).
    """
    # Create user
    user = User(
        email=email,
        password_hash=hash_password(password) if password else None,
        google_id=google_id,
        is_verified=bool(google_id),  # Google users are pre-verified
    )
    db.add(user)
    await db.flush()  # Get the UUID

    # Create profile
    profile = UserProfile(
        user_id=user.id,
        display_name=display_name,
        current_stage=LifeStage.SINGLE,
        ai_personality=AIPersonality.WARM_FRIEND,
        onboarding_completed=False,
    )
    db.add(profile)

    # Create psychology baseline
    psychology = UserPsychology(user_id=user.id)
    db.add(psychology)

    await db.commit()
    await db.refresh(user)

    # Generate tokens
    access_token = create_access_token(str(user.id), stage=LifeStage.SINGLE.value)
    refresh_token = create_refresh_token(str(user.id))

    logger.info(f"✅ New user created: {email} ({user.id})")
    return user, access_token, refresh_token


async def authenticate_user(db: AsyncSession, email: str, password: str) -> Optional[User]:
    user = await get_user_by_email(db, email)
    if not user or not user.password_hash:
        return None
    if not verify_password(password, user.password_hash):
        return None

    # Update last login
    user.last_login_at = datetime.now(timezone.utc).replace(tzinfo=None)
    await db.commit()
    return user


async def get_or_create_dev_user(db: AsyncSession) -> User:
    dev_email = "dev@loveguru.local"
    user = await get_user_by_email(db, dev_email)
    if user:
        return user
    user, _, _ = await create_user(db, dev_email, "Dev User")
    if user.profile:
        user.profile.onboarding_completed = True
        user.profile.current_stage = LifeStage.SINGLE
    await db.commit()
    await db.refresh(user)
    logger.info("Created dev user for AUTH_DISABLED mode")
    return user
