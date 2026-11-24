"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Pydantic Request & Response Schemas    ║
║         Full validation models for all 67+ endpoints         ║
╚══════════════════════════════════════════════════════════════╝
"""

from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List, Dict, Any
from datetime import datetime, timezone
import uuid


# ── Auth Schemas ─────────────────────────────────────────────

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)
    name: Optional[str] = "Friend"
    stage: Optional[str] = "single"


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    refresh_token: Optional[str] = None
    user: Optional[Dict[str, Any]] = None


class UserProfileResponse(BaseModel):
    id: str
    email: str
    display_name: Optional[str] = None
    current_stage: str = "single"
    gender: Optional[str] = None
    age: Optional[int] = None
    ai_personality: str = "warm_friend"
    attachment_style: Optional[str] = "unknown"
    love_languages: Optional[List[str]] = []
    created_at: Optional[datetime] = None


class ProfileUpdateRequest(BaseModel):
    display_name: Optional[str] = None
    current_stage: Optional[str] = None
    gender: Optional[str] = None
    age: Optional[int] = None
    location: Optional[str] = None
    ai_personality: Optional[str] = None
    attachment_style: Optional[str] = None
    bio: Optional[str] = None


# ── Chat Schemas ─────────────────────────────────────────────

class ChatMessageRequest(BaseModel):
    message: str
    conversation_id: Optional[str] = None
    mode: Optional[str] = "general"
    persona: Optional[str] = None


class ChatResponseSchema(BaseModel):
    response: str
    conversation_id: str
    message_id: str
    quick_replies: List[str] = []
    crisis_level: str = "safe"
    emotion_detected: Optional[str] = None
    stage_routed: Optional[str] = None
    suggested_actions: Optional[List[str]] = []


# ── Stage 1: Single & Searching ──────────────────────────────

class PartnerDescriptionRequest(BaseModel):
    description: str
    must_haves: Optional[List[str]] = []
    dealbreakers: Optional[List[str]] = []
    values: Optional[List[str]] = []


class RealityCheckRequest(BaseModel):
    traits_desired: List[str]
    gender_preference: Optional[str] = "any"
    age_range: Optional[List[int]] = [24, 32]
    income_expectation: Optional[str] = None
    education_level: Optional[str] = None
    location: Optional[str] = None


class ReadinessQuizRequest(BaseModel):
    emotional_independence: int = Field(ge=1, le=5)
    past_relationship_closure: int = Field(ge=1, le=5)
    financial_readiness: int = Field(ge=1, le=5)
    communication_openness: int = Field(ge=1, le=5)
    conflict_resilience: int = Field(ge=1, le=5)


# ── Stage 2: Finding Love ────────────────────────────────────

class DatingProfileAuditRequest(BaseModel):
    bio_text: str
    app_name: Optional[str] = "Hinge"
    photo_descriptions: Optional[List[str]] = []
    target_partner: Optional[str] = None


class MessageAdviceRequest(BaseModel):
    chat_history: str
    context: Optional[str] = None
    intent: Optional[str] = "keep_conversation_engaging"


class FlagCheckRequest(BaseModel):
    situation_text: str
    partner_behaviors: List[str]


# ── Stage 3: In a Relationship ───────────────────────────────

class GottmanAssessmentRequest(BaseModel):
    criticism_freq: int = Field(ge=1, le=5)
    contempt_freq: int = Field(ge=1, le=5)
    defensiveness_freq: int = Field(ge=1, le=5)
    stonewalling_freq: int = Field(ge=1, le=5)
    recent_conflict_topic: Optional[str] = None


class ConflictResolutionRequest(BaseModel):
    trigger_incident: str
    user_feelings: str
    desired_outcome: str


class LoveLanguageQuizRequest(BaseModel):
    answers: Dict[str, Any]


# ── Stage 4: Breakup Recovery ────────────────────────────────

class GriefWeatherLogRequest(BaseModel):
    weather: str = Field(description="storm, overcast, rain, clearing, sun")
    notes: Optional[str] = None
    intensity: int = Field(ge=1, le=10)


class NoContactLogRequest(BaseModel):
    day_count: int
    urge_felt: bool = False
    urge_trigger: Optional[str] = None


class ClosureLetterRequest(BaseModel):
    letter_text: str
    recipient_name: Optional[str] = "Ex-partner"
    send_intent: bool = False  # Should always be False (vault only)


# ── Progress & Daily Tracker ─────────────────────────────────

class MoodLogRequest(BaseModel):
    mood_score: int = Field(ge=1, le=10)
    primary_emotion: str
    tags: Optional[List[str]] = []
    journal_note: Optional[str] = None


class DailyCheckinRequest(BaseModel):
    gratitude: Optional[str] = None
    daily_intention: Optional[str] = None
    energy_level: int = Field(ge=1, le=5)
    relationship_feeling: Optional[str] = None


class TaskUpdateRequest(BaseModel):
    task_id: str
    status: str = Field(description="pending, completed, skipped")
