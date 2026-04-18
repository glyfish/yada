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
            Tool names that must be present. Logs a warning if any are missing
            (does not crash app startup).
        """
        try:
            client = MultiServerMCPClient(servers)
            discovered = {t.name: t for t in await client.get_tools()}
        except Exception as exc:
            logger.warning(
                f"MCPToolRegistry: could not connect to MCP server(s) — "
                f"MCP tools will be unavailable. Reason: {exc}"
            )
            return

        logger.debug(f"MCPToolRegistry discovered {len(discovered)} tools: {list(discovered.keys())}")

        missing = [name for name in required if name not in discovered]
        if missing:
            logger.warning(f"MCPToolRegistry: required tools not found on MCP server: {missing}")

        cls._tools = discovered
        cls._initialized = True
        logger.info(f"MCPToolRegistry initialized with {len(cls._tools)} tools: {list(cls._tools.keys())}")

    @classmethod
    def get(cls, name: str) -> BaseTool | None:
        """
        Return a single tool by name, or None if unavailable.
        """
        if not cls._check_initialized():
            return None
        if name not in cls._tools:
            logger.warning(f"MCPToolRegistry: tool '{name}' not found. Available: {list(cls._tools.keys())}")
            return None
        return cls._tools[name]

    @classmethod
    def get_many(cls, names: list[str]) -> list[BaseTool]:
        """
        Return a list of tools by name, in the order given.
        Missing or unavailable tools are omitted with a warning.
        """
        if not cls._check_initialized():
            return []
        missing = [name for name in names if name not in cls._tools]
        if missing:
            logger.warning(f"MCPToolRegistry: tools not found: {missing}. Available: {list(cls._tools.keys())}")
        return [cls._tools[name] for name in names if name in cls._tools]

    @classmethod
    def _check_initialized(cls) -> bool:
        if not cls._initialized:
            logger.warning("MCPToolRegistry: not initialized — MCP tools are unavailable.")
            return False
        return True
