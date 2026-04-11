from abc import ABC

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition, ToolNode
from langchain_core.tools import BaseTool

from apps.agentic.core.agents.messages import WorkerState
from apps.agentic.core.agents.react_node import ReactNode
from apps.agentic.core.checkpointer import checkpointer
from apps.agentic.core.mcp_tool_registry import MCPToolRegistry
from lib.logger import get_logger

logger = get_logger("YADA")


class ReactAgent(ABC):
    """
    Abstract base class for ReAct-style agents. Owns the graph topology
    (model → tools → model loop). Composes a ReactNode for LLM invocation.

    By default creates a ReactNode from create_prompt(). Pass a custom node
    to override LLM behavior without subclassing.

    Class variables:
        _mcp_tool_names: list[str]
            MCP tool names this agent requires. Subclasses override to declare
            which MCP tools they need. Discovery runs automatically in create().
    """

    _mcp_tool_names: list[str] = []

    def __init__(self, tools: list[BaseTool], tool_node_name: str,
                 mcp_tools: list[BaseTool] = [], node: ReactNode | None = None):
        all_tools = tools + mcp_tools
        self._mcp_tools = mcp_tools
        if node is None:
            node = ReactNode(all_tools, self.create_prompt(), name=self.__class__.__name__)
        self._node = node
        self._tool_node = ToolNode(all_tools, name=tool_node_name)
        self._tool_node_name = tool_node_name
        self._agent = self._create_agent()

    
    @property
    def node(self) -> ReactNode:
        return self._node

    
    @property
    def tool_node_name(self) -> str:
        return self._tool_node_name

    
    @property
    def tool_node(self):
        return self._tool_node

    
    @property
    def agent(self):
        return self._agent

    @property
    def mcp_tools(self) -> list[BaseTool]:
        return self._mcp_tools


    @classmethod
    def _discover_mcp_tools(cls) -> list[BaseTool]:
        """
        Fetch required MCP tools from the registry.
        MCPToolRegistry must be initialized at app startup before this is called.
        """
        tools = MCPToolRegistry.get_many(cls._mcp_tool_names)
        logger.debug(f"{cls.__name__} using MCP tools: {[t.name for t in tools]}")
        return tools


    @classmethod
    async def create(cls) -> "ReactAgent":
        """
        Async factory. Discovers MCP tools if _mcp_tool_names is set, then
        constructs the agent passing resolved tools via mcp_tools=.
        Subclasses override only when they need additional async setup.
        """
        mcp_tools = cls._discover_mcp_tools() if cls._mcp_tool_names else []
        return cls(mcp_tools=mcp_tools)  # type: ignore[call-arg]


    def create_prompt(self):
        raise NotImplementedError(
            "Subclasses must implement create_prompt() or pass a ReactNode to the constructor."
        )


    def _create_agent(self):
        graph = (
            StateGraph(WorkerState)
            .add_node("model", self._node.model_runner)
            .add_node("tools", self.tool_node)
            .add_edge(START, "model")
            .add_edge("tools", "model")
            .add_conditional_edges(
                "model",
                tools_condition,
                {
                    "tools": "tools",
                    END: END,
                },
            )
        )
        return graph.compile(checkpointer=checkpointer)
