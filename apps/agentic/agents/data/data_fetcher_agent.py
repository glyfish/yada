from __future__ import annotations

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

from apps.agentic.core.agents.linear_agent import LinearAgent
from lib.logger import get_logger

logger = get_logger("YADA")


class DataFetcherAgent(LinearAgent):
    """
    Fetches time series data from external data sources via MCP tools.
    Only the tools listed in _mcp_tool_names are selected from the MCP server.
    An exception is raised if any required tool is not found.
    """

    _mcp_tool_names: list[str] = ["fred_series_observations"]


    def __init__(self, mcp_tools: list):
        tool_node_name = "data_fetcher_tool_node"
        super().__init__([], tool_node_name, mcp_tools=mcp_tools)


    def create_prompt(self):
        system_prompt = """
            <instructions>
            You are a data fetcher agent. Use the available MCP tools to retrieve time series data
            from external data sources. Return the raw tool result unmodified — do not summarize,
            reformat, or interpret it. The result will be consumed by downstream agents for
            plotting or analysis.

            When fetching FRED data use the fred_series_observations tool with a limit of
            10000 to retrieve the full series.
            </instructions>
            """

        logger.debug(f"DataFetcherAgent prompt: {system_prompt}")

        return ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
        ])
