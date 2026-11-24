"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Stage 2 Graph (Finding Love)           ║
║  Emotion-aware dating coaching with profile/conversation lens║
╚══════════════════════════════════════════════════════════════╝
"""

import logging

from langgraph.graph import StateGraph, END
from graph.graph_state import GuruGraphState
from agents.emotion_agent import emotion_agent
from agents.personalizer_agent import personalizer_agent
from agents.response_builder_agent import response_builder_agent

logger = logging.getLogger(__name__)


async def _detect_emotion(state: GuruGraphState) -> GuruGraphState:
    return await emotion_agent.run(state)


async def _stage2_coach(state: GuruGraphState) -> GuruGraphState:
    from agents import safe_llm_text
    from config.llm_config import LLMConfig
    message = state.get("raw_message", "")
    coaching = await safe_llm_text(
        "You are LoveGuru's witty, warm dating coach. Give tactical, romance-smart coaching on "
        f"this dating situation.\nMessage:\n{message}",
        LLMConfig.stage2_dating_coach,
        "Match their energy, keep it playful, and move toward a real-world plan.",
    )
    return {**state, "specialist_coaching": coaching}


async def _personalize(state: GuruGraphState) -> GuruGraphState:
    return await personalizer_agent.run(state)


async def _build(state: GuruGraphState) -> GuruGraphState:
    return await response_builder_agent.run(state)


def build_stage2_graph():
    graph = StateGraph(GuruGraphState)
    graph.add_node("emotion", _detect_emotion)
    graph.add_node("dating_coach", _stage2_coach)
    graph.add_node("personalize", _personalize)
    graph.add_node("build_response", _build)
    graph.set_entry_point("emotion")
    graph.add_edge("emotion", "dating_coach")
    graph.add_edge("dating_coach", "personalize")
    graph.add_edge("personalize", "build_response")
    graph.add_edge("build_response", END)
    return graph.compile()


stage2_graph = build_stage2_graph()