from abc import ABC, abstractmethod

from langgraph.graph import StateGraph, START, END
from apps.agentic.core.agents.messages import WorkerState
from apps.agentic.core.llm_factory import agent_llm_model

from langgraph.prebuilt import tools_condition
from langchain_core.tools import BaseTool
from lib.logger import get_logger
from langgraph.prebuilt import ToolNode
from apps.agentic.core.checkpointer import checkpointer
from langsmith.run_helpers import traceable

logger = get_logger("YADA")


class ReactAgent(ABC):

    """
    Abstract Base class for agents that use a language model to generate data and can call tools.
    """

    def __init__(self, tools: list[BaseTool], tool_node_name: str):
        self._tools = tools
        self._tool_node_name = tool_node_name
        self._tool_node = ToolNode(tools, name=self._tool_node_name)
        self._llm = agent_llm_model()
        self._prompt = self.create_prompt()
        self._tooled_llm = self._llm.bind_tools(self._tools)
        self._model_runner = traceable(
            run_type="chain",
            name=f"{self.__class__.__name__}.model",
        )(self._invoke_model)
        self._agent = self._create_agent()


    @property
    def tools(self):
        """
        Get the tools available to the agent.
        """
        
        return self._tools


    @property
    def tool_node_name(self):
        """
        Get the name of the tool node.
        """

        return self._tool_node_name


    @property
    def tool_node(self):
        """
        Get the tool node used by the agent.
        """

        return self._tool_node


    @property
    def agent(self):
        """
        Get the compiled agent state graph.
        """

        return self._agent
    

    @property
    def llm(self):
        """
        Get the language model used by the agent.
        """

        return self._llm
    

    @property
    def prompt(self):
        """
        Get the prompt template used by the agent.
        """

        return self._prompt
    
    
    @property
    def tooled_llm(self):
        """
        Get the language model bound with tools.
        """

        return self._tooled_llm
    

    async def _invoke_model(self, state: WorkerState, config=None) -> WorkerState:
        """
        Invoke the agent with the current state.
        """

        messages = state["messages"]
        prompt_messages = self.prompt.format_messages(messages=messages)
        result = await self.tooled_llm.ainvoke(prompt_messages)
        return {"messages": [result]}

    
    def _create_agent(self):
        """
        Create the state graph for the tool agent.
        This defines the flow of the agent's operations.
        """

        graph = (
            StateGraph(WorkerState)
            .add_node("model", self._model_runner)
            .add_node("tools", self.tool_node)
            .add_edge(START, "model")
            .add_edge("tools", "model")
            .add_conditional_edges(
                "model",
                tools_condition,
                {
                    "tools": "tools",
                    END: END,
                }
            )
        )

        return graph.compile(checkpointer=checkpointer)
    

    @abstractmethod   
    def create_prompt(self):
        """
        Create the prompt template for the agent.
        This defines how the model should interpret the messages and what it should do.
        """

        raise NotImplementedError("Subclasses must implement this method to create a prompt template.") 
    
