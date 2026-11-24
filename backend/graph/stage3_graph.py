"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Stage 3 Graph (In a Relationship)      ║
║  Gottman counseling floor with safety gate preserved.        ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging

from langgraph.graph import StateGraph, END
from graph.graph_state import GuruGraphState
from agents.crisis_agent import crisis_agent
from agents.relationship_counselor_agent import relationship_counselor_agent
from agents.response_builder_agent import response_builder_agent

logger = logging.getLogger(__name__)


async def _safety(state: GuruGraphState) -> GuruGraphState:
    return await crisis_agent.run(state)


async def _counsel(state: GuruGraphState) -> GuruGraphState:
    return await relationship_counselor_agent.run(state)


async def _build(state: GuruGraphState) -> GuruGraphState:
    return await response_builder_agent.run(state)


async def _emergency(state: GuruGraphState) -> GuruGraphState:
    state["specialist_coaching"] = (
        "If there is any immediate risk to anyone's safety, please stop and call a crisis "
        "helpline or emergency services right now. You matter."
    )
    return state


def build_stage3_graph():
    graph = StateGraph(GuruGraphState)
    graph.add_node("safety", _safety)
    graph.add_node("counselor", _counsel)
    graph.add_node("build_response", _build)
    graph.add_node("emergency_handler", _emergency)
    graph.set_entry_point("safety")

    def branch(state: GuruGraphState) -> str:
        return "emergency_handler" if state.get("crisis_triggered") else "counselor"

    graph.add_conditional_edges("safety", branch, {
        "emergency_handler": "emergency_handler", "counselor": "counselor"})
    graph.add_edge("counselor", "build_response")
    graph.add_edge("emergency_handler", "build_response")
    graph.add_edge("build_response", END)
    return graph.compile()


stage3_graph = build_stage3_graph()