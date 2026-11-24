"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Shared Service Utilities               ║
║   LLM JSON helper + stage-data row resolution + safe casts   ║
╚══════════════════════════════════════════════════════════════╝
"""

import json
import logging
import re
from typing import Any, Callable, Dict, Optional, Type

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from config.llm_config import LLMConfig
from models.database_models import (
    Stage1Data, Stage2Data, Stage3Data, Stage4Data,
)

logger = logging.getLogger(__name__)

_JSON_BLOCK = re.compile(r"\{.*\}", re.DOTALL)


def extract_json(text: str) -> Optional[dict]:
    """Best-effort JSON extraction from an LLM response."""
    if not text:
        return None
    clean_text = text.strip()
    # 1. Direct parse
    try:
        data = json.loads(clean_text)
        if isinstance(data, dict):
            return data
    except (ValueError, TypeError):
        pass

    # 2. Markdown code block
    fence_match = re.search(r"```(?:json)?\s*(\{[\s\S]*?\})\s*```", clean_text, re.IGNORECASE)
    if fence_match:
        try:
            data = json.loads(fence_match.group(1))
            if isinstance(data, dict):
                return data
        except (ValueError, TypeError):
            pass

    # 3. Outer curly braces
    first_idx = clean_text.find("{")
    last_idx = clean_text.rfind("}")
    if first_idx != -1 and last_idx != -1 and last_idx > first_idx:
        candidate = clean_text[first_idx:last_idx + 1]
        try:
            data = json.loads(candidate)
            if isinstance(data, dict):
                return data
        except (ValueError, TypeError):
            pass
    return None


async def llm_json(
    prompt: str,
    llm_factory: Callable[[], Any],
    fallback: Dict[str, Any],
    temperature: Optional[float] = None,
) -> Dict[str, Any]:
    """Invoke an LLM expecting JSON. Returns *fallback* on any failure."""
    try:
        llm = llm_factory()
        result = await llm.ainvoke(prompt)
        parsed = extract_json(getattr(result, "content", "") or str(result))
        if isinstance(parsed, dict):
            return parsed
    except Exception as e:
        logger.warning(f"llm_json failed, using fallback: {e}", exc_info=True)
    return fallback


async def llm_text(
    prompt: str,
    llm_factory: Callable[[], Any],
    fallback: str,
) -> str:
    """Invoke an LLM expecting free text. Returns *fallback* on failure."""
    try:
        llm = llm_factory()
        result = await llm.ainvoke(prompt)
        content = (getattr(result, "content", "") or "").strip()
        return content or fallback
    except Exception as e:
        logger.warning(f"llm_text failed, using fallback: {e}")
        return fallback


_STAGE_MODELS: Dict[str, Type] = {
    "stage1": Stage1Data,
    "stage2": Stage2Data,
    "stage3": Stage3Data,
    "stage4": Stage4Data,
}


async def get_or_create_stage_data(
    db: AsyncSession,
    stage: str,
    profile_id,
):
    """Fetches (or lazily creates) the per-profile stage data row."""
    model = _STAGE_MODELS[stage]
    row = (await db.execute(
        select(model).where(model.profile_id == profile_id)
    )).scalar_one_or_none()
    if row is None:
        row = model(profile_id=profile_id)
        db.add(row)
        await db.flush()
    return row
