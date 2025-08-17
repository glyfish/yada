from abc import ABC, abstractmethod
from typing import Annotated, Literal, Sequence

from pydantic import BaseModel, Field
from typing import Dict

from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langgraph.prebuilt import tools_condition
from langchain.tools.retriever import create_retriever_tool
from langgraph.prebuilt import ToolNode

from apps.agentic.core.chroma_document_loader import ChromaDocumentLoader
from apps.agentic.core.messages import WorkerState
from apps.agentic.core.utils import build_llm
from apps.agentic.core.constants import GITHUB_DB_NAME, GITHUB_COLLECTION_NAME
from apps.agentic.core.chroma_rag_agent import ChromaRAGAgent
from lib.logger import get_logger

logger = get_logger("YADA")


class DocumentGrade(BaseModel):
    """Binary score for relevance check."""
    binary_score: str = Field(description="Relevance score 'yes' or 'no'")


class CodeRepoAgent(ChromaRAGAgent):

    def __init__(self):
        tool_name = "github_agent_tool"
        tool_description = """
                           Search and retrieve information about Troy Stribling's (who can be referred to a me) 
                           computer software GitHub repositories. The code base is well documented and organized
                           and written in over a dozen of programming languages. The applications include web
                           development, messaging, cryptocurrencies, data analysis, and machine learning focused on
                           finance.
                           """
        
        super().__init__(tool_name, tool_description, GITHUB_DB_NAME, GITHUB_COLLECTION_NAME)
