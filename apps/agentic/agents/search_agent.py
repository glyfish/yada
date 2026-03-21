from langchain_tavily import TavilySearch
from langgraph.graph import StateGraph, START, END
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.prebuilt import ToolNode

from apps.agentic.core.agents.react_agent import ReactAgent
from langchain_core.tools import BaseTool

class SearchAgent(ReactAgent):
    """
    Search Agent that uses a language model to research and find relevant information.
    It can call tools like TavilySearchResults to fetch search results.
    """

    def __init__(self):
        tools: list[BaseTool] = [TavilySearch()]
        tool_node_name = "tavily_search_tool_node"

        super().__init__(tools, tool_node_name)
    

    def create_prompt(self):
        """
        Create the prompt template for the researcher agent.
        This defines how the model should interpret the messages and what it should do.
        """
    
        return ChatPromptTemplate.from_messages([
            ("system", "You are a researcher. Given the conversation below, dig up relevant facts or decide which tool to call."),
            MessagesPlaceholder(variable_name="messages"),
        ])
