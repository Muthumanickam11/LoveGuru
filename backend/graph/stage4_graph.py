"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Stage 4 Graph (After a Breakup)        ║
║  Grief-weather triage inside a safety-gated pipeline.        ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging

from langgraph.graph import StateGraph, END
from graph.graph_state import GuruGraphState
from agents.crisis_agent import crisis_agent
from agents.heartbreak_coach_agent import heartbreak_coach_agent
from agents.response_builder_agent import response_builder_agent

logger = logging.getLogger(__name__)


async def _safety(state: GuruGraphState) -> GuruGraphState:
    return await crisis_agent.run(state)


async def _coach(state: GuruGraphState) -> GuruGraphState:
    return await heartbreak_coach_agent.run(state)


async def _build(state: GuruGraphState) -> GuruGraphState:
    return await response_builder_agent.run(state)


async def _emergency(state: GuruGraphState) -> GuruGraphState:
    state["specialist_coaching"] = (
        "Please prioritize your immediate safety and reach a crisis helpline or emergency "
        "services now. Grief is heavy, but you do not carry it alone."
    )
    return state


def build_stage4_graph():
    graph = StateGraph(GuruGraphState)
    graph.add_node("safety", _safety)
    graph.add_node("heartbreak_coach", _coach)
    graph.add_node("build_response", _build)
    graph.add_node("emergency_handler", _emergency)
    graph.set_entry_point("safety")

    def branch(state: GuruGraphState) -> str:
        return "emergency_handler" if state.get("crisis_triggered") else "heartbreak_coach"

    graph.add_conditional_edges("safety", branch, {
        "emergency_handler": "emergency_handler", "heartbreak_coach": "heartbreak_coach"})
    graph.add_edge("heartbreak_coach", "build_response")
    graph.add_edge("emergency_handler", "build_response")
    graph.add_edge("build_response", END)
    return graph.compile()


stage4_graph = build_stage4_graph()