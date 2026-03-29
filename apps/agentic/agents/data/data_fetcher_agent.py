from __future__ import annotations

from collections.abc import Mapping

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.sessions import SSEConnection

from apps.agentic.core.agents.react_agent import ReactAgent
from apps.agentic.core.constants import MCP_URL
from lib.logger import get_logger

logger = get_logger("YADA")

_mcp_servers: Mapping[str, SSEConnection] = {
    "fred": {"transport": "sse", "url": MCP_URL},
}


class DataFetcherAgent(ReactAgent):
    """
    Fetches time series data from external data sources via MCP tools.
    Tool discovery runs on instantiation — all tools exposed by the MCP server
    are loaded automatically and passed to the agent.
    """

    def __init__(self, tools: list):
        tool_node_name = "data_fetcher_tool_node"
        super().__init__(tools, tool_node_name)

    @classmethod
    async def create(cls) -> "DataFetcherAgent":
        """
        Async factory. Connects to the MCP server, discovers all available tools,
        and returns a fully initialized DataFetcherAgent.
        """
        client = MultiServerMCPClient(dict(_mcp_servers))
        tools = await client.get_tools()

        logger.debug(f"DataFetcherAgent discovered {len(tools)} MCP tools: {[t.name for t in tools]}")
        return cls(tools)

    def create_prompt(self):
        system_prompt = """
            <instructions>
            You are a data fetcher agent. Use the available MCP tools to retrieve time series data
            from external data sources. Return the raw tool result unmodified — do not summarize,
            reformat, or interpret it. The result will be consumed by downstream agents for
            plotting or analysis.

            When fetching FRED data use a limit of 10000 to retrieve the full series.
            </instructions>
            """

        logger.debug(f"DataFetcherAgent prompt: {system_prompt}")

        return ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
        ])
