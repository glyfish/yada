from __future__ import annotations

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

from apps.agentic.core.agents.linear_agent import LinearAgent
from apps.agentic.agents.data.caching_fred_tool import CachingFredTool
from lib.logger import get_logger

logger = get_logger("YADA")


class DataFetcherAgent(LinearAgent):
    """
    Fetches time series data from external data sources via MCP tools.
    MCP tools are wrapped with caching so only a compact SeriesRef JSON
    flows through the agent messages — never the raw observations.
    """

    _mcp_tool_names: list[str] = ["fred_series_observations", "fred_series_info"]


    def __init__(self, mcp_tools: list):
        tool_node_name = "data_fetcher_tool_node"
        super().__init__([], tool_node_name, mcp_tools=mcp_tools)


    @classmethod
    async def create(cls) -> "DataFetcherAgent":
        mcp_tools = cls._discover_mcp_tools()
        by_name = {t.name: t for t in mcp_tools}
        wrapped = [
            CachingFredTool(
                wrapped=by_name["fred_series_observations"],
                info_tool=by_name.get("fred_series_info"),
            )
        ]
        return cls(mcp_tools=wrapped)


    def create_prompt(self):
        system_prompt = """
            <instructions>
            You are a data fetcher agent. Use the available MCP tools to retrieve time series
            data from external data sources.

            The tools return a SeriesRef JSON object — pass it back unmodified as your response.
            Do not summarize, reformat, or interpret it.

            When fetching FRED data use the fred_series_observations tool with a limit of
            10000 to retrieve the full series.
            </instructions>
            """

        logger.debug(f"DataFetcherAgent prompt: {system_prompt}")

        return ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
        ])
