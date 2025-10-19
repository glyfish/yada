import os
import re, bisect
from pathlib import Path
from datetime import datetime, timezone
import aiofiles

from lib.logger import get_logger
from git import Repo

from langchain.text_splitter import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader

from apps.agentic.core.document_loaders.chroma_document_loader import ChromaDocumentLoader
from apps.agentic.core.constants import (RESEARCH_NOTES_COLLECTION_NAME, RESEARCH_NOTES_DB_NAME, 
                                         RESEARCH_NOTES_LOCAL_PATH, DB_PATH)

from lib.utils import get_param_throw_if_missing

logger = get_logger("YADA")


class DocumentLibraryLoader(ChromaDocumentLoader):
    """
    Document loader for PDF files. The documents are split
    by H2 headers and then further split into smaller chunks for embedding.

    Metadata added to each document
    ------------------------------
    - filename: Base name of the file
    - path: File path relative to the research notes root
    - title: Title of the research note.
    - author: Author of the research note
    - start_date: Start date of the research note
    - topic: Topic of the research note
    - tags: Comma-separated list of tags associated with the research note
    """

    def __init__(self, db_path=DB_PATH):
        super().__init__(RESEARCH_NOTES_DB_NAME, RESEARCH_NOTES_COLLECTION_NAME, db_path)
    

    async def load_document(self, path: str, **kwargs):
        """
        Load a PDF document into the ChromaDB collection.

        Expected kwargs:
          - meta_data: dict with keys {filename, path, title, authors, published_date, topic, tags}
            authors may be a list[str] or comma-separated string. tags may be list[str] or comma-separated string.
        """
        # Resolve and validate path
        file_path = Path(path)
        if not file_path.exists() or not file_path.is_file():
            logger.error(f"PDF path not found or not a file: {file_path}")
            return
        if file_path.suffix.lower() != ".pdf":
            logger.error(f"Not a PDF file: {file_path}")
            return

        meta = kwargs.get("meta_data", {}) or {}

        # Normalize scalar metadata values for Chroma (no lists allowed)
        def _to_scalar(val):
            if val is None:
                return ""
            if isinstance(val, (int, float, bool)):
                return val
            if isinstance(val, (list, tuple, set)):
                return ",".join([str(x) for x in val if str(x)])
            return str(val)

        filename = meta.get("filename") or file_path.name
        title = meta.get("title") or file_path.stem
        authors = _to_scalar(meta.get("authors"))
        published_date = _to_scalar(meta.get("published_date"))
        topic = _to_scalar(meta.get("topic"))
        tags = _to_scalar(meta.get("tags"))

        # Optional numeric timestamp for filtering
        published_date_unix = None
        try:
            if meta.get("published_date"):
                # Accept YYYY-MM-DD or ISO formats
                dt = datetime.fromisoformat(str(meta.get("published_date")))
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                published_date_unix = int(dt.timestamp())
        except Exception:
            published_date_unix = None

        # Load pages with LangChain's PyPDFLoader (one Document per page)
        try:
            loader = PyPDFLoader(str(file_path))
            page_docs = loader.load()
        except Exception as e:
            logger.exception(f"Failed to load PDF with PyPDFLoader: {file_path}: {e}")
            return

        if not page_docs:
            logger.warning(f"No pages extracted from PDF: {file_path}")
            return

        # Split each page into chunks for embedding
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1200,
            chunk_overlap=150,
            separators=["\n\n", "\n", " ", ""]
        )

        documents = []
        for pdoc in page_docs:
            page_num = int(pdoc.metadata.get("page", 0)) + 1  # 1-based
            page_text = pdoc.page_content or ""
            if not page_text.strip():
                continue
            chunks = splitter.split_text(page_text)

            for idx, chunk in enumerate(chunks):
                md = {
                    "filename": filename,
                    "path": str(meta.get("path") or file_path),
                    "ext": ".pdf",
                    "title": title,
                    "authors": authors,
                    "published_date": published_date,
                    "published_date_unix": published_date_unix if published_date_unix is not None else None,
                    "topic": topic,
                    "tags": tags,
                    "source": "pdf-library",
                    "page": page_num,
                    "section": f"Page {page_num}",
                }
                # Remove None values to avoid validator issues
                md = {k: v for k, v in md.items() if v is not None}
                documents.append(Document(page_content=chunk, metadata=md))

        if not documents:
            logger.warning(f"No text chunks produced from PDF: {file_path}")
            return

        # Upsert in batches
        BATCH = 100
        for i in range(0, len(documents), BATCH):
            batch = documents[i:i + BATCH]
            try:
                self.vectorstore.add_documents(batch)
            except Exception as e:
                logger.exception(f"Error upserting PDF chunks (batch {i}//{BATCH}) for {file_path}: {e}")
                # continue with next batch
                continue

        logger.info(f"Loaded PDF into vector store: {file_path} (pages={len(page_docs)}, chunks={len(documents)})")


    async def load_all_documents(self, path: str, **kwargs):
        root = Path(path)
        if not root.exists() or not root.is_dir():
            logger.error(f"PDF root does not exist or is not a directory: {root}")
            return

        for pdf_path in root.rglob("*.pdf"):
            meta = {
                "filename": pdf_path.name,
                "path": str(pdf_path),
                "title": pdf_path.stem,
                "authors": "",
                "published_date": "",
                "topic": "",
                "tags": "",
            }
            try:
                await self.load_document(str(pdf_path), meta_data=meta)
            except Exception as e:
                logger.exception(f"Failed to load PDF {pdf_path}: {e}")
                continue

