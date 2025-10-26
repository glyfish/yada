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
from apps.agentic.core.document_loaders.document_library_loader import DocumentLibraryLoader
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

        super().__init__(tool_name, tool_description, document_prompt, DocumentLibraryLoader(), query)


    def read_file(self, top_files):
        """
        Reconstruct and return the full file contents of the **top** retrieved PDF
        by pulling all of its chunks from the Chroma collection and ordering them.

        Ordering preference:
          1) If 'page' is present in metadata -> sort by page (int) then stable index
          2) Else if ('section','section_char_offset') -> (section, section_char_offset)
          3) Else if 'start_index' -> start_index
          4) Else preserve retrieval order

        Returns a markdown string that includes a small metadata header and a
        fenced block containing the reconstructed text. If nothing can be found,
        returns an empty string.
        """
        try:
            if not top_files:
                return ""

            # Use the first unique file/path from the top hits
            top = top_files[0]
            md0 = top.metadata or {}
            path = md0.get("path")
            filename = md0.get("filename")

            vs = self.doc_loader.vectorstore
            coll = getattr(vs, "_collection", None)
            if coll is None:
                return ""

            where = {"path": str(path)} if path else ({"filename": str(filename)} if filename else None)
            if not where:
                return ""

            # Pull all chunks for the file
            try:
                res = coll.get(where=where, include=["documents", "metadatas"], limit=100_000, offset=0)
            except Exception as e:
                logger.error(f"Error fetching full file from collection: {e}")
                return ""

            docs = res.get("documents") or []
            metas = res.get("metadatas") or []
            if not docs:
                return ""

            # Build sortable tuples
            items = []
            any_page = False
            any_section = False
            for i, (txt, md) in enumerate(zip(docs, metas)):
                txt = txt or ""
                m = md or {}
                page = m.get("page")
                section = m.get("section")
                sec_off = m.get("section_char_offset") or 0
                start_ix = m.get("start_index") or 0
                if page is not None:
                    any_page = True
                    try:
                        page = int(page)
                    except Exception:
                        page = 0
                    items.append(((0, page, i), txt, m))
                elif section is not None:
                    any_section = True
                    try:
                        sec_off = int(sec_off)
                    except Exception:
                        sec_off = 0
                    items.append(((1, str(section), sec_off, i), txt, m))
                elif start_ix is not None:
                    try:
                        start_ix = int(start_ix)
                    except Exception:
                        start_ix = i
                    items.append(((2, start_ix, i), txt, m))
                else:
                    items.append(((3, i), txt, m))

            items.sort(key=lambda t: t[0])

            # Compose output with simple page/section dividers
            out_parts = []
            header_bits = []
            title = md0.get("title") or ""
            authors = md0.get("authors") or ""
            published = md0.get("published_date") or ""
            topic = md0.get("topic") or ""
            tags = md0.get("tags") or ""

            header_bits.append(f"**File:** {filename or path or '(unknown)'}")
            if path:
                header_bits.append(f"**Path:** {path}")
            if title:
                header_bits.append(f"**Title:** {title}")
            if authors:
                header_bits.append(f"**Authors:** {authors}")
            if published:
                header_bits.append(f"**Published:** {published}")
            if topic:
                header_bits.append(f"**Topic:** {topic}")
            if tags:
                header_bits.append(f"**Tags:** {tags}")

            header = "\n".join(header_bits)

            current_marker = None
            for key, txt, m in items:
                if any_page:
                    marker = f"Page {key[1]}"  # key = (0, page, i)
                elif any_section:
                    marker = str(m.get("section") or "")
                else:
                    marker = None

                if marker and marker != current_marker:
                    out_parts.append(f"\n\n--- {marker} ---\n\n")
                    current_marker = marker
                out_parts.append(txt)

            body = "".join(out_parts).strip()

            if not body:
                return ""

            # Wrap in a fenced block so it renders monospaced without mangling math
            out = [
                "\n\n-----\n\n",
                header,
                "\n\n",
                "```text\n",
                body,
                "\n```\n"
            ]
            return "".join(out)

        except Exception as e:
            logger.error(f"read_file failed: {e}")
            return ""
