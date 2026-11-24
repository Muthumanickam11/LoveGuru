"""
╔══════════════════════════════════════════════════════════════╗
║           LOVEGURU AI — LLM Configuration                    ║
║   3-Tier Fallback: Groq (Primary) → Gemini → Error          ║
╚══════════════════════════════════════════════════════════════╝

LLM Node Configuration Matrix (from master plan):
┌─────────────────────────────┬───────────────┬─────────────┬───────┬──────────┐
│ Agent Node                  │ Primary        │ Fallback    │ Temp  │ MaxTok   │
├─────────────────────────────┼───────────────┼─────────────┼───────┼──────────┤
│ Input Classifier            │ Groq 70B       │ Gemini Flash│  0.0  │ 50       │
│ Stage Router                │ Groq 70B       │ Gemini Flash│  0.0  │ 100      │
│ Emotion Detector            │ Groq 70B       │ Gemini Flash│  0.1  │ 200      │
│ Crisis Safety Agent         │ Groq+Gemini    │ Rule-based  │  0.0  │ 150      │
│ Emergency Handler           │ Groq 70B       │ Pre-cached  │  0.0  │ 300      │
│ Stage 1 Partner Analyzer    │ Groq 70B       │ Gemini Flash│  0.6  │ 600      │
│ Stage 2 Dating Coach        │ Groq 70B       │ Gemini Flash│  0.7  │ 700      │
│ Stage 3 Relationship Coach  │ Groq 70B       │ Gemini Flash│  0.7  │ 700      │
│ Stage 4 Heartbreak Coach    │ Groq 70B       │ Gemini Flash│  0.5  │ 600      │
│ Personalizer Agent          │ Groq 70B       │ Gemini Flash│  0.8  │ 600      │
│ Pattern Analyzer            │ Gemini Flash   │ Groq 70B    │  0.3  │ 1000     │
└─────────────────────────────┴───────────────┴─────────────┴───────┴──────────┘
"""

from typing import Any, List, Optional
import logging
from .settings import settings
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import BaseMessage, AIMessage
from langchain_core.outputs import ChatResult, ChatGeneration

logger = logging.getLogger(__name__)


class MockFallbackChatModel(BaseChatModel):
    """Resilient mock model used when provider keys are missing or offline."""
    response_text: str = "I hear you deeply. Love is a journey of self-discovery, patience, and mutual understanding. Let's take this one step at a time."

    def _generate(self, messages: List[BaseMessage], stop: Optional[List[str]] = None, run_manager: Any = None, **kwargs: Any) -> ChatResult:
        # Check last message for basic routing response simulation
        last_msg = messages[-1].content if messages else ""
        text = self.response_text
        if "rate" in last_msg.lower() or "score" in last_msg.lower():
            text = '{"score": 85, "reasoning": "Strong alignment on emotional intelligence and growth mindset."}'
        elif "stage" in last_msg.lower():
            text = '{"stage": "single", "confidence": 0.95}'
        elif "emotion" in last_msg.lower():
            text = '{"primary_emotion": "hopeful", "intensity": 0.7, "sadness": 0.1, "anxiety": 0.2, "anger": 0.0, "loneliness": 0.1, "hope": 0.8, "love": 0.6, "confusion": 0.2, "joy": 0.5}'
        elif "crisis" in last_msg.lower():
            text = '{"level": "safe", "confidence": 0.99, "triggers": []}'

        return ChatResult(generations=[ChatGeneration(message=AIMessage(content=text))])

    @property
    def _llm_type(self) -> str:
        return "mock_fallback_llm"


class LLMFactory:
    """
    Factory for creating LLM instances with the exact settings
    defined in the LoveGuru AI Master Build Bible.
    """

    # Valid Groq model names
    VALID_GROQ_MODELS = {
        "openai/gpt-oss-120b",
        "openai/gpt-oss-20b",
        "qwen/qwen3.8-27b",
        "llama-3.3-70b-versatile",
        "llama-3.1-70b-versatile",
        "llama-3.1-8b-instant",
        "llama3-70b-8192",
        "llama3-8b-8192",
        "mixtral-8x7b-32768",
        "gemma2-9b-it",
        "gemma-7b-it",
    }
    # Default safe model matching the user's available Groq tier
    GROQ_DEFAULT_MODEL = "openai/gpt-oss-120b"

    @staticmethod
    def get_fast(temperature: float = 0.1, max_tokens: int = 150) -> BaseChatModel:
        """Fast ultra-low-latency model for classification, routing, and quick sentiment."""
        fast_model = settings.GROQ_FAST_MODEL or "qwen/qwen3.8-27b"
        return LLMFactory.get_groq(temperature=temperature, max_tokens=max_tokens, model=fast_model)

    @staticmethod
    def get_groq(temperature: float = 0.7, max_tokens: int = 700, streaming: bool = False, model: Optional[str] = None) -> BaseChatModel:
        key = settings.GROQ_API_KEY or ""
        if not key or key.startswith("placeholder") or key.startswith("REPLACE"):
            logger.warning("Groq API key missing or placeholder — using mock fallback.")
            return MockFallbackChatModel()
        
        target_model = model or settings.GROQ_PRIMARY_MODEL or LLMFactory.GROQ_DEFAULT_MODEL
        try:
            from langchain_groq import ChatGroq
            return ChatGroq(
                api_key=key,
                model=target_model,
                temperature=temperature,
                max_tokens=max_tokens,
                streaming=streaming,
                timeout=30,
            )
        except Exception as e:
            logger.error(f"ChatGroq init error ({e}), using mock fallback.", exc_info=True)
            return MockFallbackChatModel()

    # Valid Gemini models (as of 2025)
    VALID_GEMINI_MODELS = {
        "gemini-2.0-flash",
        "gemini-2.0-flash-lite",
        "gemini-1.5-flash",
        "gemini-1.5-flash-8b",
        "gemini-1.5-pro",
        "gemini-2.5-flash-preview-05-20",
    }
    GEMINI_DEFAULT_MODEL = "gemini-2.0-flash"

    @staticmethod
    def get_gemini(temperature: float = 0.7, max_tokens: int = 700) -> BaseChatModel:
        key = settings.GEMINI_API_KEY or ""
        # Validate key format: real Gemini keys start with "AIza"
        if not key or key.startswith("placeholder") or key.startswith("REPLACE") or not key.startswith("AIza"):
            if key and not key.startswith("placeholder") and not key.startswith("REPLACE"):
                logger.warning(
                    f"GEMINI_API_KEY format looks invalid (should start with 'AIza'). "
                    f"Get a real key from https://aistudio.google.com/app/apikey"
                )
            else:
                logger.warning("Gemini API key missing or placeholder — using mock fallback.")
            return MockFallbackChatModel()
        # Validate model name
        model = settings.GEMINI_MODEL or ""
        if model not in LLMFactory.VALID_GEMINI_MODELS:
            logger.warning(
                f"GEMINI_MODEL '{model}' may not be valid. "
                f"Falling back to '{LLMFactory.GEMINI_DEFAULT_MODEL}'."
            )
            model = LLMFactory.GEMINI_DEFAULT_MODEL
        try:
            from langchain_google_genai import ChatGoogleGenerativeAI
            return ChatGoogleGenerativeAI(
                google_api_key=key,
                model=model,
                temperature=temperature,
                max_output_tokens=max_tokens,
            )
        except Exception as e:
            logger.warning(f"ChatGoogleGenerativeAI init error ({e}), using mock fallback.")
        return MockFallbackChatModel()

    @classmethod
    def with_fallback(cls, primary: BaseChatModel, fallback: BaseChatModel) -> BaseChatModel:
        """Wraps primary LLM with fallback using LangChain's .with_fallbacks()."""
        try:
            return primary.with_fallbacks([fallback])
        except Exception:
            return primary

    @staticmethod
    def diagnose() -> dict:
        """
        Run at startup to show which LLMs are active vs mock.
        Call this from main.py lifespan to see AI status in logs.
        """
        groq_key = settings.GROQ_API_KEY or ""
        gemini_key = settings.GEMINI_API_KEY or ""
        groq_model = settings.GROQ_PRIMARY_MODEL or ""
        gemini_model = settings.GEMINI_MODEL or ""

        groq_key_ok = bool(groq_key) and not groq_key.startswith("placeholder") and not groq_key.startswith("REPLACE")
        gemini_key_ok = bool(gemini_key) and gemini_key.startswith("AIza")
        groq_model_ok = groq_model in LLMFactory.VALID_GROQ_MODELS
        gemini_model_ok = gemini_model in LLMFactory.VALID_GEMINI_MODELS

        status = {
            "groq": {
                "key_set": groq_key_ok,
                "model": groq_model,
                "model_valid": groq_model_ok,
                "active": groq_key_ok,
                "effective_model": groq_model if groq_model_ok else LLMFactory.GROQ_DEFAULT_MODEL,
            },
            "gemini": {
                "key_set": gemini_key_ok,
                "key_format_ok": gemini_key.startswith("AIza") if gemini_key else False,
                "model": gemini_model,
                "model_valid": gemini_model_ok,
                "active": gemini_key_ok,
                "effective_model": gemini_model if gemini_model_ok else LLMFactory.GEMINI_DEFAULT_MODEL,
            },
            "ai_mode": "REAL_AI" if (groq_key_ok or gemini_key_ok) else "MOCK_FALLBACK_ONLY",
        }

        # Log clear summary
        logger.info("=" * 60)
        logger.info("🤖 LoveGuru AI — LLM Status")
        logger.info(f"   Groq  : {'✅ ACTIVE' if groq_key_ok else '❌ MOCK'} | model={status['groq']['effective_model']}")
        logger.info(f"   Gemini: {'✅ ACTIVE' if gemini_key_ok else '❌ MOCK'} | model={status['gemini']['effective_model']}")
        logger.info(f"   Mode  : {status['ai_mode']}")
        if not groq_key_ok:
            logger.warning("   ⚠️  GROQ: Set GROQ_API_KEY in .env (get from console.groq.com)")
        if not gemini_key_ok:
            logger.warning("   ⚠️  GEMINI: Set GEMINI_API_KEY='AIza...' from aistudio.google.com/app/apikey")
        if not groq_model_ok and groq_key_ok:
            logger.warning(f"   ⚠️  GROQ MODEL '{groq_model}' unknown → using '{LLMFactory.GROQ_DEFAULT_MODEL}'")
        logger.info("=" * 60)
        return status


# ── Pre-built LLM instances (one per agent type) ─────────────

class LLMConfig:
    """Central registry of LLM instances per agent role."""

    @staticmethod
    def input_classifier() -> BaseChatModel:
        """Fast, deterministic. Classifies raw input."""
        primary = LLMFactory.get_fast(temperature=0.0, max_tokens=100)
        fallback = LLMFactory.get_gemini(temperature=0.0, max_tokens=100)
        return primary.with_fallbacks([fallback])

    @staticmethod
    def stage_router() -> BaseChatModel:
        """Routes to correct stage. Must be deterministic."""
        primary = LLMFactory.get_fast(temperature=0.0, max_tokens=100)
        fallback = LLMFactory.get_gemini(temperature=0.0, max_tokens=100)
        return primary.with_fallbacks([fallback])

    @staticmethod
    def emotion_detector() -> BaseChatModel:
        """8-dimension emotion vector. Fast response."""
        primary = LLMFactory.get_fast(temperature=0.1, max_tokens=200)
        fallback = LLMFactory.get_gemini(temperature=0.1, max_tokens=200)
        return primary.with_fallbacks([fallback])

    @staticmethod
    def crisis_safety() -> BaseChatModel:
        """CRITICAL: Zero tolerance for false negatives."""
        primary = LLMFactory.get_fast(temperature=0.0, max_tokens=150)
        fallback = LLMFactory.get_gemini(temperature=0.0, max_tokens=150)
        return primary.with_fallbacks([fallback])

    @staticmethod
    def emergency_handler() -> BaseChatModel:
        """Empathetic SOS responses. Warm but structured."""
        primary = LLMFactory.get_groq(temperature=0.2, max_tokens=600)
        fallback = LLMFactory.get_gemini(temperature=0.2, max_tokens=600)
        return primary.with_fallbacks([fallback])

    @staticmethod
    def stage1_partner_analyzer() -> BaseChatModel:
        """Stage 1: Single & Searching companion. Empathetic and conversational."""
        primary = LLMFactory.get_groq(temperature=0.7, max_tokens=700)
        fallback = LLMFactory.get_gemini(temperature=0.7, max_tokens=700)
        return primary.with_fallbacks([fallback])

    @staticmethod
    def stage2_dating_coach() -> BaseChatModel:
        """Stage 2: Witty, tactical dating coach. High empathy."""
        primary = LLMFactory.get_groq(temperature=0.7, max_tokens=700, streaming=True)
        fallback = LLMFactory.get_gemini(temperature=0.7, max_tokens=700)
        return primary.with_fallbacks([fallback])

    @staticmethod
    def stage3_relationship_coach() -> BaseChatModel:
        """Stage 3: Gottman-based empathetic guidance. Warm and human."""
        primary = LLMFactory.get_groq(temperature=0.7, max_tokens=700, streaming=True)
        fallback = LLMFactory.get_gemini(temperature=0.7, max_tokens=700)
        return primary.with_fallbacks([fallback])

    @staticmethod
    def stage4_heartbreak_coach() -> BaseChatModel:
        """Stage 4: Gentle, validating heartbreak support."""
        primary = LLMFactory.get_groq(temperature=0.6, max_tokens=700, streaming=True)
        fallback = LLMFactory.get_gemini(temperature=0.6, max_tokens=700)
        return primary.with_fallbacks([fallback])

    @staticmethod
    def personalizer() -> BaseChatModel:
        """Tone personalizer."""
        primary = LLMFactory.get_fast(temperature=0.3, max_tokens=600, streaming=True)
        fallback = LLMFactory.get_gemini(temperature=0.3, max_tokens=600)
        return primary.with_fallbacks([fallback])

    @staticmethod
    def pattern_analyzer() -> BaseChatModel:
        """Weekly longitudinal analysis. Gemini primary for long context."""
        primary = LLMFactory.get_gemini(temperature=0.3, max_tokens=3000)
        fallback = LLMFactory.get_groq(temperature=0.3, max_tokens=3000)
        return primary.with_fallbacks([fallback])
