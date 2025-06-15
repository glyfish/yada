

from langchain_community.tools import TavilySearchResults
from langgraph.graph import StateGraph, START, END
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.prebuilt import ToolNode

from apps.agentic.core.messages import WorkerState
from apps.agentic.core.utils import build_llm, should_continue


class SearchAgent:
    """
    Search Agent that uses a language model to research and find relevant information.
    It can call tools like TavilySearchResults to fetch search results.
    """

    def __init__(self):
        self.__llm = build_llm()
        self.__prompt = self.__create_prompt()
        self.__tools = [TavilySearchResults()]
        self.__tool_node = ToolNode(self.__tools, name="researcher_tool_node")
        self.__tooled_llm = self.__llm.bind_tools(self.__tools)
        self.__agent = self.__create_agent()


    @property
    def agent(self):
        """
        Get the compiled agent state graph.
        """
        return self.__agent
    
    async def __invoke_model(self, state: WorkerState, config=None) -> WorkerState:
        """
        Invoke the agent with the current state.
        """

        messages = state["messages"]
        prompt_messages = self.__prompt.format_messages(messages=messages)
        result = await self.__tooled_llm.ainvoke(prompt_messages)
        return {"messages": [result]}

    
    def __create_prompt(self):
        """
        Create the prompt template for the researcher agent.
        This defines how the model should interpret the messages and what it should do.
        """
    
        return ChatPromptTemplate.from_messages([
            ("system", "You are a researcher. Given the conversation below, dig up relevant facts or decide which tool to call."),
            MessagesPlaceholder(variable_name="messages"),
            ("system", "If you choose to call a tool, do so; otherwise, provide your findings in markdown text."),
        ])


    def __create_agent(self):
        """
        Create the state graph for the researcher agent.
        This defines the flow of the agent's operations.
        """

        graph = (
            StateGraph(WorkerState)
            .add_node("model", self.__invoke_model)
            .add_node("tool", self.__tool_node)
            .add_edge(START, "model")
            .add_edge("tool", "model")
            .add_conditional_edges(
                "model",
                should_continue,
                {
                    "tool": "tool",
                    END: END,
                }
            )
        )

        return graph.compile()
