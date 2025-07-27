import os
import sys
import numpy

from lib.logger import get_logger

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import GitLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from apps.agentic.core.utils import load_api_key
import tiktoken

logger = get_logger("YADA")

def num_tokens(text):
    encoding = tiktoken.encoding_for_model("text-embedding-ada-002")
    return len(encoding.encode(text))


class ChromaDocumentLoader:

    def __init__(self, db_name: str, collection_name: str):
        self.__db_name = db_name
        self.__collection_name = collection_name
        self.__db_path = os.path.join(".db", db_name)
        self.__embedding_function = OpenAIEmbeddings()

        self.__vectorstore = Chroma(
            collection_name=self.__collection_name,
            persist_directory=self.__db_path,
            embedding_function=self.__embedding_function
        )


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
    def vectorstore(self):
        """
        Get the ChromaDB client instance.
        """

        return self.__vectorstore
        

    async def load_github_documents(self, base_path: str = ".repos"):
        """
        Load documents into the ChromaDB collection.
        """

        logger.info(f"Updating github document store from {base_path}.")

        for acct in os.listdir(base_path):
            acct_path = os.path.join(base_path, acct)   
            logger.info(f"Updating github documents in {acct} from {acct_path}.")

            if not os.path.isdir(acct_path):
                continue

            for repo in os.listdir(acct_path):
                repo_path = os.path.join(acct_path, repo)
                logger.info(f"Updating github documents in {repo} from {repo_path}.")
                if os.path.isdir(os.path.join(repo_path, ".git")):
                    await self.load_github_repo(repo_path)


    async def load_github_repo(self, path: str):
        """
        Load the GitHub repositories into the ChromaDB collection.
        """

        loader = GitLoader(
            repo_path=path,
            branch="master"
        )

        documents = await loader.aload()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1028,
            chunk_overlap=200
        )

        all_chunked = []
        for doc in documents:
            all_chunked.extend(splitter.split_documents([doc]))

        max_tokens = 0
        total_tokens = 0
        for _, doc in enumerate(all_chunked):
            ntokens = num_tokens(doc.page_content)
            max_tokens = max(max_tokens, ntokens)
            total_tokens += ntokens

        logger.info(f"Loaded {len(documents)} documents from {path} into ChromaDB collection {self.collection_name}, " \
                    f"max chunk tokens: {max_tokens}, total tokens: {total_tokens}, number of chunks: {len(all_chunked)}.")
        
        nchunks = len(all_chunked)
        batche_size = 
        

        self.vectorstore.add_documents(all_chunked)
        