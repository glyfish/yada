from abc import ABC, abstractmethod
from typing import Annotated, Literal, Sequence

from pydantic import BaseModel, Field
from typing import Dict

from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
from langchain.prompts import PromptTemplate
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
        tool_description = (
            "Troy Stribling Code Retriever"
            "Description: Search and retrieve content from Troy Stribling’s (the user’s) GitHub repositories "
            "indexed in the vector store (code, READMEs, docs, issues, commit messages). Use this for "
            "any query about 'my code', 'my repo(s)', or specific files/functions."
        )

        prompt_template = (
            "You are looking up Troy Stribling’s code (“my code”) in his indexed GitHub repositories.vector store "
            "Information about the code can be found in the metadata attached to each file. Following is a description of the metadata:"
            "The programming language should be deduced from the file extension."
            "- GitHub account: {metadata[account]}"
            "- Repository name: {metadata[repo]}"
            "- Git branch name: {metadata[branch]}"
            "- File path: {metadata[path]}"
            "- File extension: {metadata[ext]}"
            "- Programming language: {programming_language}"
            "- Latest Commit: {metadata[commit]}"
            "---"
            "{page_content}"
        )
        document_prompt = PromptTemplate.from_template(template=prompt_template)

        super().__init__(tool_name, tool_description, document_prompt, GITHUB_DB_NAME, GITHUB_COLLECTION_NAME)
