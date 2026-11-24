"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — RAG Agent                               ║
║  Retrieves evidence-based context for coaching responses.     ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging

from agents import safe_llm_json
from config.llm_config import LLMConfig

logger = logging.getLogger(__name__)


class RAGAgent:
    name = "rag_agent"

    async def run(self, state: dict) -> dict:
        query = state.get("raw_message", "")
        retrieved = state.get("rag_context", {})
        if not retrieved.get("context"):
            try:
                from rag.rag_pipeline import retrieve_context
                retrieved = await retrieve_context(query, top_k=3) or retrieved
            except Exception as e:
                logger.debug(f"RAG retrieval unavailable: {e}")

        segments = retrieved.get("context") or retrieved.get("sources") or []
        summary_fallback = "Grounded guidance based on your shared history and evidence-based relationship science."
        summary = summary_fallback
        if segments:
            text = "\n".join(str(s) if isinstance(s, str) else str(s.get("text", s)) for s in segments)
            prompt = (
                "Synthesize a brief, warm coaching summary from these retrieved sources.\nSources:\n"
                + text
            )
            summary_out = await safe_llm_json(
                prompt, LLMConfig.emotion_detector, {"summary": summary_fallback})
            summary = summary_out.get("summary", summary_fallback)

        return {
            **state,
            "rag_context": {
                "retrieved": bool(segments),
                "sources": [str(s) if isinstance(s, str) else s.get("source", str(s)) for s in segments],
                "summary": summary,
            },
        }


rag_agent = RAGAgent()