import os
import sys
from tracemalloc import start
import numpy

from lib.logger import get_logger
from git import Repo

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import GitLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from apps.agentic.core.utils import load_api_key
from apps.agentic.core.constants import GITHUB_LOCAL_PATH, GITHUB_EXCLUDED_REPOS, CHROMA_DB_MAX_BATCH_SIZE
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
        self.__embedding_function = OpenAIEmbeddings(
            embedding_ctx_length=2000,
            chunk_size=100
        )

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
        

    async def load_github_documents(self, base_path: str = GITHUB_LOCAL_PATH):
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
                
                if repo in GITHUB_EXCLUDED_REPOS:
                    logger.info(f"Skipping excluded repo {repo}.")
                    continue

                repo_path = os.path.join(acct_path, repo)
                logger.info(f"Updating github documents in {repo} from {repo_path}.")
                if os.path.isdir(os.path.join(repo_path, ".git")):
                    await self.load_github_repo(repo_path)

        logger.info(f"Finished updating github document store from {base_path}.")


    def get_default_branch(self, repo_path: str) -> str:
        repo = Repo(repo_path)
        # If HEAD is pointing to a branch, use that
        try:
            return repo.active_branch.name
        except TypeError:
            # Detached HEAD? fall back to reading origin/HEAD
            remote_head = repo.remotes.origin.refs.HEAD
            return remote_head.reference.name.split("/")[-1]


    def latest_commit_for(self, repo, rel_path: str) -> str | None:
        try:
            c = next(repo.iter_commits(paths=rel_path, max_count=1))
            return c.hexsha[:12]
        except StopIteration:
            return None


    async def load_github_repo(self, path: str):
        """
        Load the GitHub repositories into the ChromaDB collection.
        """

        branch = self.get_default_branch(path)        
        logger.info(f"Setting default branch {branch} for {path}.")        
        loader = GitLoader(repo_path=path, branch=branch)

        documents = await loader.aload()

        repo = Repo(path)
        repo_root = os.path.realpath(repo.working_tree_dir)

        account = os.path.basename(os.path.dirname(path.rstrip("/")))
        repo_name = os.path.basename(path.rstrip("/"))

        for d in documents:
            src = d.metadata.get("source")  # absolute path from GitLoader
            if not src:
                rel = None
            else:
                src_real = os.path.realpath(src)
                # only compute rel if file is inside the repo root
                if src_real.startswith(repo_root + os.sep) or src_real == repo_root:
                    rel = os.path.relpath(src_real, start=repo_root)
                else:
                    logger.warning(f"Skipping commit lookup for out-of-repo file: {src_real}")
                    rel = None

            d.metadata.update({
                "account": account,
                "repo": repo_name,
                "branch": branch,
                "path": rel,
                "filename": os.path.basename(rel) if rel else None,
                "ext": os.path.splitext(rel)[1] if rel else None,
                "commit": self.latest_commit_for(repo, rel) if rel else None,
            })

        splitter = RecursiveCharacterTextSplitter(chunk_size=1028, chunk_overlap=200)

        all_chunked = []
        for doc in documents:
            all_chunked.extend(splitter.split_documents([doc]))

        max_tokens = 0
        total_tokens = 0
        for _, doc in enumerate(all_chunked):
            ntokens = num_tokens(doc.page_content)
            max_tokens = max(max_tokens, ntokens)
            total_tokens += ntokens

        logger.info(f"Started loading {len(documents)} documents from {path} into ChromaDB collection {self.collection_name}, " \
                    f"max chunk tokens: {max_tokens}, total tokens: {total_tokens}, number of chunks: {len(all_chunked)}, ", \
                    f"default branch: {branch}.")        

        if len(all_chunked) == 0:
            logger.warning(f"No documents loaded from {path}. Skipping.")
            return

        for start in range(0, len(all_chunked), CHROMA_DB_MAX_BATCH_SIZE):
            end = start + CHROMA_DB_MAX_BATCH_SIZE
            self.vectorstore.add_documents(all_chunked[start:end])

        logger.info(f"Added {len(all_chunked)} documents to ChromaDB collection {self.collection_name} from {path}.") 
