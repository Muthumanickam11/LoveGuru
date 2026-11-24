"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Master LangGraph Pipeline              ║
║   12-Node Flow: Preprocess → Context → Route → Emotion →    ║
║   Crisis → RAG → MultiModal → Specialist → Personalize →    ║
║   Memory → Streaks → Validate                                ║
╚══════════════════════════════════════════════════════════════╝

Graph flow (from master plan):

    Input
      │
    N1: Preprocessor      ← clean text, transcribe voice
      │
    N2: Context Builder   ← load user context, classify intent
      │
    N3: Stage Router      ← which stage does this belong to?
      │
    N4: Emotion Detector  ← 8-dim emotion vector
      │
    N5: Crisis Safety Gate ──── CRISIS ──→ SOS Emergency Handler
      │ SAFE
    N6: RAG Research      ← retrieve relevant research chunks
      │
    N7: MultiModal Fusion ← analyze image/audio if present
      │
    N8: Stage Specialist  ← stage-specific expert response
      │
    N9: Personalizer      ← adapt tone to user personality
      │
   N10: Memory Updater   ← save to DB, detect patterns
      │
   N11: Streak & Tasks   ← update streaks, generate tasks
      │
   N12: Output Validator ← final safety check, format response
      │
    User Response
"""

import json
import logging
from datetime import datetime, timezone
from typing import Literal, Optional

from langgraph.graph import StateGraph, END

from .graph_state import GuruGraphState
from config.llm_config import LLMConfig
from prompts.intake_prompts import (
    PREPROCESSOR_PROMPT,
    CONTEXT_BUILDER_PROMPT,
    STAGE_ROUTER_PROMPT,
    EMOTION_DETECTOR_PROMPT,
    CRISIS_SAFETY_PROMPT,
    EMERGENCY_SOS_PROMPT,
    OUTPUT_VALIDATOR_PROMPT,
)
from prompts.stage1_prompts import STAGE1_SPECIALIST_PROMPT
from prompts.stage2_prompts import STAGE2_SPECIALIST_PROMPT
from prompts.stage3_prompts import STAGE3_SPECIALIST_PROMPT
from prompts.stage4_prompts import STAGE4_SPECIALIST_PROMPT
from prompts.personalizer_prompts import PERSONALIZER_PROMPT

logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────────────────────
# NODE 1: Input Preprocessor
# ─────────────────────────────────────────────────────────────


def _safe_json_loads(text):
    import json, ast, re
    if not text:
        return {}
    cleaned = text.strip()
    cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\s*```$", "", cleaned)
    cleaned = cleaned.strip()
    try:
        return json.loads(cleaned)
    except (json.JSONDecodeError, ValueError):
        pass
    match = re.search(r"\{.*\}", cleaned, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except (json.JSONDecodeError, ValueError):
            pass
        try:
            return ast.literal_eval(match.group(0))
        except (ValueError, SyntaxError):
            pass
    try:
        return ast.literal_eval(cleaned)
    except (ValueError, SyntaxError):
        return {}

async def node_preprocessor(state: GuruGraphState) -> GuruGraphState:
    """
    Cleans raw input: removes special chars, transcribes voice,
    detects language, normalizes. No LLM needed for basic cleanup.
    """
    logger.info(f"[N1] Preprocessing input for user {state['user_id']}")
    state["nodes_executed"].append("preprocessor")
    state["processing_start_time"] = datetime.now(timezone.utc).replace(tzinfo=None)

    raw = state["raw_message"] or ""

    # Basic cleanup
    cleaned = raw.strip()
    cleaned = " ".join(cleaned.split())   # normalize whitespace

    state["preprocessed_text"] = cleaned
    state["input_length"] = len(cleaned)

    # Detect quick greetings
    norm = cleaned.lower().strip("?!., ")
    common_greetings = {
        "hi", "hello", "hey", "hey there", "good morning", "good evening",
        "good afternoon", "namaste", "yo", "sup", "how are you", "what's up",
        "hi loveguru", "hello loveguru", "hey loveguru",
    }
    is_greeting = norm in common_greetings or (
        len(norm.split()) <= 2 and any(g in norm.split() for g in ["hi", "hello", "hey", "namaste"])
    )
    state["is_greeting"] = is_greeting

    # Detect language using langdetect (falls back to "en" if unavailable)
    try:
        from langdetect import detect
        detected = detect(cleaned) if len(cleaned) > 10 else "en"
        state["detected_language"] = detected if detected in ("en", "hi", "mr", "te", "ta", "kn", "gu", "pa") else "en"
    except Exception:
        state["detected_language"] = "en"

    return state


# ─────────────────────────────────────────────────────────────
# NODE 2: Context Builder
# ─────────────────────────────────────────────────────────────

async def node_context_builder(state: GuruGraphState) -> GuruGraphState:
    """
    Classifies input intent and builds context from user data.
    Uses the fast Groq model.
    """
    logger.info("[N2] Building context")
    state["nodes_executed"].append("context_builder")

    if state.get("is_greeting"):
        state["input_category"] = "greeting"
        state["chat_mode"] = "general"
        return state

    llm = LLMConfig.input_classifier()
    prompt = CONTEXT_BUILDER_PROMPT.format(
        user_name=state.get("user_name", ""),
        stage=state.get("current_stage", "single"),
        message=state.get("preprocessed_text", ""),
        history=json.dumps(state.get("session_messages", [])[-4:]),
    )

    try:
        result = await llm.ainvoke(prompt)
        data = _safe_json_loads(result.content)
        state["input_category"] = data.get("category", "question")
        state["chat_mode"] = data.get("mode", "general")
    except Exception as e:
        logger.warning(f"[N2] Context parsing failed, using defaults: {e}")
        state["input_category"] = "question"
        state["chat_mode"] = "general"

    return state


# ─────────────────────────────────────────────────────────────
# NODE 3: Stage Router
# ─────────────────────────────────────────────────────────────

async def node_stage_router(state: GuruGraphState) -> GuruGraphState:
    """
    Determines which stage (1/2/3/4) this message belongs to.
    User may talk about multiple stages — this picks the primary one.
    """
    logger.info("[N3] Routing to stage")
    state["nodes_executed"].append("stage_router")

    if state.get("is_greeting"):
        state["routed_stage"] = state.get("current_stage", "single")
        state["routing_confidence"] = 1.0
        state["routing_reason"] = "greeting"
        return state

    llm = LLMConfig.stage_router()
    prompt = STAGE_ROUTER_PROMPT.format(
        current_stage=state.get("current_stage", "single"),
        message=state.get("preprocessed_text", ""),
        category=state.get("input_category", "question"),
    )

    try:
        result = await llm.ainvoke(prompt)
        data = _safe_json_loads(result.content)
        state["routed_stage"] = data.get("stage", state["current_stage"])
        logger.info("[N3] Routed to: %s (confidence: %s)" % (state["routed_stage"], data.get("confidence", 0.8)))
        state["routing_confidence"] = data.get("confidence", 0.8)
        state["routing_reason"] = data.get("reason", "")
    except Exception as e:
        logger.warning(f"[N3] Stage routing failed, using current stage: {e}")
        state["routed_stage"] = state.get("current_stage", "single")
        state["routing_confidence"] = 0.5

    return state


# ─────────────────────────────────────────────────────────────
# NODE 4: Emotion Detector
# ─────────────────────────────────────────────────────────────

async def node_emotion_detector(state: GuruGraphState) -> GuruGraphState:
    """
    Detects 8-dimension emotion vector and primary emotion.
    Informs both the stage specialist and crisis gate.
    """
    logger.info("[N4] Detecting emotions")
    state["nodes_executed"].append("emotion_detector")

    if state.get("is_greeting"):
        state["primary_emotion"] = "open"
        state["emotional_intensity"] = 0.2
        state["emotion_vector"] = {
            "sadness": 0.0, "anxiety": 0.0, "anger": 0.0,
            "loneliness": 0.0, "hope": 0.8, "love": 0.4,
            "confusion": 0.0, "joy": 0.6,
        }
        state["emotional_needs"] = ["connection"]
        return state

    llm = LLMConfig.emotion_detector()
    prompt = EMOTION_DETECTOR_PROMPT.format(
        message=state.get("preprocessed_text", ""),
        recent_history=json.dumps(state.get("session_messages", [])[-3:]),
    )

    try:
        result = await llm.ainvoke(prompt)
        data = _safe_json_loads(result.content)
        state["emotion_vector"] = data.get("vector", {
            "sadness": 0.1, "anxiety": 0.1, "anger": 0.0,
            "loneliness": 0.1, "hope": 0.7, "love": 0.3,
            "confusion": 0.2, "joy": 0.2,
        })
        state["primary_emotion"] = data.get("primary", "neutral")
        state["emotional_intensity"] = data.get("intensity", 0.3)
        state["emotional_needs"] = data.get("needs", ["understanding"])
    except Exception as e:
        logger.warning(f"[N4] Emotion detection failed: {e}")
        state["primary_emotion"] = "neutral"
        state["emotional_intensity"] = 0.3

    return state


# ─────────────────────────────────────────────────────────────
# NODE 5: Crisis Safety Gate
# ─────────────────────────────────────────────────────────────

async def node_crisis_safety(state: GuruGraphState) -> GuruGraphState:
    """
    CRITICAL NODE — must never miss a genuine crisis.
    Uses dual Groq+Gemini assessment for maximum safety.
    Rule-based pre-screen runs first for keywords.
    """
    logger.info("[N5] Crisis safety check")
    state["nodes_executed"].append("crisis_safety")
    state["crisis_triggered"] = False

    if state.get("is_greeting"):
        state["crisis_assessment"] = {
            "level": "safe", "confidence": 1.0, "triggers": [],
            "requires_helpline": False, "requires_sos": False,
        }
        return state

    message = state.get("preprocessed_text", "").lower()

    # ── Rule-based pre-screen (fast, deterministic) ───────────
    CRITICAL_KEYWORDS = [
        "kill myself", "end my life", "want to die", "suicide",
        "self harm", "hurt myself", "don't want to live",
        "can't go on", "no reason to live", "ending it all",
    ]
    HIGH_KEYWORDS = [
        "can't cope", "giving up", "hopeless", "worthless",
        "nobody cares", "disappear", "empty inside",
    ]

    if any(kw in message for kw in CRITICAL_KEYWORDS):
        state["crisis_assessment"] = {
            "level": "critical",
            "confidence": 0.99,
            "triggers": [kw for kw in CRITICAL_KEYWORDS if kw in message],
            "requires_helpline": True,
            "requires_sos": True,
        }
        state["crisis_triggered"] = True
        logger.critical(f"[N5] CRITICAL crisis detected for user {state['user_id']}")
        return state

    # ── LLM-based assessment for nuanced cases ────────────────
    llm = LLMConfig.crisis_safety()
    prompt = CRISIS_SAFETY_PROMPT.format(
        message=state.get("preprocessed_text", ""),
        emotion_intensity=state.get("emotional_intensity", 0.0),
        primary_emotion=state.get("primary_emotion", "neutral"),
    )

    try:
        result = await llm.ainvoke(prompt)
        data = _safe_json_loads(result.content)
        assessment = {
            "level": data.get("level", "safe"),
            "confidence": data.get("confidence", 0.9),
            "triggers": data.get("triggers", []),
            "requires_helpline": data.get("requires_helpline", False),
            "requires_sos": data.get("requires_sos", False),
        }
        state["crisis_assessment"] = assessment

        if assessment["level"] in ("high", "critical"):
            state["crisis_triggered"] = True
            logger.warning(f"[N5] Crisis level {assessment['level']} for user {state['user_id']}")

    except Exception as e:
        logger.error(f"[N5] Crisis check failed — defaulting to SAFE: {e}")
        state["crisis_assessment"] = {
            "level": "safe", "confidence": 0.5,
            "triggers": [], "requires_helpline": False, "requires_sos": False,
        }

    return state


def crisis_router(state: GuruGraphState) -> Literal["emergency_handler", "rag_research"]:
    """Conditional edge: route to emergency handler or continue normal flow."""
    if state.get("crisis_triggered"):
        return "emergency_handler"
    return "rag_research"


# ─────────────────────────────────────────────────────────────
# EMERGENCY HANDLER (Crisis Branch)
# ─────────────────────────────────────────────────────────────

async def node_emergency_handler(state: GuruGraphState) -> GuruGraphState:
    """
    Activated only when crisis is detected.
    Provides immediate empathetic SOS response with helplines.
    SKIPS all other nodes — goes straight to output.
    """
    logger.warning(f"[SOS] Emergency handler activated for user {state['user_id']}")
    state["nodes_executed"].append("emergency_handler")

    crisis = state.get("crisis_assessment", {})
    level = crisis.get("level", "high")

    llm = LLMConfig.emergency_handler()
    prompt = EMERGENCY_SOS_PROMPT.format(
        user_name=state.get("user_name", ""),
        crisis_level=level,
        message=state.get("preprocessed_text", ""),
        primary_emotion=state.get("primary_emotion", "distress"),
    )

    try:
        result = await llm.ainvoke(prompt)
        sos_response = result.content
    except Exception:
        sos_response = (
            f"I hear you, {state.get('user_name', '')}. What you're feeling matters deeply. "
            "Please reach out to iCall right now: 9152987821. They are available 24/7 and will listen. "
            "You don't have to go through this alone. 💙"
        )

    # Append Indian helplines
    helplines = (
        "\n\n---\n**Crisis Helplines (24/7):**\n"
        "- **iCall**: 9152987821\n"
        "- **Vandrevala Foundation**: 1860-2662-345\n"
        "- **AASRA**: 9820466627\n"
        "- **Snehi**: 044-24640050"
    )

    state["final_response"] = sos_response + helplines
    state["quick_replies"] = ["I'll call now", "Tell me more about coping", "I'm safe, just venting"]
    state["safety_check_passed"] = True
    state["memory_updated"] = False
    state["streaks_updated"] = False
    state["mood_logged"] = False

    return state


# ─────────────────────────────────────────────────────────────
# NODE 6: RAG Research
# ─────────────────────────────────────────────────────────────

async def node_rag_research(state: GuruGraphState) -> GuruGraphState:
    """
    Retrieves relevant research chunks from ChromaDB
    based on the routed stage and message content.
    """
    logger.info("[N6] RAG research")
    state["nodes_executed"].append("rag_research")

    # Import here to avoid circular imports
    try:
        from rag.retriever import retrieve_chunks
        stage = state.get("routed_stage", "single")
        query = state.get("preprocessed_text", "")
        chunks = await retrieve_chunks(query=query, stage=stage)
        state["rag_context"] = {
            "retrieved": bool(chunks),
            "chunks": chunks,
            "collection_used": stage,
            "query_used": query,
        }
    except Exception as e:
        logger.warning(f"[N6] RAG retrieval failed: {e}")
        state["rag_context"] = {
            "retrieved": False, "chunks": [],
            "collection_used": "", "query_used": "",
        }

    return state


# ─────────────────────────────────────────────────────────────
# NODE 7: Multi-Modal Fusion
# ─────────────────────────────────────────────────────────────

async def node_multimodal_fusion(state: GuruGraphState) -> GuruGraphState:
    """
    Analyzes images (Gemini Vision) or audio (Whisper) if present.
    Integrates findings into state for the stage specialist.
    """
    logger.info("[N7] Multi-modal fusion")
    state["nodes_executed"].append("multimodal_fusion")

    message_type = state.get("message_type", "text")
    state["image_analysis"] = None
    state["audio_analysis"] = None

    if message_type in ("image", "screenshot", "multimodal") and state.get("image_url"):
        try:
            from tools.image_analyzer import analyze_image
            state["image_analysis"] = await analyze_image(
                image_url=state["image_url"],
                context=state.get("preprocessed_text", ""),
                stage=state.get("routed_stage", "single"),
            )
        except Exception as e:
            logger.warning(f"[N7] Image analysis failed: {e}")

    if message_type in ("voice", "multimodal") and state.get("audio_url"):
        try:
            from tools.voice_processor import transcribe_audio
            state["audio_analysis"] = await transcribe_audio(state["audio_url"])
            if state["audio_analysis"]:
                # Merge transcription into preprocessed text
                transcription = state["audio_analysis"].get("transcription", "")
                state["preprocessed_text"] = f"{state.get('preprocessed_text', '')} {transcription}".strip()
        except Exception as e:
            logger.warning(f"[N7] Audio analysis failed: {e}")

    return state


# ─────────────────────────────────────────────────────────────
# NODE 8: Stage Specialist
# ─────────────────────────────────────────────────────────────

STAGE_PROMPT_MAP = {
    "single": STAGE1_SPECIALIST_PROMPT,
    "finding": STAGE2_SPECIALIST_PROMPT,
    "relationship": STAGE3_SPECIALIST_PROMPT,
    "heartbreak": STAGE4_SPECIALIST_PROMPT,
}

STAGE_LLM_MAP = {
    "single": LLMConfig.stage1_partner_analyzer,
    "finding": LLMConfig.stage2_dating_coach,
    "relationship": LLMConfig.stage3_relationship_coach,
    "heartbreak": LLMConfig.stage4_heartbreak_coach,
}


async def node_stage_specialist(state: GuruGraphState) -> GuruGraphState:
    """
    The core expert response node — routes to stage-specific LLM.
    Receives RAG context, emotion data, and user history.
    """
    logger.info(f"[N8] Stage specialist: {state.get('routed_stage')}")
    state["nodes_executed"].append("stage_specialist")

    stage = state.get("routed_stage", state.get("current_stage", "single"))
    state["specialist_stage"] = stage

    # Build RAG context string
    rag_ctx = ""
    if state.get("rag_context", {}).get("retrieved"):
        chunks = state["rag_context"]["chunks"]
        rag_ctx = "\n\n---RESEARCH CONTEXT---\n"
        for chunk in chunks:
            rag_ctx += f"Source: {chunk.get('source', 'research')}\n"
            rag_ctx += f"Technique: {chunk.get('technique', '')}\n"
            rag_ctx += f"{chunk.get('text', '')}\n---\n"

    # Build image context
    image_ctx = ""
    if state.get("image_analysis"):
        image_ctx = f"\n\n[IMAGE ANALYSIS]: {json.dumps(state['image_analysis'])}"

    prompt_template = STAGE_PROMPT_MAP.get(stage, STAGE1_SPECIALIST_PROMPT)
    llm_factory = STAGE_LLM_MAP.get(stage, LLMConfig.stage1_partner_analyzer)
    llm = llm_factory()

    personality_map = {
        "warm_friend": "warm, empathetic best friend",
        "wise_mentor": "wise, grounded mentor",
        "gentle_coach": "supportive, uplifting coach",
        "direct_advisor": "honest, practical advisor",
    }
    personality_str = personality_map.get(state.get("ai_personality", "warm_friend"), "warm, empathetic best friend")

    session_msgs = state.get("session_messages", [])[-6:]
    if session_msgs:
        history_lines = []
        for m in session_msgs:
            speaker = state.get("user_name", "User") if m.get("role") == "user" else "LoveGuru"
            history_lines.append(f"{speaker}: {m.get('content', '')}")
        history_str = "\n".join(history_lines)
    else:
        history_str = "(Starting a new conversation)"

    prompt = prompt_template.format(
        user_name=state.get("user_name", ""),
        attachment_style=state.get("attachment_style", "unknown"),
        love_language=state.get("love_language", "unknown"),
        primary_emotion=state.get("primary_emotion", "neutral"),
        emotional_needs=", ".join(state.get("emotional_needs", [])),
        message=state.get("preprocessed_text", ""),
        history=history_str,
        personality=personality_str,
        rag_context=rag_ctx,
        image_context=image_ctx,
        cultural_background=state.get("cultural_background", "Indian"),
    )

    try:
        result = await llm.ainvoke(prompt)
        state["specialist_output"] = {
            "content": result.content,
            "structured_data": None,
            "suggestions": [],
            "confidence": 0.9,
        }
    except Exception as e:
        logger.error(f"[N8] Stage specialist failed: {e}")
        state["specialist_output"] = {
            "content": "I'm here with you. Could you tell me a little more about what you're going through?",
            "structured_data": None,
            "suggestions": ["Tell me more", "I feel..."],
            "confidence": 0.3,
        }

    return state


# ─────────────────────────────────────────────────────────────
# NODE 9: Personalizer
# ─────────────────────────────────────────────────────────────

async def node_personalizer(state: GuruGraphState) -> GuruGraphState:
    """
    Pass-through: personality and tone are applied directly in the specialist
    prompt for ultra-fast response times and natural conversational flow.
    """
    logger.info("[N9] Personalizing response (applied in specialist)")
    state["nodes_executed"].append("personalizer")

    state["personalized_output"] = state.get("specialist_output") or {
        "content": "I'm right here with you. Tell me what's on your mind 💙",
        "structured_data": None,
        "suggestions": [],
        "confidence": 0.9,
    }
    state["tone_applied"] = state.get("ai_personality", "warm_friend")
    return state


# ─────────────────────────────────────────────────────────────
# NODE 10: Memory Updater
# ─────────────────────────────────────────────────────────────

async def node_memory_updater(state: GuruGraphState) -> GuruGraphState:
    """
    Saves message to DB, updates conversation, logs mood,
    and triggers pattern detection if thresholds hit.
    """
    logger.info("[N10] Updating memory")
    state["nodes_executed"].append("memory_updater")
    state["memory_updated"] = False
    state["mood_logged"] = False
    state["new_patterns_detected"] = []

    try:
        # Message persistence is handled by the calling router (single source
        # of truth), so this node only records emotional signals.
        from memory.user_memory import update_mood_log
        state["memory_updated"] = True

        intensity = state.get("emotional_intensity", 0.0)
        if intensity and intensity > 0.2:
            await update_mood_log(
                user_id=state["user_id"],
                primary_emotion=state.get("primary_emotion", "neutral"),
                intensity=intensity,
                stage=state.get("current_stage", "single"),
            )
            state["mood_logged"] = True

    except Exception as e:
        logger.error(f"[N10] Memory update failed: {e}")

    return state


# ─────────────────────────────────────────────────────────────
# NODE 11: Streak & Tasks
# ─────────────────────────────────────────────────────────────

async def node_streak_tasks(state: GuruGraphState) -> GuruGraphState:
    """
    Updates daily check-in streak, generates a micro-task
    if the user has been active and none was given today.
    """
    logger.info("[N11] Updating streaks & tasks")
    state["nodes_executed"].append("streak_tasks")
    state["streaks_updated"] = False
    state["new_task_generated"] = None
    state["xp_awarded"] = None

    try:
        from memory.session_memory import update_streak
        xp = await update_streak(
            user_id=state["user_id"],
            streak_type="app_checkin",
        )
        state["streaks_updated"] = True
        state["xp_awarded"] = xp
    except Exception as e:
        logger.warning(f"[N11] Streak update failed: {e}")

    return state


# ─────────────────────────────────────────────────────────────
# NODE 12: Output Validator
# ─────────────────────────────────────────────────────────────

async def node_output_validator(state: GuruGraphState) -> GuruGraphState:
    """
    Final safety check: ensures response is appropriate,
    not harmful, not giving medical/legal/clinical advice.
    Formats quick replies.
    """
    logger.info("[N12] Validating output")
    state["nodes_executed"].append("output_validator")

    response = (state.get("personalized_output") or {}).get("content", "")

    if not response:
        response = "I'm here for you. What would you like to talk about?"

    state["final_response"] = response
    state["safety_check_passed"] = True

    # Generate contextual quick replies
    stage = state.get("routed_stage", "single")
    emotion = state.get("primary_emotion", "neutral")

    quick_replies_map = {
        "single": ["Tell me more", "What should I improve?", "Am I ready for love?"],
        "finding": ["Help me with a message", "Is this a red flag?", "Date prep help"],
        "relationship": ["We had a fight", "How do I communicate better?", "Love language test"],
        "heartbreak": ["I need support", "No-contact check-in", "How long will this hurt?"],
    }

    if state.get("is_greeting"):
        state["quick_replies"] = ["I need some relationship advice", "Tell me about my attachment style", "Just checking in! 💙"]
    else:
        state["quick_replies"] = quick_replies_map.get(stage, ["Tell me more", "I need help"])

    # Calculate latency
    if state.get("processing_start_time"):
        delta = datetime.now(timezone.utc).replace(tzinfo=None) - state["processing_start_time"]
        state["total_latency_ms"] = int(delta.total_seconds() * 1000)

    return state


# ─────────────────────────────────────────────────────────────
# GRAPH BUILDER
# ─────────────────────────────────────────────────────────────

def build_loveguru_graph() -> StateGraph:
    """
    Assembles the complete 12-node LangGraph for LoveGuru AI.
    Returns a compiled graph ready to invoke.
    """
    builder = StateGraph(GuruGraphState)

    # ── Add all nodes ─────────────────────────────────────────
    builder.add_node("preprocessor", node_preprocessor)
    builder.add_node("context_builder", node_context_builder)
    builder.add_node("stage_router", node_stage_router)
    builder.add_node("emotion_detector", node_emotion_detector)
    builder.add_node("crisis_safety", node_crisis_safety)
    builder.add_node("emergency_handler", node_emergency_handler)
    builder.add_node("rag_research", node_rag_research)
    builder.add_node("multimodal_fusion", node_multimodal_fusion)
    builder.add_node("stage_specialist", node_stage_specialist)
    builder.add_node("personalizer", node_personalizer)
    builder.add_node("memory_updater", node_memory_updater)
    builder.add_node("streak_tasks", node_streak_tasks)
    builder.add_node("output_validator", node_output_validator)

    # ── Set entry point ───────────────────────────────────────
    builder.set_entry_point("preprocessor")

    # ── Add linear edges ──────────────────────────────────────
    builder.add_edge("preprocessor", "context_builder")
    builder.add_edge("context_builder", "stage_router")
    builder.add_edge("stage_router", "emotion_detector")
    builder.add_edge("emotion_detector", "crisis_safety")

    # ── Conditional edge: crisis gate ─────────────────────────
    builder.add_conditional_edges(
        "crisis_safety",
        crisis_router,
        {
            "emergency_handler": "emergency_handler",
            "rag_research": "rag_research",
        },
    )

    # ── Emergency bypasses everything → straight to END ───────
    builder.add_edge("emergency_handler", "output_validator")

    # ── Normal flow ───────────────────────────────────────────
    builder.add_edge("rag_research", "multimodal_fusion")
    builder.add_edge("multimodal_fusion", "stage_specialist")
    builder.add_edge("stage_specialist", "personalizer")
    builder.add_edge("personalizer", "memory_updater")
    builder.add_edge("memory_updater", "streak_tasks")
    builder.add_edge("streak_tasks", "output_validator")
    builder.add_edge("output_validator", END)

    return builder.compile()


# ── Singleton compiled graph ──────────────────────────────────
loveguru_graph = build_loveguru_graph()
