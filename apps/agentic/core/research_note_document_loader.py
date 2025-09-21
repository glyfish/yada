import os
from datetime import timezone
import aiofiles

from lib.logger import get_logger
from git import Repo

from langchain_community.document_loaders import GitLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from apps.agentic.core.chroma_document_loader import ChromaDocumentLoader
from apps.agentic.core.constants import (RESEARCH_NOTES_COLLECTION_NAME, RESEARCH_NOTES_DB_NAME)
logger = get_logger("YADA")


class ResearchNoteChromaDocumentLoader(ChromaDocumentLoader):

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
        Load the research notes into the ChromaDB collection.
        """

        note_path = os.path.join(path, self.meta_data["file_name"])
        logger.info(f"Loading research note from {note_path}.")

        async with aiofiles.open(note_path, "r", encoding="utf-8") as f:
           content = await f.read()

        document = Document(page_content=content, metadata=self.meta_data)
        self.vectorstore.add_documents([document])

        logger.info(f"Loaded research note: {self.meta_data['title']}.")
