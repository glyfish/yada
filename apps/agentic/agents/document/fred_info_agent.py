from pydantic import BaseModel, Field

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool

from functools import lru_cache

from pathlib import Path

from apps.agentic.core.agents.tool_agent import ToolAgent
from apps.agentic.core.constants import GITHUB_LOCAL_PATH, DB_PATH
from apps.agentic.core.document_loaders.research_library_document_loader import (
    ResearchLibraryChromaDocumentLoader,
)
from apps.agentic.core.document_loaders.document_library_loader import (
    DocumentLibraryLoader,
)

from lib.logger import get_logger

logger = get_logger("YADA")

class FredInfoAgent(ToolAgent):
    """
    Handle requests for information about FRED time series data.
    """

    def __init__(self):
        tools = [
        ]
        tool_node_name = "fred_info_tool_node"

        super().__init__(tools, tool_node_name)

    
    def create_prompt(self):
        """
        Create the prompt template for the FRED agent.
        """
    
        system_prompt = """
        You are an expert in retrieving information about the from the FRED document store which
        contains indexed Markdown files with descriptions of time series data from the FRED 
        (Federal Reserve Economic Data) website.:
        - 
        - Summarize metadata for research notes, including filename, title, author, topic, and shelf.
        - Filter research note titles using author/topic/shelf metadata.
        - Summarize metadata for PDF documents, including filename, title, authors, published date, topic, and shelf.
        - Filter PDF document titles using author/topic/shelf metadata.
        Call the appropriate tool when the user asks about any of these data sources.
        """

        logger.debug(f"DocumentInfoAgent Agent prompt: {system_prompt}")

        return ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
            ("system", "If you choose to call a tool, do so; otherwise, provide your findings in plain text."),
        ])
