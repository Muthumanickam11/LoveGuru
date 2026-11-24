"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — ChromaDB Vector Store                  ║
║         Multi-collection storage for 4 relationship stages   ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import logging
from typing import List, Dict, Any, Optional
from config.settings import settings
from rag.embeddings import get_embedding

logger = logging.getLogger(__name__)

# In-memory storage fallback if ChromaDB is unavailable
_memory_store: Dict[str, List[Dict[str, Any]]] = {}
_chroma_client = None


def get_chroma_client():
    global _chroma_client
    if _chroma_client is not None:
        return _chroma_client

    try:
        import chromadb
        from chromadb.config import Settings as ChromaSettings
        os.makedirs(settings.CHROMA_PERSIST_DIR, exist_ok=True)
        _chroma_client = chromadb.PersistentClient(
            path=settings.CHROMA_PERSIST_DIR,
            settings=ChromaSettings(anonymized_telemetry=False)
        )
        logger.info(f"✅ ChromaDB client initialized at {settings.CHROMA_PERSIST_DIR}")
        return _chroma_client
    except Exception as e:
        logger.warning(f"⚠️ ChromaDB initialization failed: {e}. Using in-memory vector store.")
        _chroma_client = "memory"
        return _chroma_client


def add_documents_to_collection(
    collection_name: str,
    documents: List[Dict[str, Any]],
) -> None:
    """Adds documents with embeddings to a collection."""
    client = get_chroma_client()
    if client != "memory":
        try:
            collection = client.get_or_create_collection(name=collection_name)
            ids = [f"{collection_name}_{i}_{doc.get('metadata', {}).get('source', 'doc')}" for i, doc in enumerate(documents)]
            texts = [doc["content"] for doc in documents]
            metadatas = [doc.get("metadata", {}) for doc in documents]
            embeddings = [get_embedding(t) for t in texts]

            collection.upsert(
                ids=ids,
                documents=texts,
                metadatas=metadatas,
                embeddings=embeddings,
            )
            return
        except Exception as e:
            logger.warning(f"ChromaDB upsert failed ({e}), falling back to memory store")

    # Fallback in-memory store (idempotent on content)
    bucket = _memory_store.setdefault(collection_name, [])
    existing = {d["content"] for d in bucket}
    for doc in documents:
        content = doc["content"]
        if content in existing:
            continue
        emb = get_embedding(content)
        bucket.append({
            "content": content,
            "metadata": doc.get("metadata", {}),
            "embedding": emb,
        })
        existing.add(content)


def search_collection(
    collection_name: str,
    query_text: str,
    top_k: int = 3,
) -> List[Dict[str, Any]]:
    """Searches a collection for most similar documents."""
    client = get_chroma_client()
    query_vector = get_embedding(query_text)

    if client != "memory":
        try:
            collection = client.get_or_create_collection(name=collection_name)
            results = collection.query(
                query_embeddings=[query_vector],
                n_results=top_k,
            )
            docs = []
            if results and results.get("documents") and results["documents"][0]:
                for idx, text in enumerate(results["documents"][0]):
                    meta = results["metadatas"][0][idx] if results.get("metadatas") else {}
                    score = results["distances"][0][idx] if results.get("distances") else 0.8
                    docs.append({
                        "text": text,
                        "metadata": meta,
                        "source": meta.get("source", "Relationship Research"),
                        "score": 1.0 / (1.0 + float(score)),
                    })
            return docs
        except Exception as e:
            logger.warning(f"ChromaDB query failed ({e}), searching in-memory store")

    # In-memory cosine similarity search
    items = _memory_store.get(collection_name, [])
    if not items:
        return []

    # Simple dot product on normalized vectors (equivalent to cosine similarity)
    scored = []
    for it in items:
        dot = sum(a * b for a, b in zip(query_vector, it["embedding"]))
        scored.append((dot, it))

    scored.sort(key=lambda x: x[0], reverse=True)
    results = []
    for score, it in scored[:top_k]:
        results.append({
            "text": it["content"],
            "metadata": it.get("metadata", {}),
            "source": it.get("metadata", {}).get("source", "Relationship Research"),
            "score": round(max(0.0, min(1.0, float(score))), 4),
        })
    return results
