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

from apps.agentic.core.agents.chroma_rag_agent import ChromaRAGAgent
from apps.agentic.core.document_loaders.research_note_document_loader import ResearchNoteChromaDocumentLoader
from lib.logger import get_logger

logger = get_logger("YADA")


class DocumentLibraryAgent(ChromaRAGAgent):
    """
    PDF Document Agent that uses a vector store index of PDF documents to answer questions about document
    content. It is designed to handle queries related to PDF documents like: title, topic, authors, 
    published_date, and tags.

    Query filters
    -------------
    The agent supports the following query filters to refine searches:
    - authors: Author names (e.g., author:Troy Stribling)
    - topic: Research topic (e.g., topic:AI)
    - published_date: Start date of work on the research note (e.g., date:2023-01-01)
    - tag: Tag associated with the research note (e.g., tag:physics)
    """

    def __init__(self, query):
        tool_name = "research_note_agent_tool"
        tool_description = (
            "PDF Document Retriever"
            "Description: Search and retrieve content from the PDF document library which contains "
            "indexed PDF documents that cover a wide range of technical and research topics "
            "Use this for any query about 'document library', 'library' or 'PDF documents'."
        )

        prompt_template = (
            "You are searching the PDF document library in his indexed library vector store to answer "
            "requests about the contents of the documents. Information about the document can be found " 
            "in the metadata attached to each file."
            "Following is a description of the metadata."
            "- Document filename: {metadata[filename]}"
            "- Document file path: {metadata[path]}"
            "- Document title: {metadata[title]}"
            "- Document published date: {metadata[published_date]}"
            "- Document authors: {metadata[authors]}"
            "- Document topic description: {metadata[topic]}"
            "- Document tags: {metadata[tags]}"
            "---"
            "{page_content}"
        )
        document_prompt = PromptTemplate.from_template(template=prompt_template)

        super().__init__(tool_name, tool_description, document_prompt, ResearchNoteChromaDocumentLoader(), query)


    def read_file(self, top_files):
        """
        Reconstruct and return the full file contents of the top hit from the index.
        Orders chunks by (section, section_char_offset) with a fallback to start_index.
        Returns a markdown/HTML fenced block plus a small header with file metadata.
        """

        if not top_files:
            return ""

        return None
