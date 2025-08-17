from abc import ABC, abstractmethod

from langgraph.graph import StateGraph, START, END
from apps.agentic.core.messages import WorkerState
from apps.agentic.core.utils import build_llm
from langgraph.prebuilt import tools_condition

from lib.logger import get_logger

logger = get_logger("YADA")


class ToolAgent(ABC):

    """
    Abstract Base class for agents that use a language model to generate data and can call tools.
    """

    def __init__(self, tools, tool_node):
        self.__tools = tools
        self.__tool_node = tool_node
        self.__llm = build_llm()
        self.__prompt = self.create_prompt()
        self.__tooled_llm = self.__llm.bind_tools(self.__tools)
        self.__agent = self._create_agent()


    @property
    def tools(self):
        """
        Get the tools available to the agent.
        """
        
        self.__tools

    
    @property
    def tool_node(self):
        """
        Get the tool node used by the agent.
        """

        return self.__tool_node


    @property
    def agent(self):
        """
        Get the compiled agent state graph.
        """

        return self.__agent
    

    @property
    def llm(self):
        """
        Get the language model used by the agent.
        """

        return self.__llm
    

    @property
    def prompt(self):
        """
        Get the prompt template used by the agent.
        """

        return self.__prompt
    
    
    @property
    def tooled_llm(self):
        """
        Get the language model bound with tools.
        """

        return self.__tooled_llm
    

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
            .add_node("model", self._invoke_model)
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

        return graph.compile()
    

    @abstractmethod   
    def create_prompt(self):
        """
        Create the prompt template for the agent.
        This defines how the model should interpret the messages and what it should do.
        """

        raise NotImplementedError("Subclasses must implement this method to create a prompt template.") 
    
