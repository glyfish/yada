import os
import sys
from tracemalloc import start
from matplotlib import text
import numpy
from datetime import timezone
import aiofiles
from abc import ABC, abstractmethod

from lib.logger import get_logger
from git import Repo

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import GitLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from apps.agentic.core.utils import load_api_key
from apps.agentic.core.constants import (GITHUB_LOCAL_PATH, GITHUB_EXCLUDED_REPOS, CHROMA_DB_MAX_BATCH_SIZE,
                                         RESEARCH_LIBRARY_LOCAL_PATH, DB_PATH)
import tiktoken

logger = get_logger("YADA")

def num_tokens(text):
    encoding = tiktoken.encoding_for_model("text-embedding-ada-002")
    return len(encoding.encode(text))


class ChromaDocumentLoader(ABC):

    def __init__(self, db_name: str, collection_name: str, db_path: str=DB_PATH):
        self._db_name = db_name
        self._collection_name = collection_name
        self._db_path = os.path.join(db_path, db_name)
        os.makedirs(self._db_path, exist_ok=True)
        self._embedding_function = OpenAIEmbeddings(
            embedding_ctx_length=2000,
            chunk_size=100
        )

        self._vectorstore = Chroma(
            collection_name=self._collection_name,
            persist_directory=self._db_path,
            embedding_function=self._embedding_function
        )


    @property
    def db_name(self):
        """
        Get the name of the ChromaDB database.
        """

        return self._db_name
    
    
    @property
    def collection_name(self):
        """
        Get the name of the collection in the ChromaDB.
        """

        return self._collection_name


    @property
    def db_path(self):
        """
        Get the database path.
        """

        return self._db_path
    

    @property
    def vectorstore(self):
        """
        Get the ChromaDB client instance.
        """

        return self._vectorstore
    

    def delete_document(self, filename: str) -> int:
        """
        Delete all chunks in the collection that match the given filename.

        Parameters
        ----------
        filename : str
            The filename metadata value to match. All chunks with
            ``metadata["filename"] == filename`` are deleted.

        Returns
        -------
        int
            Number of chunks deleted.
        """
        collection = getattr(self._vectorstore, "_collection", None)
        if collection is None:
            logger.warning("delete_document: vector store collection unavailable, skipping delete.")
            return 0

        result = collection.get(where={"filename": filename}, include=[])
        ids = result.get("ids") or []
        if ids:
            collection.delete(ids=ids)
            logger.info(
                f"delete_document: deleted {len(ids)} chunks for filename='{filename}' "
                f"from collection '{self._collection_name}'."
            )
        return len(ids)


    @staticmethod
    def num_tokens(text):
        encoding = tiktoken.encoding_for_model("text-embedding-ada-002")
        return len(encoding.encode(text))


    @abstractmethod
    async def load_all_documents(self, base_path: str, **kwargs):
        """
        load all of the documents from the base path.
        """

        raise NotImplementedError("Subclasses must implement the load_all_documents method to read files.")


    @abstractmethod
    async def load_document(self, path: str, **kwargs):
        """
        Load document from path into the ChromaDB collection.
        """

        raise NotImplementedError("Subclasses must implement the load_all_documents method to read files.")
