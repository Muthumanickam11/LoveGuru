"""
╔══════════════════════════════════════════════════════════════╗
║        LOVEGURU AI — Complete Database Schema (18 Tables)    ║
║        SQLAlchemy 2.0 Async ORM Models                       ║
║        Built in strict foreign-key dependency order          ║
╚══════════════════════════════════════════════════════════════╝

Table order (foreign-key safe):
 1. users                    → auth credentials
 2. user_profiles            → display info, current stage
 3. user_psychology          → attachment, love languages
 4. partner_profiles         → partner context
 5. conversations            → session tracking
 6. messages                 → individual messages
 7. mood_logs               → daily mood entries
 8. stage1_data             → single-life data
 9. stage2_data             → finding-love data
10. stage3_data             → relationship data
11. stage4_data             → heartbreak recovery data
12. daily_checkins          → morning/evening logs
13. tasks_challenges        → micro-tasks
14. streaks                 → streak tracking
15. user_patterns           → AI-detected patterns
16. weekly_reports          → 7-day synthesis
17. crisis_logs             → high/critical events
18. journal_entries         → free-form reflections
"""

import uuid
from datetime import datetime, timezone
from typing import Optional, List
from sqlalchemy import (
    String, Text, Integer, Float, Boolean, DateTime,
    ForeignKey, JSON, Enum as SAEnum, Index,
    UniqueConstraint, CheckConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Uuid
from config.database import Base
import enum

# Universal cross-database aliases
PG_UUID = Uuid
JSONB = JSON



# ─────────────────────────────────────────────────────────────
# ENUMS
# ─────────────────────────────────────────────────────────────

class LifeStage(str, enum.Enum):
    SINGLE = "single"
    FINDING = "finding"
    RELATIONSHIP = "relationship"
    HEARTBREAK = "heartbreak"


class AttachmentStyle(str, enum.Enum):
    SECURE = "secure"
    ANXIOUS = "anxious"
    AVOIDANT = "avoidant"
    DISORGANIZED = "disorganized"
    UNKNOWN = "unknown"


class AIPersonality(str, enum.Enum):
    WARM_FRIEND = "warm_friend"
    WISE_MENTOR = "wise_mentor"
    GENTLE_COACH = "gentle_coach"
    DIRECT_ADVISOR = "direct_advisor"


class MessageRole(str, enum.Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


class MessageType(str, enum.Enum):
    TEXT = "text"
    VOICE = "voice"
    IMAGE = "image"
    SCREENSHOT = "screenshot"


class CrisisLevel(str, enum.Enum):
    SAFE = "safe"
    MODERATE = "moderate"
    HIGH = "high"
    CRITICAL = "critical"


class GriefWeather(str, enum.Enum):
    STORM = "storm"
    OVERCAST = "overcast"
    RAIN = "rain"
    CLEARING = "clearing"
    SUN = "sun"


class TaskStatus(str, enum.Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    SKIPPED = "skipped"


class StreakType(str, enum.Enum):
    APP_CHECKIN = "app_checkin"
    NO_CONTACT = "no_contact"
    DAILY_CHALLENGE = "daily_challenge"
    JOURNALING = "journaling"


class LoveLanguage(str, enum.Enum):
    WORDS_OF_AFFIRMATION = "words_of_affirmation"
    QUALITY_TIME = "quality_time"
    RECEIVING_GIFTS = "receiving_gifts"
    ACTS_OF_SERVICE = "acts_of_service"
    PHYSICAL_TOUCH = "physical_touch"


# ─────────────────────────────────────────────────────────────
# TABLE 1 — users
# ─────────────────────────────────────────────────────────────

class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    password_hash: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)  # Null for Google-only users
    google_id: Mapped[Optional[str]] = mapped_column(String(255), unique=True, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    last_login_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    # Relationships
    profile: Mapped["UserProfile"] = relationship(back_populates="user", uselist=False, cascade="all, delete-orphan", lazy="selectin")
    psychology: Mapped["UserPsychology"] = relationship(back_populates="user", uselist=False, cascade="all, delete-orphan", lazy="selectin")
    conversations: Mapped[List["Conversation"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    mood_logs: Mapped[List["MoodLog"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    journal_entries: Mapped[List["JournalEntry"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    streaks: Mapped[List["Streak"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    tasks: Mapped[List["TaskChallenge"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    patterns: Mapped[List["UserPattern"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    weekly_reports: Mapped[List["WeeklyReport"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    crisis_logs: Mapped[List["CrisisLog"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    daily_checkins: Mapped[List["DailyCheckin"]] = relationship(back_populates="user", cascade="all, delete-orphan")


# ─────────────────────────────────────────────────────────────
# TABLE 2 — user_profiles
# ─────────────────────────────────────────────────────────────

class UserProfile(Base):
    __tablename__ = "user_profiles"

    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    display_name: Mapped[str] = mapped_column(String(100), nullable=False)
    age: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    gender: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    city: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    current_stage: Mapped[LifeStage] = mapped_column(SAEnum(LifeStage), default=LifeStage.SINGLE, nullable=False)
    ai_personality: Mapped[AIPersonality] = mapped_column(SAEnum(AIPersonality), default=AIPersonality.WARM_FRIEND, nullable=False)
    onboarding_completed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    avatar_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    cultural_background: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    notification_preferences: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    user: Mapped["User"] = relationship(back_populates="profile")
    stage1_data: Mapped[Optional["Stage1Data"]] = relationship(back_populates="profile", uselist=False, cascade="all, delete-orphan")
    stage2_data: Mapped[Optional["Stage2Data"]] = relationship(back_populates="profile", uselist=False, cascade="all, delete-orphan")
    stage3_data: Mapped[Optional["Stage3Data"]] = relationship(back_populates="profile", uselist=False, cascade="all, delete-orphan")
    stage4_data: Mapped[Optional["Stage4Data"]] = relationship(back_populates="profile", uselist=False, cascade="all, delete-orphan")
    partner_profiles: Mapped[List["PartnerProfile"]] = relationship(back_populates="user_profile", cascade="all, delete-orphan")


# ─────────────────────────────────────────────────────────────
# TABLE 3 — user_psychology
# ─────────────────────────────────────────────────────────────

class UserPsychology(Base):
    __tablename__ = "user_psychology"

    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    attachment_style: Mapped[AttachmentStyle] = mapped_column(SAEnum(AttachmentStyle), default=AttachmentStyle.UNKNOWN, nullable=False)
    primary_love_language: Mapped[Optional[LoveLanguage]] = mapped_column(SAEnum(LoveLanguage), nullable=True)
    secondary_love_language: Mapped[Optional[LoveLanguage]] = mapped_column(SAEnum(LoveLanguage), nullable=True)
    readiness_score: Mapped[Optional[float]] = mapped_column(Float, nullable=True)  # 0-100
    emotional_triggers: Mapped[Optional[List[str]]] = mapped_column(JSONB, nullable=True)
    core_values: Mapped[Optional[List[str]]] = mapped_column(JSONB, nullable=True)
    communication_style: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)  # passive/assertive/aggressive
    relationship_history: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True)
    onboarding_summary: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    user: Mapped["User"] = relationship(back_populates="psychology")


# ─────────────────────────────────────────────────────────────
# TABLE 4 — partner_profiles
# ─────────────────────────────────────────────────────────────

class PartnerProfile(Base):
    __tablename__ = "partner_profiles"

    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    profile_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("user_profiles.id", ondelete="CASCADE"), nullable=False)
    partner_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    stage_context: Mapped[LifeStage] = mapped_column(SAEnum(LifeStage), nullable=False)
    relationship_type: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    relationship_start: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    guessed_love_language: Mapped[Optional[LoveLanguage]] = mapped_column(SAEnum(LoveLanguage), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # Relationships
    user_profile: Mapped["UserProfile"] = relationship(back_populates="partner_profiles")


# ─────────────────────────────────────────────────────────────
# TABLE 5 — conversations
# ─────────────────────────────────────────────────────────────

class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    title: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    stage_context: Mapped[Optional[LifeStage]] = mapped_column(SAEnum(LifeStage), nullable=True)
    chat_mode: Mapped[str] = mapped_column(String(50), default="general", nullable=False)
    max_crisis_level: Mapped[CrisisLevel] = mapped_column(SAEnum(CrisisLevel), default=CrisisLevel.SAFE, nullable=False)
    mood_delta: Mapped[Optional[float]] = mapped_column(Float, nullable=True)  # mood change in session
    message_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    last_message_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    # Relationships
    user: Mapped["User"] = relationship(back_populates="conversations")
    messages: Mapped[List["Message"]] = relationship(back_populates="conversation", cascade="all, delete-orphan", order_by="Message.created_at")


# ─────────────────────────────────────────────────────────────
# TABLE 6 — messages
# ─────────────────────────────────────────────────────────────

class Message(Base):
    __tablename__ = "messages"
    __table_args__ = (
        Index("ix_messages_conversation_id", "conversation_id"),
        Index("ix_messages_user_id", "user_id"),
    )

    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    conversation_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("conversations.id", ondelete="CASCADE"), nullable=False)
    user_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    role: Mapped[MessageRole] = mapped_column(SAEnum(MessageRole), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    message_type: Mapped[MessageType] = mapped_column(SAEnum(MessageType), default=MessageType.TEXT, nullable=False)
    emotion_tag: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    emotion_vector: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True)  # 8-dim emotion scores
    crisis_level: Mapped[CrisisLevel] = mapped_column(SAEnum(CrisisLevel), default=CrisisLevel.SAFE, nullable=False)
    rag_used: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    rag_sources: Mapped[Optional[List[str]]] = mapped_column(JSONB, nullable=True)
    image_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    audio_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    tokens_used: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    latency_ms: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # Relationships
    conversation: Mapped["Conversation"] = relationship(back_populates="messages")


# ─────────────────────────────────────────────────────────────
# TABLE 7 — mood_logs
# ─────────────────────────────────────────────────────────────

class MoodLog(Base):
    __tablename__ = "mood_logs"
    __table_args__ = (
        Index("ix_mood_logs_user_logged", "user_id", "logged_at"),
    )

    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    mood_score: Mapped[int] = mapped_column(Integer, nullable=False)   # 1–10
    pain_score: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)  # 1–10
    emoji: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    trigger_notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    context_stage: Mapped[Optional[LifeStage]] = mapped_column(SAEnum(LifeStage), nullable=True)
    logged_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # Relationships
    user: Mapped["User"] = relationship(back_populates="mood_logs")


# ─────────────────────────────────────────────────────────────
# TABLE 8 — stage1_data
# ─────────────────────────────────────────────────────────────

class Stage1Data(Base):
    __tablename__ = "stage1_data"

    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    profile_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("user_profiles.id", ondelete="CASCADE"), unique=True, nullable=False)
    partner_raw_description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    realism_score: Mapped[Optional[float]] = mapped_column(Float, nullable=True)       # 0-100
    healthy_expectations: Mapped[Optional[List[str]]] = mapped_column(JSONB, nullable=True)
    examine_expectations: Mapped[Optional[List[dict]]] = mapped_column(JSONB, nullable=True)
    reconsider_expectations: Mapped[Optional[List[dict]]] = mapped_column(JSONB, nullable=True)
    what_reveals: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    refined_vision: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    improvement_plan: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True)     # 6-area plan
    grooming_guide: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True)
    readiness_score: Mapped[Optional[float]] = mapped_column(Float, nullable=True)    # 0-100
    readiness_breakdown: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True) # per-dimension scores
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    profile: Mapped["UserProfile"] = relationship(back_populates="stage1_data")


# ─────────────────────────────────────────────────────────────
# TABLE 9 — stage2_data
# ─────────────────────────────────────────────────────────────

class Stage2Data(Base):
    __tablename__ = "stage2_data"

    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    profile_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("user_profiles.id", ondelete="CASCADE"), unique=True, nullable=False)
    profile_review_scores: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True)
    bio_rewrites: Mapped[Optional[List[str]]] = mapped_column(JSONB, nullable=True)
    photo_order: Mapped[Optional[List[int]]] = mapped_column(JSONB, nullable=True)
    conversation_analyses: Mapped[Optional[List[dict]]] = mapped_column(JSONB, nullable=True)
    red_flags_detected: Mapped[Optional[List[str]]] = mapped_column(JSONB, nullable=True)
    green_flags_detected: Mapped[Optional[List[str]]] = mapped_column(JSONB, nullable=True)
    date_prep_data: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True)
    date_debrief_data: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    profile: Mapped["UserProfile"] = relationship(back_populates="stage2_data")


# ─────────────────────────────────────────────────────────────
# TABLE 10 — stage3_data
# ─────────────────────────────────────────────────────────────

class Stage3Data(Base):
    __tablename__ = "stage3_data"

    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    profile_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("user_profiles.id", ondelete="CASCADE"), unique=True, nullable=False)
    weekly_health_scores: Mapped[Optional[List[dict]]] = mapped_column(JSONB, nullable=True)
    discussed_conflicts: Mapped[Optional[List[dict]]] = mapped_column(JSONB, nullable=True)
    gottman_scripts_used: Mapped[Optional[List[str]]] = mapped_column(JSONB, nullable=True)
    partner_love_language_guess: Mapped[Optional[LoveLanguage]] = mapped_column(SAEnum(LoveLanguage), nullable=True)
    relationship_health_current: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True) # 6-axis radar
    date_ideas_used: Mapped[Optional[List[str]]] = mapped_column(JSONB, nullable=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    profile: Mapped["UserProfile"] = relationship(back_populates="stage3_data")


# ─────────────────────────────────────────────────────────────
# TABLE 11 — stage4_data
# ─────────────────────────────────────────────────────────────

class Stage4Data(Base):
    __tablename__ = "stage4_data"

    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    profile_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("user_profiles.id", ondelete="CASCADE"), unique=True, nullable=False)
    breakup_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    relationship_duration_months: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    grief_weather: Mapped[Optional[GriefWeather]] = mapped_column(SAEnum(GriefWeather), nullable=True)
    no_contact_start: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    no_contact_streak_days: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    no_contact_longest_days: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    pain_scores: Mapped[Optional[List[dict]]] = mapped_column(JSONB, nullable=True)   # [{date, score}]
    sleep_scores: Mapped[Optional[List[dict]]] = mapped_column(JSONB, nullable=True)
    identity_items: Mapped[Optional[List[str]]] = mapped_column(JSONB, nullable=True) # reclaimed hobbies/interests
    lessons_extracted: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True)
    readiness_for_love: Mapped[Optional[float]] = mapped_column(Float, nullable=True) # 0-100
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    profile: Mapped["UserProfile"] = relationship(back_populates="stage4_data")


# ─────────────────────────────────────────────────────────────
# TABLE 12 — daily_checkins
# ─────────────────────────────────────────────────────────────

class DailyCheckin(Base):
    __tablename__ = "daily_checkins"
    __table_args__ = (
        Index("ix_checkins_user_date", "user_id", "checkin_date"),
    )

    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    checkin_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    checkin_type: Mapped[str] = mapped_column(String(20), default="morning", nullable=False)  # morning/evening
    sleep_hours: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    sleep_quality: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)   # 1-10
    appetite_score: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)  # 1-10
    movement_done: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    sunlight_done: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    emotional_note: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    ai_response: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # Relationships
    user: Mapped["User"] = relationship(back_populates="daily_checkins")


# ─────────────────────────────────────────────────────────────
# TABLE 13 — tasks_challenges
# ─────────────────────────────────────────────────────────────

class TaskChallenge(Base):
    __tablename__ = "tasks_challenges"

    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    difficulty: Mapped[int] = mapped_column(Integer, default=1, nullable=False)  # 1-5
    stage_context: Mapped[Optional[LifeStage]] = mapped_column(SAEnum(LifeStage), nullable=True)
    task_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    status: Mapped[TaskStatus] = mapped_column(SAEnum(TaskStatus), default=TaskStatus.PENDING, nullable=False)
    completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    xp_reward: Mapped[int] = mapped_column(Integer, default=10, nullable=False)

    # Relationships
    user: Mapped["User"] = relationship(back_populates="tasks")


# ─────────────────────────────────────────────────────────────
# TABLE 14 — streaks
# ─────────────────────────────────────────────────────────────

class Streak(Base):
    __tablename__ = "streaks"
    __table_args__ = (
        UniqueConstraint("user_id", "streak_type", name="uq_user_streak_type"),
    )

    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    streak_type: Mapped[StreakType] = mapped_column(SAEnum(StreakType), nullable=False)
    current_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    longest_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    last_activity_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    started_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    user: Mapped["User"] = relationship(back_populates="streaks")


# ─────────────────────────────────────────────────────────────
# TABLE 15 — user_patterns
# ─────────────────────────────────────────────────────────────

class UserPattern(Base):
    __tablename__ = "user_patterns"
    __table_args__ = (
        Index("ix_patterns_user_id", "user_id"),
    )

    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    pattern_type: Mapped[str] = mapped_column(String(100), nullable=False)  # cognitive/dating/emotional
    pattern_name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    evidence_snippets: Mapped[Optional[List[str]]] = mapped_column(JSONB, nullable=True)
    evidence_count: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    confidence: Mapped[float] = mapped_column(Float, default=0.5, nullable=False)  # 0-1
    is_confirmed: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)  # null=pending
    detected_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    user: Mapped["User"] = relationship(back_populates="patterns")


# ─────────────────────────────────────────────────────────────
# TABLE 16 — weekly_reports
# ─────────────────────────────────────────────────────────────

class WeeklyReport(Base):
    __tablename__ = "weekly_reports"

    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    week_start: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    week_end: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    mood_summary: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True)         # avg, trend, lowest, highest
    conflict_summary: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True)
    growth_summary: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    top_insights: Mapped[Optional[List[str]]] = mapped_column(JSONB, nullable=True)
    recommendations: Mapped[Optional[List[str]]] = mapped_column(JSONB, nullable=True)
    stage_at_report: Mapped[Optional[LifeStage]] = mapped_column(SAEnum(LifeStage), nullable=True)
    ai_narrative: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    generated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # Relationships
    user: Mapped["User"] = relationship(back_populates="weekly_reports")


# ─────────────────────────────────────────────────────────────
# TABLE 17 — crisis_logs
# ─────────────────────────────────────────────────────────────

class CrisisLog(Base):
    __tablename__ = "crisis_logs"

    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    crisis_level: Mapped[CrisisLevel] = mapped_column(SAEnum(CrisisLevel), nullable=False)
    trigger_message: Mapped[Optional[str]] = mapped_column(Text, nullable=True)       # anonymized trigger
    response_type: Mapped[str] = mapped_column(String(50), nullable=False)            # grounding/helpline/sos
    helplines_shown: Mapped[Optional[List[str]]] = mapped_column(JSONB, nullable=True)
    conversation_id: Mapped[Optional[uuid.UUID]] = mapped_column(PG_UUID(as_uuid=True), nullable=True)
    resolved: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    logged_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # Relationships
    user: Mapped["User"] = relationship(back_populates="crisis_logs")


# ─────────────────────────────────────────────────────────────
# TABLE 18 — journal_entries
# ─────────────────────────────────────────────────────────────

class JournalEntry(Base):
    __tablename__ = "journal_entries"

    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    entry_type: Mapped[str] = mapped_column(String(30), default="free", nullable=False)  # free/prompted/unsent_letter
    prompt_used: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    sentiment_score: Mapped[Optional[float]] = mapped_column(Float, nullable=True)  # -1 to 1
    dominant_emotion: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    ai_reflection: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    stage_context: Mapped[Optional[LifeStage]] = mapped_column(SAEnum(LifeStage), nullable=True)
    is_private: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    word_count: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # Relationships
    user: Mapped["User"] = relationship(back_populates="journal_entries")
