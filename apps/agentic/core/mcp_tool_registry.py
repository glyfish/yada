from __future__ import annotations

from langchain_core.tools import BaseTool
from langchain_mcp_adapters.client import MultiServerMCPClient

from lib.logger import get_logger

logger = get_logger("YADA")


class MCPToolRegistry:
    """
    Singleton registry for MCP tools. Initialized once at app startup.
    Agents pull tools from the registry instead of connecting to the MCP server
    on each request.
    """

    _tools: dict[str, BaseTool] = {}
    _initialized: bool = False

    @classmethod
    async def initialize(cls, servers: dict, required: list[str]) -> None:
        """
        Connect to MCP servers, discover tools, validate all required tool names
        are present, and populate the registry.

        Parameters
        ----------
        servers : dict
            MCP server connection configs keyed by server name.
            e.g. {"fred": {"transport": "sse", "url": "http://localhost:8080/sse"}}
        required : list[str]
            Tool names that must be present. Raises RuntimeError if any are missing.
        """
        client = MultiServerMCPClient(servers)
        discovered = {t.name: t for t in await client.get_tools()}

        logger.debug(f"MCPToolRegistry discovered {len(discovered)} tools: {list(discovered.keys())}")

        missing = [name for name in required if name not in discovered]
        if missing:
            raise RuntimeError(f"MCPToolRegistry: required tools not found on MCP server: {missing}")

        cls._tools = discovered
        cls._initialized = True
        logger.info(f"MCPToolRegistry initialized with {len(cls._tools)} tools: {list(cls._tools.keys())}")

    @classmethod
    def get(cls, name: str) -> BaseTool:
        """
        Return a single tool by name.

        Raises
        ------
        RuntimeError
            If the registry has not been initialized.
        KeyError
            If the tool name is not in the registry.
        """
        cls._check_initialized()
        if name not in cls._tools:
            raise KeyError(f"MCPToolRegistry: tool '{name}' not found. Available: {list(cls._tools.keys())}")
        return cls._tools[name]

    @classmethod
    def get_many(cls, names: list[str]) -> list[BaseTool]:
        """
        Return a list of tools by name, in the order given.

        Raises
        ------
        RuntimeError
            If the registry has not been initialized or any name is missing.
        """
        cls._check_initialized()
        missing = [name for name in names if name not in cls._tools]
        if missing:
            raise RuntimeError(f"MCPToolRegistry: tools not found: {missing}. Available: {list(cls._tools.keys())}")
        return [cls._tools[name] for name in names]

    @classmethod
    def _check_initialized(cls) -> None:
        if not cls._initialized:
            raise RuntimeError(
                "MCPToolRegistry has not been initialized. "
                "Call MCPToolRegistry.initialize() at app startup."
            )
