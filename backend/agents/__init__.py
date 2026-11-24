"""
╔══════════════════════════════════════════════════════════════╗
║          LOVEGURU AI — Agent Library                          ║
║  Twelve specialized agents mirroring the LangGraph nodes.    ║
║  Each exposes `name` and `async def run(state) -> dict`.     ║
╚══════════════════════════════════════════════════════════════╝
"""

import json
import logging
import re
from typing import Any, Callable, Dict, Optional

logger = logging.getLogger(__name__)

_JSON_BLOCK = re.compile(r"\{.*\}", re.DOTALL)


def extract_json(text: Optional[str]) -> Optional[dict]:
    if not text:
        return None
    try:
        return json.loads(text)
    except (ValueError, TypeError):
        pass
    match = _JSON_BLOCK.search(text)
    if match:
        try:
            return json.loads(match.group(0))
        except (ValueError, TypeError):
            return None
    return None


async def safe_llm_json(
    prompt: str,
    factory: Callable[[], Any],
    fallback: Dict[str, Any],
    temperature: Optional[float] = None,
) -> Dict[str, Any]:
    """Run an LLM expecting JSON, always returning a dict."""
    try:
        llm = factory()
        result = await llm.ainvoke(prompt)
        parsed = extract_json(getattr(result, "content", "") or str(result))
        if isinstance(parsed, dict):
            return parsed
    except Exception as e:
        logger.warning(f"safe_llm_json fell back after: {e}")
    return fallback


async def safe_llm_text(prompt: str, factory: Callable[[], Any], fallback: str) -> str:
    try:
        llm = factory()
        result = await llm.ainvoke(prompt)
        content = (getattr(result, "content", "") or "").strip()
        return content or fallback
    except Exception as e:
        logger.warning(f"safe_llm_text fell back after: {e}")
        return fallback