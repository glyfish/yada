from __future__ import annotations

from langgraph.graph import END

from apps.agentic.core.agents.react_agent import ReactAgent


class LinearAgent(ReactAgent):
    """
    Single-pass agent: model → tools → END.

    The ToolMessage is the final state message, so callers receive raw tool
    output without an extra LLM round-trip.
    """

    def _post_tools_target(self):
        return END
