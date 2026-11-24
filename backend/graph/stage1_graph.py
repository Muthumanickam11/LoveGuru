"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Stage 1 Graph (Single & Searching)     ║
║  A focused LangGraph: intake -> partner analysis -> personal  ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging

from langgraph.graph import StateGraph, END
from graph.graph_state import GuruGraphState
from agents.partner_analysis_agent import partner_analysis_agent
from agents.personalizer_agent import personalizer_agent
from agents.response_builder_agent import response_builder_agent

logger = logging.getLogger(__name__)


async def _analyze(state: GuruGraphState) -> GuruGraphState:
    return await partner_analysis_agent.run(state)


async def _personalize(state: GuruGraphState) -> GuruGraphState:
    return await personalizer_agent.run(state)


async def _build(state: GuruGraphState) -> GuruGraphState:
    return await response_builder_agent.run(state)


def build_stage1_graph():
    graph = StateGraph(GuruGraphState)
    graph.add_node("partner_analysis", _analyze)
    graph.add_node("personalize", _personalize)
    graph.add_node("build_response", _build)
    graph.set_entry_point("partner_analysis")
    graph.add_edge("partner_analysis", "personalize")
    graph.add_edge("personalize", "build_response")
    graph.add_edge("build_response", END)
    return graph.compile()


stage1_graph = build_stage1_graph()