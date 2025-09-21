import os
from pathlib import Path
import aiofiles

from lib.logger import get_logger
from git import Repo

from langchain.text_splitter import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
from langchain_core.documents import Document

from apps.agentic.core.chroma_document_loader import ChromaDocumentLoader
from apps.agentic.core.constants import (RESEARCH_NOTES_COLLECTION_NAME, RESEARCH_NOTES_DB_NAME, 
                                         RESEARCH_NOTES_LOCAL_PATH)
logger = get_logger("YADA")


class ResearchNoteChromaDocumentLoader(ChromaDocumentLoader):
    """
    Loader for Research Note files stored as **Markdown** only.
    - Keeps TeX delimiters ($...$, $$...$$) in text for math-friendly embeddings.
    - Splits by Markdown headings first, then by length with overlap.
    - Batches inserts into the Chroma vector store.
    """

    def __init__(self, meta_data: dict):
        super().__init__(RESEARCH_NOTES_DB_NAME, RESEARCH_NOTES_COLLECTION_NAME, ".db")
        self._meta_data = meta_data


    @property
    def meta_data(self):
        """
        Get the metadata for the research note.
        """

        return self._meta_data

    
    async def load_document(self, path: str):
        """
        Load a **Markdown** research note into the ChromaDB collection.
        """

        filename = self.meta_data["filename"]
        note_path = os.path.join(RESEARCH_NOTES_LOCAL_PATH, filename)
        logger.info(f"Loading research note from {note_path}.")

        async with aiofiles.open(note_path, "r", encoding="utf-8", errors="ignore") as f:
            md = await f.read()

        ext = (Path(filename).suffix or "").lower()
        if ext and ext not in (".md", ".markdown"):
            logger.warning(f"Expected Markdown file, got '{ext}'; proceeding as Markdown.")
        title = self.meta_data.get("title") or Path(filename).stem

        base_meta = {
            **self.meta_data,
            "path": filename,
            "ext": ext or ".md",
            "source": "research_notes",
            "format": "md",
            "images": [],
            "md_localized": None,
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

        chunks = []
        for d in header_docs:
            sec_meta = {**base_meta, **(d.metadata or {})}
            chunks.extend(
                length_splitter.split_documents(
                    [Document(page_content=d.page_content, metadata=sec_meta)]
                )
            )

        if not chunks:
            logger.warning(f"No content extracted from {filename}; skipping.")
            return

        BATCH = 64
        for i in range(0, len(chunks), BATCH):
            self.vectorstore.add_documents(chunks[i:i + BATCH])

        logger.info(
            f"Loaded research note into collection {self.collection_name}: '{title}' with {len(chunks)} chunks."
        )

        logger.info(f"Loaded research note: {self.meta_data['title']}.")


    async def load_all_documents(self, path: str):
        pass
