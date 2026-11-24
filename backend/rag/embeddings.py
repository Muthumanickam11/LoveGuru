"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Embedding Engine                       ║
║         SentenceTransformers with fallback vector generator  ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging
import hashlib
import math
import re
from typing import List
from config.settings import settings

logger = logging.getLogger(__name__)

_model_instance = None

_TOKEN_RE = re.compile(r"[a-z0-9]+")

_STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "if", "then", "so", "of", "to", "in",
    "on", "at", "for", "with", "about", "as", "by", "is", "are", "was", "were",
    "be", "been", "being", "am", "i", "you", "we", "they", "he", "she", "it",
    "my", "your", "our", "their", "his", "her", "its", "me", "us", "them",
    "this", "that", "these", "those", "do", "does", "did", "have", "has", "had",
    "not", "no", "yes", "will", "would", "can", "could", "should", "may",
    "might", "must", "from", "into", "up", "out", "over", "again", "more",
}


def get_embedding_model():
    """Lazy load embedding model with deterministic fallback.

    Real SentenceTransformer loading is opt-in via RAG_EMBEDDING_REQUIRED=True
    to avoid HuggingFace downloads that can hang offline/dev startups. Model
    loading runs in a time-boxed thread; on timeout we keep the fallback.
    """
    global _model_instance
    if _model_instance is not None:
        return _model_instance

    if not settings.RAG_EMBEDDING_REQUIRED:
        logger.info("Real embedding model disabled (RAG_EMBEDDING_REQUIRED=False) — using deterministic fallback embeddings.")
        _model_instance = "fallback"
        return _model_instance

    import concurrent.futures

    def _load() -> object:
        from sentence_transformers import SentenceTransformer
        return SentenceTransformer(settings.EMBEDDING_MODEL)

    try:
        logger.info(f"Loading embedding model: {settings.EMBEDDING_MODEL}")
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
            future = pool.submit(_load)
            model = future.result(timeout=30)
        _model_instance = model
        return _model_instance
    except Exception as e:
        logger.warning(f"Could not load SentenceTransformer ({e}). Using deterministic fallback embedding generator.")
        _model_instance = "fallback"
        return _model_instance


def _lexical_embedding(text: str, dim: int = 384) -> List[float]:
    """Deterministic feature-hashing bag-of-words embedding.

    Tokens (and word bigrams) are hashed into `dim` buckets with signed
    weights, then L2-normalized. Unlike a plain whole-string hash, the dot
    product of two vectors reflects shared vocabulary, so cosine similarity
    is meaningful for retrieval without any external model.
    """
    vec = [0.0] * dim
    tokens = [t for t in _TOKEN_RE.findall(text.lower()) if t not in _STOPWORDS]
    if not tokens:
        return vec

    def _bucket(token: str, weight: float) -> None:
        h = int.from_bytes(hashlib.blake2b(token.encode("utf-8"), digest_size=8).digest(), "big")
        idx = h % dim
        sign = 1.0 if (h >> 63) & 1 else -1.0
        vec[idx] += sign * weight

    for tok in tokens:
        _bucket(tok, 1.0)
    for first, second in zip(tokens, tokens[1:]):
        _bucket(f"{first}_{second}", 0.5)

    norm = math.sqrt(sum(v * v for v in vec))
    if norm > 0:
        vec = [round(v / norm, 6) for v in vec]
    return vec


def get_embedding(text: str) -> List[float]:
    """Generates an embedding vector for a given string."""
    model = get_embedding_model()
    if model != "fallback" and hasattr(model, "encode"):
        try:
            vector = model.encode(text)
            return vector.tolist() if hasattr(vector, "tolist") else list(vector)
        except Exception as e:
            logger.warning(f"Encoding failed ({e}), falling back to deterministic vector.")

    return _lexical_embedding(text)


def get_embeddings_batch(texts: List[str]) -> List[List[float]]:
    """Generates embeddings for a batch of strings."""
    return [get_embedding(t) for t in texts]
