from abc import ABC

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition, ToolNode
from langchain_core.tools import BaseTool

from apps.agentic.core.agents.messages import WorkerState
from apps.agentic.core.agents.react_node import ReactNode
from apps.agentic.core.checkpointer import checkpointer
from lib.logger import get_logger

logger = get_logger("YADA")


class ReactAgent(ABC):
    """
    Abstract base class for ReAct-style agents. Owns the graph topology
    (model → tools → model loop). Composes a ReactNode for LLM invocation.

    By default creates a ReactNode from create_prompt(). Pass a custom node
    to override LLM behavior without subclassing.
    """

    def __init__(self, tools: list[BaseTool], tool_node_name: str, node: ReactNode | None = None):
        if node is None:
            node = ReactNode(tools, self.create_prompt(), name=self.__class__.__name__)
        self._node = node
        self._tool_node = ToolNode(tools, name=tool_node_name)
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
