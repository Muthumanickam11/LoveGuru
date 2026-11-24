"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Unified RAG Pipeline                   ║
║         Corpus indexer and query orchestration               ║
╚══════════════════════════════════════════════════════════════╝
"""

import asyncio
import logging
from typing import List, Dict, Any
from rag.document_loader import load_seed_corpus
from rag.retriever import retrieve_chunks

logger = logging.getLogger(__name__)


async def initialize_rag() -> None:
    """Initializes the RAG vector database and loads seed research.

    Runs corpus indexing in a worker thread so slow model loads can never
    block the event loop (and therefore the server from starting).
    """
    logger.info("Initializing LoveGuru RAG knowledge base...")
    loop = asyncio.get_running_loop()
    try:
        await loop.run_in_executor(None, load_seed_corpus)
        logger.info("\u2705 LoveGuru RAG knowledge base ready")
    except Exception as e:
        logger.warning(f"RAG initialization failed (non-fatal): {e}")


async def query_rag(query: str, stage: str = "single", top_k: int = 3) -> List[Dict[str, Any]]:
    """Public query helper for retrieving research chunks."""
    return await retrieve_chunks(query=query, stage=stage, top_k=top_k)
