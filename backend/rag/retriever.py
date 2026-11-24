"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Research Retriever                     ║
║         Stage-specific similarity retrieval & reranking      ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging
from typing import List, Dict, Any
from config.settings import settings
from rag.vector_store import search_collection

logger = logging.getLogger(__name__)


async def retrieve_chunks(
    query: str,
    stage: str = "single",
    top_k: int = None,
) -> List[Dict[str, Any]]:
    """
    Retrieves the most scientifically relevant research excerpts
    for a user query given their current life stage.

    Honors RAG_TOP_K (candidates), RAG_SCORE_THRESHOLD (min relevance)
    and RAG_FINAL_CHUNKS (max returned).
    """
    if not query:
        return []

    valid_stage = stage.lower() if stage else "single"
    if valid_stage not in ["single", "finding", "relationship", "heartbreak", "indian_context"]:
        valid_stage = "single"

    candidate_k = top_k or settings.RAG_TOP_K
    threshold = settings.RAG_SCORE_THRESHOLD
    final_k = settings.RAG_FINAL_CHUNKS

    try:
        # The stage collection is inherently relevant (it was routed by stage),
        # so its best hits are always used.
        primary = search_collection(
            collection_name=valid_stage, query_text=query, top_k=candidate_k)

        results = list(primary)

        # Augment with the cross-cutting Indian-context corpus only when the
        # stage collection is sparse. The score threshold gates this so
        # unrelated cultural excerpts are never injected as noise.
        if valid_stage != "indian_context" and len(results) < final_k:
            extra = search_collection(
                collection_name="indian_context",
                query_text=query,
                top_k=candidate_k,
            )
            results.extend(r for r in extra if r.get("score", 0.0) >= threshold)

        # De-duplicate and keep the strongest hits.
        seen = set()
        deduped = []
        for r in sorted(results, key=lambda x: x.get("score", 0.0), reverse=True):
            key = r.get("text", "")
            if key in seen:
                continue
            seen.add(key)
            deduped.append(r)

        final = deduped[:final_k]
        logger.info(
            f"Retrieved {len(final)} chunks for stage '{valid_stage}' "
            f"(candidates={len(results)}, threshold={threshold})"
        )
        return final
    except Exception as e:
        logger.error(f"Error retrieving research chunks: {e}")
        return []
