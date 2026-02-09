from __future__ import annotations

from typing import Optional, Callable, Awaitable

from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig

from apps.agentic.core.agents.messages import WorkerState
from apps.agentic.agents.search_agent import SearchAgent
from apps.agentic.agents.plots.bar_chart_agent import BarChartAgent


class Orchestrator:
    """
    Minimal supervisor that routes a request to either SearchAgent or BarChartAgent.
    """

    def __init__(self) -> None:
        self._workers: dict[str, Callable[[WorkerState, RunnableConfig | None], Awaitable[WorkerState]]] = {
            "search": self._wrap_agent(SearchAgent().agent),
            "bar_chart": self._wrap_agent(BarChartAgent().agent),
        }

    async def process_request(self, request: str, session_id: Optional[str] = None) -> WorkerState:
        """
        Route the request to the bar chart or search agent based on a simple heuristic.
        """

        state: WorkerState = {"messages": [HumanMessage(content=request)]}
        config: RunnableConfig | None = None
        if session_id is not None:
            config = {"configurable": {"thread_id": session_id}}

        if self._should_plot(request):
            return await self._workers["bar_chart"](state, config)

        return await self._workers["search"](state, config)

    def _wrap_agent(self, agent) -> Callable[[WorkerState, RunnableConfig | None], Awaitable[WorkerState]]:
        async def runner(state: WorkerState, config: RunnableConfig | None) -> WorkerState:
            return await agent.ainvoke(state, config)

        return runner

    @staticmethod
    def _should_plot(request: str) -> bool:
        lowered = request.lower()
        keywords = ("bar chart", "chart", "plot", "visualize")
        return any(keyword in lowered for keyword in keywords)
