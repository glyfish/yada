from abc import ABC, abstractmethod
from typing import Annotated, Literal, Sequence
from pathlib import Path

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

from apps.agentic.core.constants import GITHUB_DB_NAME, GITHUB_COLLECTION_NAME, GITHUB_LOCAL_PATH
from apps.agentic.core.chroma_rag_agent import ChromaRAGAgent
from lib.logger import get_logger

logger = get_logger("YADA")


class ResearchNoteAgent(ChromaRAGAgent):

    def __init__(self, query):
        tool_name = "github_agent_tool"
        tool_description = (
            "Troy Stribling Research Note Retriever"
            "Description: Search and retrieve content from Troy Stribling’s research notes "
            "indexed in the vector store. "
            "The vector store contains research notes stored as HTML files. " 
            "Use this for any query about 'my research', 'my notes', or requests for specific files/functions."
        )

        prompt_template = (
            "You are searching Troy Stribling’s research notes in his indexed GitHub repositories.vector store to answer "
            "requests about his research. Information about the note can be found in the metadata attached to each file. "
            "Following is a description of the metadata."
            "- title: {metadata[title]}"
            "- start_date: {metadata[start_date]}"
            "- subject: {metadata[subject]}"
            "- File path: {metadata[path]}"
            "---"
            "{page_content}"
        )
        document_prompt = PromptTemplate.from_template(template=prompt_template)

        super().__init__(tool_name, tool_description, document_prompt, GITHUB_DB_NAME, GITHUB_COLLECTION_NAME, query)


    def read_file(self, top_files):
        pass