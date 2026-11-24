"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — LangGraph State Definition             ║
║   Complete TypedDict with all fields the 12-node graph uses  ║
╚══════════════════════════════════════════════════════════════╝
"""

from typing import TypedDict, Optional, List, Literal, Any, Dict
from datetime import datetime, timezone


class EmotionVector(TypedDict):
    """8-dimensional emotion representation."""
    sadness: float        # 0-1
    anxiety: float        # 0-1
    anger: float          # 0-1
    loneliness: float     # 0-1
    hope: float           # 0-1
    love: float           # 0-1
    confusion: float      # 0-1
    joy: float            # 0-1


class CrisisAssessment(TypedDict):
    level: Literal["safe", "moderate", "high", "critical"]
    confidence: float
    triggers: List[str]
    requires_helpline: bool
    requires_sos: bool


class RAGContext(TypedDict):
    retrieved: bool
    chunks: List[Dict[str, Any]]       # [{text, source, score, technique, metadata}]
    collection_used: str
    query_used: str


class AgentOutput(TypedDict):
    content: str
    structured_data: Optional[Dict[str, Any]]
    suggestions: Optional[List[str]]
    confidence: float


class GuruGraphState(TypedDict):
    """
    Master state object flowing through all 12 LangGraph nodes.
    Every node reads from and writes to this shared state.
    """

    # ── Core Input ───────────────────────────────────────────
    user_id: str
    conversation_id: str
    raw_message: str
    message_type: Literal["text", "voice", "image", "screenshot", "multimodal"]
    image_url: Optional[str]
    audio_url: Optional[str]
    session_messages: List[Dict[str, str]]   # [{role, content}] — last N turns

    # ── User Context (loaded from DB) ────────────────────────
    user_name: str
    current_stage: Literal["single", "finding", "relationship", "heartbreak"]
    ai_personality: Literal["warm_friend", "wise_mentor", "gentle_coach", "direct_advisor"]
    attachment_style: Optional[str]
    love_language: Optional[str]
    readiness_score: Optional[float]
    onboarding_completed: bool
    cultural_background: Optional[str]
    relationship_history_summary: Optional[str]

    # ── Node 1 — Input Preprocessor ──────────────────────────
    preprocessed_text: Optional[str]           # cleaned, transcribed if voice
    detected_language: Optional[str]
    input_length: Optional[int]

    # ── Node 2 — Context Builder ──────────────────────────────
    input_category: Optional[str]              # question/vent/request/crisis/journal
    chat_mode: Optional[str]                   # general/analysis/coaching/roleplay
    recent_patterns: Optional[List[str]]
    active_tasks: Optional[List[Dict]]

    # ── Node 3 — Stage Router ─────────────────────────────────
    routed_stage: Optional[str]                # which stage this message belongs to
    routing_confidence: Optional[float]
    routing_reason: Optional[str]

    # ── Node 4 — Emotion Detector ────────────────────────────
    emotion_vector: Optional[EmotionVector]
    primary_emotion: Optional[str]
    emotional_intensity: Optional[float]      # 0-1
    emotional_needs: Optional[List[str]]

    # ── Node 5 — Crisis Safety Gate ──────────────────────────
    crisis_assessment: Optional[CrisisAssessment]
    crisis_triggered: bool                    # routes to emergency handler

    # ── Node 6 — RAG Research ────────────────────────────────
    rag_context: Optional[RAGContext]

    # ── Node 7 — Multi-Modal Fusion ──────────────────────────
    image_analysis: Optional[Dict[str, Any]]  # Gemini Vision output
    audio_analysis: Optional[Dict[str, Any]]  # Whisper transcription + analysis

    # ── Node 8 — Stage Specialist ────────────────────────────
    specialist_output: Optional[AgentOutput]
    specialist_stage: Optional[str]

    # ── Node 9 — Personalizer ────────────────────────────────
    personalized_output: Optional[AgentOutput]
    tone_applied: Optional[str]
    cultural_adaptation: Optional[str]

    # ── Node 10 — Memory Updater ─────────────────────────────
    memory_updated: bool
    new_patterns_detected: Optional[List[str]]
    mood_logged: bool

    # ── Node 11 — Streak & Tasks ─────────────────────────────
    streaks_updated: bool
    new_task_generated: Optional[Dict]
    xp_awarded: Optional[int]

    # ── Node 12 — Output Validator ───────────────────────────
    final_response: Optional[str]
    quick_replies: Optional[List[str]]
    follow_up_actions: Optional[List[Dict]]
    safety_check_passed: bool

    # ── Metadata ─────────────────────────────────────────────
    processing_start_time: Optional[datetime]
    total_latency_ms: Optional[int]
    nodes_executed: List[str]
    error_state: Optional[str]
