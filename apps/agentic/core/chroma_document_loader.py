import os
import sys
import numpy

from lib.logger import get_logger

import chromadb
from langchain_community.document_loaders import GitLoader

logger = get_logger("YADA")

class ChromaDocumentLoader:

    def __init__(self, db_name: str, collection_name: str):
        self.__db_name = db_name
        self.__collection_name = collection_name
        self.__db_path = os.path.join(".db", db_name)

        self.__chroma_client = chromadb.PersistentClient(path=self.__db_path)
        self.__chroma_collection = self.__chroma_client.get_or_create_collection(self.__collection_name)


    @property
    def db_name(self):
        """
        Get the name of the ChromaDB database.
        """

        return self.__db_name
    
    
    @property
    def collection_name(self):
        """
        Get the name of the collection in the ChromaDB.
        """

        return self.__collection_name


    @property
    def db_path(self):
        """
        Get the database path.
        """

        return self.__db_path
    

    @property
    def chroma_client(self):
        """
        Get the ChromaDB client instance.
        """

        return self.__chroma_client
    

    @property
    def chroma_collection(self):
        """
        Get the ChromaDB collection instance.
        """

        return self.__chroma_collection
    

    async def load_github_documents(self, base_path: str = ".repos"):
        """
        Load documents into the ChromaDB collection.
        """

        for acct in os.listdir(base_path):
            acct_path = os.path.join(base_path, acct)

            if not os.path.isdir(acct):
                continue

            for repo in os.listdir(acct_path):
                repo_path = os.path.join(acct_path, repo)
                if os.path.isdir(os.path.join(repo_path, ".git")):
                    await self.load_github_repo(repo_path)


    async def load_github_repo(self, path: str):
        """
        Load the GitHub repositories into the ChromaDB collection.
        """

        loader = GitLoader(
            repo_name=path,
            token=os.environ.get("GITHUB_API_KEY")
        )

        documents = await loader.aload()
        self.chroma_collection.add_documents(documents)
        logger.info(f"Loaded {len(documents)} documents from {path} into ChromaDB collection {self.collection_name}.")    