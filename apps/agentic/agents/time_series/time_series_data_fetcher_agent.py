from __future__ import annotations

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

from apps.agentic.core.agents.linear_agent import LinearAgent
from apps.agentic.agents.data.caching_fred_tool import CachingFredTool
from apps.agentic.agents.data.caching_tiingo_tool import CachingTiingoTool
from lib.logger import get_logger

logger = get_logger("YADA")


class TimeSeriesDataFetcherAgent(LinearAgent):
    """
    Fetches time series data from external data sources via MCP tools.
    MCP tools are wrapped with caching so only a compact SeriesRef JSON
    flows through the agent messages — never the raw observations.
    """

    _mcp_tool_names: list[str] = [
        "fred_series_observations",
        "fred_series_info",
        "tiingo_price_series",
        "tiingo_series_info",
    ]


    def __init__(self, mcp_tools: list):
        tool_node_name = "time_series_data_fetcher_tool_node"
        super().__init__([], tool_node_name, mcp_tools=mcp_tools)


    @classmethod
    async def create(cls) -> "TimeSeriesDataFetcherAgent":
        mcp_tools = cls._discover_mcp_tools()
        by_name = {t.name: t for t in mcp_tools}
        wrapped = []
        if "fred_series_observations" in by_name:
            wrapped.append(
                CachingFredTool(
                    wrapped=by_name["fred_series_observations"],
                    info_tool=by_name.get("fred_series_info"),
                )
            )
        if "tiingo_price_series" in by_name:
            wrapped.append(
                CachingTiingoTool(
                    wrapped=by_name["tiingo_price_series"],
                    info_tool=by_name.get("tiingo_series_info"),
                )
            )
        if not wrapped:
            raise RuntimeError(
                "TimeSeriesDataFetcherAgent.create: none of the expected MCP tools were "
                f"discovered ({cls._mcp_tool_names}). Is the MCP server running?"
            )
        return cls(mcp_tools=wrapped)


    def create_prompt(self):
        system_prompt = """
            <instructions>
            You are a time series data fetcher agent. Use the available MCP tools to retrieve time series
            data from external data sources.

            The tools return a SeriesRef JSON object — pass it back unmodified as your response.
            Do not summarize, reformat, or interpret it.

            When fetching FRED data use the fred_series_observations tool with a limit of
            10000 to retrieve the full series.

            For ETF, mutual fund, or stock price history, use the tiingo_price_series tool
            with the ticker symbol (e.g. SPY); it returns the full adjusted-close price series.
            </instructions>
            """

        logger.debug(f"TimeSeriesDataFetcherAgent prompt: {system_prompt}")

        return ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
        ])
