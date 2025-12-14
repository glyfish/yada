import os
import re, bisect
from pathlib import Path
import aiofiles

from lib.logger import get_logger
from git import Repo

from langchain.text_splitter import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
from langchain_core.documents import Document

from apps.agentic.core.document_loaders.chroma_document_loader import ChromaDocumentLoader
from apps.agentic.core.constants import (RESEARCH_LIBRARY_COLLECTION_NAME, RESEARCH_LIBRARY_DB_NAME, 
                                         RESEARCH_LIBRARY_LOCAL_PATH, DB_PATH)

from lib.utils import get_param_throw_if_missing

logger = get_logger("YADA")


class ResearchLibraryChromaDocumentLoader(ChromaDocumentLoader):
    """
    Document loader for Research Library files stored as **Markdown** only. The documents are split
    by H2 headers and then further split into smaller chunks for embedding.

    Metadata added to each document
    ------------------------------
    - filename: Base name of the file
    - path: File path relative to the research notes root
    - title: Title of the research document.
    - authors: Authors of the research document
    - date: Published date of the research document
    - topic: Topic of the research document
    - shelf: Tag used to identify document groups
    - ext: File extension
    - images: Comma-separated list of image URLs in the document (if any)
    - h2: Section titles (from H2 headers)
    - section: Section number (1-based) within the document
    - section_char_offset: Character offset within the section
    """

    def __init__(self, db_path=DB_PATH):
        super().__init__(RESEARCH_LIBRARY_DB_NAME, RESEARCH_LIBRARY_COLLECTION_NAME, db_path)
    

    async def load_document(self, path: str, **kwargs):
        """
        Load a **Markdown** research document into the ChromaDB collection.
        """

        meta_data = get_param_throw_if_missing("meta_data", **kwargs)
        filename = meta_data["filename"]
        logger.info(f"Loading research document from {path}.")

        async with aiofiles.open(path, "r", encoding="utf-8", errors="ignore") as f:
            md = await f.read()

        starts = _page_starts_from_h2(md)
        ext = (Path(filename).suffix or "").lower()
        if ext and ext not in (".md", ".markdown"):
            logger.warning(f"Expected Markdown file, got '{ext}'; proceeding as Markdown.")
        title = meta_data.get("title") or Path(filename).stem

        base_meta = {
            **meta_data,
            "ext": ext or ".md",
            "images": "",
            "section": None,
            "section_char_offset": None,
            "_global_start": None,
            "shelf": meta_data.get("shelf") or meta_data.get("tags") or "",
        }

        try:
            header_splitter = MarkdownHeaderTextSplitter(
                headers_to_split_on=[("#", "h1"), ("##", "h2"), ("###", "h3")]
            )
            header_docs = header_splitter.split_text(md)
        except Exception:
            header_docs = [Document(page_content=md, metadata=base_meta)]

        # Size-based split per section
        length_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1500, chunk_overlap=200, add_start_index=True
        )

        cursor = 0
        for d in header_docs:
            d.metadata = d.metadata or {}
            # small, stable prefix to locate the section in the FULL md
            prefix = d.page_content.lstrip()[:200]
            idx = md.find(prefix, cursor)
            if idx == -1:
                # fallback: search from beginning (handles repeated headings)
                idx = md.find(prefix)
                if idx == -1:
                    idx = cursor  # last resort to keep monotonicity
            d.metadata["_global_start"] = idx
            cursor = max(cursor, idx) + len(prefix)

        chunks = []
        for d in header_docs:
            sec_meta = {**base_meta, **(d.metadata or {})}
            parts = length_splitter.split_documents(
                [Document(page_content=d.page_content, metadata=sec_meta)]
            )

            base = int(sec_meta.get("_global_start", 0))
            for ch in parts:
                local = int(ch.metadata.get("start_index", 0))
                global_pos = base + local
                section_num, offset = _page_of(global_pos, starts)
                ch.metadata["section"] = section_num
                ch.metadata["section_char_offset"] = offset
                ch.metadata.pop("_global_start", None)
            
            chunks.extend(parts)

        if not chunks:
            logger.warning(f"No content extracted from {filename}; skipping.")
            return

        BATCH = 64
        for i in range(0, len(chunks), BATCH):
            self.vectorstore.add_documents(chunks[i:i + BATCH])

        logger.info(
            f"Loaded research document into collection {self.collection_name}: '{title}' with {len(chunks)} chunks."
        )

        logger.info(f"Loaded research document: {meta_data['title']}.")


    async def load_all_documents(self, base_path: str, **kwargs):
        pass


_H2_RX = re.compile(r"(?m)^##\s+")

def _page_starts_from_h2(text: str) -> list[int]:
    """Return sorted char offsets where pages start: 0 and every H2 line."""
    starts = [0]
    starts.extend(m.start() for m in _H2_RX.finditer(text))
    # unique + sorted
    return sorted(set(starts))

def _page_of(pos: int, starts: list[int]) -> tuple[int, int]:
    """
    Given a GLOBAL char position, return (page_num, page_char_offset).
    page_num is 1-based. offset is chars from the page start.
    """
    i = bisect.bisect_right(starts, pos) - 1
    start_char = starts[i] if i >= 0 else 0
    return i + 1, pos - start_char
