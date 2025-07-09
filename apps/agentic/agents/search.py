

from langchain_community.tools import TavilySearchResults
from langgraph.graph import StateGraph, START, END
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.prebuilt import ToolNode

from apps.agentic.core.messages import WorkerState
from apps.agentic.core.tool_agent import ToolAgent
from apps.agentic.core.utils import build_llm, should_continue


class SearchAgent(ToolAgent):
    """
    Search Agent that uses a language model to research and find relevant information.
    It can call tools like TavilySearchResults to fetch search results.
    """

    def __init__(self):
        tools = [TavilySearchResults()]
        tool_node = ToolNode(tools, name="tavily_search_tool_node")
        super().__init__(tools, tool_node)
    

    def create_prompt(self):
        """
        Create the prompt template for the researcher agent.
        This defines how the model should interpret the messages and what it should do.
        """
    
        return ChatPromptTemplate.from_messages([
            ("system", "You are a researcher. Given the conversation below, dig up relevant facts or decide which tool to call."),
            MessagesPlaceholder(variable_name="messages"),
            ("system", "If you choose to call a tool, do so; otherwise, provide your findings in markdown text."),
        ])
