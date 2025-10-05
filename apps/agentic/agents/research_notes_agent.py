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

from apps.agentic.core.chroma_rag_agent import ChromaRAGAgent
from apps.agentic.core.research_note_document_loader import ResearchNoteChromaDocumentLoader
from lib.logger import get_logger

logger = get_logger("YADA")


class ResearchNoteAgent(ChromaRAGAgent):
    """
    Research Note Agent that uses a vector store index of research notes to answer questions about research topics.
    It is designed to handle queries related to research notes, topics, authors, dates, and tags.
    
    Query filters
    -------------
    The agent supports the following query filters to refine searches:
    - author: Author name (e.g., author:Troy Stribling)
    - topic: Research topic (e.g., topic:AI)
    - start_date: Start date of work on the research note (e.g., date:2023-01-01)
    - tag: Tag associated with the research note (e.g., tag:physics)
    - section: Section number within the research note (e.g., section:2)
    - section: Range of section within the research note (e.g., section:2-5)

    """

    def __init__(self, query):
        tool_name = "research_note_agent_tool"
        tool_description = (
            "Troy Stribling Research Note Retriever"
            "Description: Search and retrieve content from Troy Stribling’s research notes "
            "indexed in the vector store. The vector store contains research notes "
            "stored as Markdown files that cover a variety of topics. "
            "Use this for any query about 'my research', 'my notes', or requests for specific ."
        )

        prompt_template = (
            "You are searching Troy Stribling’s research notes in his indexed library vector store to answer "
            "requests about his research. Information about the note can be found in the metadata attached to each file. "
            "Following is a description of the metadata."
            "- Research Note filename: {metadata[filename]}"
            "- Research Note file path: {metadata[path]}"
            "- Research Note title: {metadata[title]}"
            "- Research Note start date: {metadata[start_date]}"
            "- Research Note author: {metadata[author]}"
            "- Research Note topic description: {metadata[topic]}"
            "- Research Note tags: {metadata[tags]}"
            "- File extension: {metadata[ext]}"
            "- Image URLs in the note: {metadata[images]}"
            "- h2 section titles: {metadata[h2]}"
            "- Section number: {metadata[section]}"
            "- Section character offset: {metadata[section_char_offset]}"
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

        d0 = top_files[0]
        md0 = (getattr(d0, "metadata", None) or {})
        path = md0.get("path") or md0.get("filename")
        if not path:
            return ""

        # Decide fenced code language
        ext = (md0.get("ext") or "").lower()
        if ext in (".md", ".markdown"):
            lang = "markdown"
        elif ext in (".html", ".htm"):
            lang = "html"
        else:
            lang = ""  # generic fence

        # Try to fetch all chunks for this file directly from the collection
        full_text = ""
        try:
            vs = self.doc_loader.vectorstore
            coll = getattr(vs, "_collection", None)
            if coll is None:
                raise RuntimeError("Chroma collection not accessible")

            res = coll.get(
                where={"path": path},                    # notes don’t include 'source' in your current metadata
                include=["metadatas", "documents"],
                limit=100_000,
            )
            docs = res.get("documents") or []
            metas = res.get("metadatas") or []

            items = list(zip(docs, metas))

            def _sort_key(item):
                _doc, m = item
                m = m or {}
                # section (1-based), default to 1 if missing
                try:
                    sec = int(m.get("section", 1))
                except Exception:
                    sec = 1
                # prefer section_char_offset; fallback to start_index; then 0
                off = m.get("section_char_offset")
                if off is None:
                    off = m.get("start_index") or 0
                try:
                    off = int(off)
                except Exception:
                    off = 0
                return (sec, off)

            items.sort(key=_sort_key)
            full_text = "".join((doc or "") for doc, _ in items)

        except Exception:
            # Fallback: stitch from the already-returned top_files if they share the same path
            same_path = [d for d in top_files if (d.metadata or {}).get("path") == path]
            def _tf_key(d):
                m = d.metadata or {}
                try:
                    sec = int(m.get("section", 1))
                except Exception:
                    sec = 1
                off = m.get("section_char_offset")
                if off is None:
                    off = m.get("start_index") or 0
                try:
                    off = int(off)
                except Exception:
                    off = 0
                return (sec, off)
            same_path.sort(key=_tf_key)
            full_text = "\n".join(d.page_content for d in same_path)

        if not full_text:
            return ""

        # Lightweight header with useful metadata
        title = md0.get("title") or path
        author = md0.get("author")
        start_date = md0.get("start_date")
        topic = md0.get("topic")

        header_lines = [ "# File", f"- {title} — {path}" ]
        if author:     header_lines.append(f"- Author: {author}")
        if start_date: header_lines.append(f"- Start: {start_date}")
        if topic:      header_lines.append(f"- Topic: {topic}")

        header = "\n\n-----\n\n" + "\n".join(header_lines) + "\n\n"
        fenced = f"```{lang}\n{full_text}\n```" if lang else f"```\n{full_text}\n```"
        return header + fenced