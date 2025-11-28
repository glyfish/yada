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
from apps.agentic.core.document_loaders.research_library_document_loader import ResearchLibraryChromaDocumentLoader
from lib.logger import get_logger

logger = get_logger("YADA")


class ResearchLibraryAgent(ChromaRAGAgent):
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

    Example Queries:
    - title: Thermodynamics Look in my research notes for the definition of a Carnot Cycle.

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

        super().__init__(tool_name, tool_description, document_prompt, ResearchLibraryChromaDocumentLoader(), query)


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

        # Stitch a window of chunks around the retrieved hit
        def _section_and_offset(meta):
            sec = _safe_int(meta.get("section"), 1)
            off = _safe_int(meta.get("section_char_offset"))
            if off is None:
                off = _safe_int(meta.get("start_index"), 0)
            return sec if sec is not None else 1, off if off is not None else 0

        context_window = 1  # number of chunks before/after the target chunk
        items: list[tuple[str, dict]] = []
        coll = getattr(self.doc_loader.vectorstore, "_collection", None)
        if coll is not None:
            try:
                res = coll.get(
                    where={"path": path},
                    include=["metadatas", "documents"],
                    limit=100_000,
                )
                docs = res.get("documents") or []
                metas = res.get("metadatas") or []
                items = list(zip(docs, metas))
            except Exception as exc:
                logger.warning("Failed to fetch chunks for %s: %s", path, exc)

        # Fallback to the already retrieved top_files if collection fetch failed
        if not items:
            same_path = [d for d in top_files if (d.metadata or {}).get("path") == path]
            if not same_path:
                return ""
            items = [(d.page_content or "", d.metadata or {}) for d in same_path]

        items.sort(key=lambda pair: _section_and_offset(pair[1]))

        target_section = _safe_int(md0.get("section"))
        target_offset = _safe_int(md0.get("section_char_offset"))
        if target_offset is None:
            target_offset = _safe_int(md0.get("start_index"))

        pivot_idx = 0
        if target_section is not None:
            best_idx = None
            best_score = None
            for idx, (_doc, meta) in enumerate(items):
                sec, off = _section_and_offset(meta)
                if sec != target_section:
                    continue
                if target_offset is None:
                    best_idx = idx
                    break
                diff = abs(off - target_offset)
                if best_score is None or diff < best_score:
                    best_idx = idx
                    best_score = diff
            if best_idx is not None:
                pivot_idx = best_idx

        start = max(0, pivot_idx - context_window)
        end = min(len(items), pivot_idx + context_window + 1)
        window_items = items[start:end]

        out_parts = []
        current_sec = None
        for doc, meta in window_items:
            sec, _ = _section_and_offset(meta)
            if current_sec != sec:
                current_sec = sec
                h2 = meta.get("h2")
                if h2:
                    out_parts.append(f"\n\n## {h2}\n\n")
            out_parts.append(doc or "")

        full_text = "".join(out_parts)
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
        if ext in (".md", ".markdown"):
            body = full_text
        else:
            fence_lang = lang if lang else ""
            body = f"```{fence_lang}\n{full_text}\n```"

        final = header + body
        final = self._clamp_markdown(final, max_chars=20_000) 
        return final


    def _clamp_markdown(self, md: str, max_chars: int = 60_000) -> str:
        """Truncate markdown to ~max_chars at a sane boundary.
        - prefers blank-line break before the budget
        - avoids breaking code fences / $$ blocks (closes them if needed)
        - appends a short notice
        """
        if not md or len(md) <= max_chars:
            return md or ""

        cut = max_chars

        # Prefer to cut at a blank-line boundary somewhat before the budget
        boundary = md.rfind("\n\n", 0, max(0, max_chars - 2000))
        if boundary > 0:
            cut = boundary
        else:
            # fallback: single newline before budget
            nl = md.rfind("\n", 0, max_chars)
            if nl > 0:
                cut = nl

        chunk = md[:cut].rstrip()

        # Keep rendering well-formed: balance code fences and $$ math if we cut inside one
        # Code fences
        if chunk.count("```") % 2 != 0:
            # attempt to cut before the last opening fence
            last_fence = chunk.rfind("```")
            if last_fence > 0:
                chunk = chunk[:last_fence].rstrip()
            else:
                # or just close it cleanly
                chunk += "\n```"

        # Display math $$ … $$
        if chunk.count("$$") % 2 != 0:
            # try to cut before last $$
            last_dd = chunk.rfind("$$")
            if last_dd > 0:
                chunk = chunk[:last_dd].rstrip()
            else:
                chunk += "\n$$"

        chunk += (
            "\n\n---\n"
            "_Note: truncated for display. Use filters (e.g., `section:` / `pages:` / `before:` / `after:`) "
            "to narrow the result, or open the file to see more._\n"
        )
        return chunk


def _safe_int(value, default=None):
    try:
        return int(value)
    except Exception:
        return default
