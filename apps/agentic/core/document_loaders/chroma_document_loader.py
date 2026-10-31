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

from apps.agentic.core.constants import (DB_PATH)
from apps.agentic.db import vocabulary_builder
from apps.agentic.db.vocabulary import Vocabulary
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

        Does **not** refresh the vocabulary, and must not: every caller is the delete
        half of a replace (`research_library_document_loader.load_document`,
        `github_document_loader._delete_repo`), so refreshing here would rebuild from a
        store with the old document removed and the new one not yet written -- a
        vocabulary momentarily describing neither. The public `load_*` entry points
        refresh once, after the write. A standalone delete, if one is ever added, has to
        call `refresh_vocabulary` itself.

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


    def refresh_vocabulary(self) -> None:
        """
        Rebuild this store's vocabulary, after a write. Every write path must call this.

        The vocabulary in Postgres is a *snapshot* of this store's Chroma metadata, and
        the MCP tools resolve filters against the snapshot rather than against Chroma.
        A write that does not refresh it leaves the two disagreeing in the one direction
        that cannot be noticed from outside: a value that now exists resolves as "no
        such value", reported authoritatively and with a facet listing to prove it. The
        content stays findable by unfiltered search, so nothing errors -- which is what
        makes it worse than a break. So the refresh belongs with the write rather than
        with whoever remembers to call it, and that is why this is here and not in the
        loader agent's tools: a notebook and a script write through the same methods.

        Stores outside the vocabulary are skipped, not treated as an error -- `fred` and
        `etf` are bound for Postgres with the time-series work and never get rows here.

        A failed rebuild is logged, not raised. The documents are already in Chroma by
        this point, so raising would report a failed load for a load that succeeded --
        the same class of wrong answer, pointed the other way. `is_stale` is the
        backstop for the gap this leaves.
        """
        if self._db_name not in vocabulary_builder.STORE_FIELDS:
            return
        try:
            Vocabulary.ensure_initialized()
            counts = vocabulary_builder.rebuild(self._db_name)
        except Exception:
            logger.exception(
                f"Could not rebuild the {self._db_name} vocabulary after a write. The "
                f"store is now AHEAD of its vocabulary: filters will deny values that "
                f"exist until a rebuild runs."
            )
            return
        logger.info(
            f"Refreshed the {self._db_name} vocabulary: {counts['combinations']} "
            f"combinations over {counts['chunks']:,} chunks."
        )


    @staticmethod
    def num_tokens(text):
        encoding = tiktoken.encoding_for_model("text-embedding-ada-002")
        return len(encoding.encode(text))


    @abstractmethod
    async def load_all_documents(self, **kwargs):
        """
        Load all documents into the ChromaDB collection.
        Subclasses declare whatever parameters their loading strategy requires.
        """

        raise NotImplementedError("Subclasses must implement the load_all_documents method to read files.")


    @abstractmethod
    async def load_document(self, path: str, **kwargs):
        """
        Load document from path into the ChromaDB collection.
        """

        raise NotImplementedError("Subclasses must implement the load_all_documents method to read files.")
