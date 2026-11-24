"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Text Splitter & Chunker                ║
║         Recursive relationship science text chunking         ║
╚══════════════════════════════════════════════════════════════╝
"""

from typing import List, Dict, Any


def split_text_into_chunks(
    text: str,
    chunk_size: int = 500,
    chunk_overlap: int = 50,
    metadata: Dict[str, Any] = None
) -> List[Dict[str, Any]]:
    """Splits a document text into smaller, overlapping chunks."""
    if not text:
        return []

    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk_words = words[start:end]
        chunk_content = " ".join(chunk_words)

        chunk_data = {
            "content": chunk_content,
            "metadata": metadata or {},
        }
        chunks.append(chunk_data)

        if end == len(words):
            break
        start += (chunk_size - chunk_overlap)

    return chunks
