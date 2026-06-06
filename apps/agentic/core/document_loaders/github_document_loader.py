import os
from datetime import timezone, datetime
from lib.logger import get_logger
from git import Repo

from langchain_community.document_loaders import GitLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from apps.agentic.core.document_loaders.chroma_document_loader import ChromaDocumentLoader
from apps.agentic.core.constants import (GITHUB_LOCAL_PATH, GITHUB_EXCLUDED_REPOS, CHROMA_DB_MAX_BATCH_SIZE,
                                         RESEARCH_LIBRARY_LOCAL_PATH, GITHUB_DB_NAME, GITHUB_COLLECTION_NAME,
                                         DB_PATH)
logger = get_logger("YADA")


class GitHubChromaDocumentLoader(ChromaDocumentLoader):
    """
    Document loader for GitHub repositories.

    Metadata added to each document
    ------------------------------
    - account: GitHub account or organization name
    - repo: Repository name
    - branch: Branch name (default branch)
    - path: File path relative to the repository root
    - filename: Base name of the file
    - ext: File extension
    - commit: Short SHA of the latest commit touching the file
    - commit_ts: ISO-8601 UTC timestamp of the latest commit touching the file
    - commit_ts_unix: Unix timestamp of the latest commit touching the file

    Meta Data Filter Examples
    ------------------------
    Requests must use filters on the meta data to restrict to a single repo or account+repo.

    Example filter to restrict to a single repo: 
        repo:yada
    Example filter to restrict to a single account: 
        account:glyfish
    Example filter to restrict to a single account+repo: 
        account:glyfish repo:yada
    Example filter to restrict to a single account+repo+path prefix: 
        account:glyfish repo:yada path:apps/agentic/
    Example to filter by file extension:
        ext:md
    Example to filter commit timestamp range:
        after:2012-01-01
        before:2023-01-01
    """

    def __init__(self, db_path=DB_PATH):
        super().__init__(GITHUB_DB_NAME, GITHUB_COLLECTION_NAME, db_path)


    async def load_all_documents(self, base_path: str = GITHUB_LOCAL_PATH, **kwargs):
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


    async def load_document(self, path: str, **kwargs):
        """
        Load documents into the ChromaDB collection.
        """

        logger.info(f"Updating github document store from {path}.")
                
        if os.path.isdir(os.path.join(path, ".git")):
            await self.load_github_repo(path)


    def _delete_repo(self, account: str, repo_name: str) -> int:
        """
        Delete all chunks in the collection for the given account/repo pair.
        """
        collection = getattr(self._vectorstore, "_collection", None)
        if collection is None:
            logger.warning("_delete_repo: vector store collection unavailable, skipping delete.")
            return 0

        result = collection.get(
            where={"$and": [{"account": account}, {"repo": repo_name}]},
            include=[],
        )
        ids = result.get("ids") or []
        if ids:
            collection.delete(ids=ids)
            logger.info(
                f"_delete_repo: deleted {len(ids)} chunks for {account}/{repo_name} "
                f"from collection '{self.collection_name}'."
            )
        return len(ids)


    def get_default_branch(self, repo_path: str) -> str:
        repo = Repo(repo_path)
        # If HEAD is pointing to a branch, use that
        try:
            return repo.active_branch.name
        except TypeError:
            # Detached HEAD? fall back to reading origin/HEAD
            remote_head = repo.remotes.origin.refs.HEAD
            return remote_head.reference.name.split("/")[-1]


    def build_commit_map(self, repo) -> dict[str, tuple[str, str, int]]:
        """
        Build a map of rel_path -> (short_sha, iso_ts, unix_ts) for all files
        in a single git log subprocess call, avoiding one iter_commits per file.
        """
        import subprocess

        repo_root = os.path.realpath(repo.working_tree_dir or "")
        commit_map: dict[str, tuple[str, str, int]] = {}

        result = subprocess.run(
            ["git", "log", "--format=COMMIT %H %ct", "--name-only", "--diff-filter=AM"],
            cwd=repo_root,
            capture_output=True,
            text=True,
        )

        current_sha = None
        current_ts_unix = None

        for line in result.stdout.splitlines():
            if line.startswith("COMMIT "):
                parts = line.split()
                current_sha = parts[1][:12]
                current_ts_unix = int(parts[2])
            elif line.strip() and current_sha is not None and current_ts_unix is not None:
                rel = line.strip()
                if rel not in commit_map:
                    ts_iso = datetime.fromtimestamp(current_ts_unix, tz=timezone.utc).isoformat()
                    commit_map[rel] = (current_sha, ts_iso, current_ts_unix)

        return commit_map


    async def load_github_repo(self, path: str):
        """
        Load the GitHub repositories into the ChromaDB collection.
        """

        account = os.path.basename(os.path.dirname(path.rstrip("/")))
        repo_name = os.path.basename(path.rstrip("/"))
        self._delete_repo(account, repo_name)

        branch = self.get_default_branch(path)
        logger.info(f"Setting default branch {branch} for {path}.")
        loader = GitLoader(repo_path=path, branch=branch)

        documents = await loader.aload()

        repo = Repo(path)
        repo_root = os.path.realpath(repo.working_tree_dir or path)

        logger.info(f"Building commit map for {path}.")
        commit_map = self.build_commit_map(repo)

        for d in documents:
            src = d.metadata.get("source")  # may be absolute or relative from GitLoader
            rel = None
            src_abs = None
            if src:
                # Ensure we resolve relative paths against the repo root, not process CWD.
                if os.path.isabs(src):
                    src_abs = os.path.realpath(src)
                else:
                    src_abs = os.path.realpath(os.path.join(repo_root, src))

                # Only compute a repo-relative path if the file is inside this repo.
                if src_abs.startswith(repo_root + os.sep) or src_abs == repo_root:
                    rel = os.path.relpath(src_abs, start=repo_root)
                else:
                    logger.debug(f"Skipping commit lookup for out-of-repo file resolved from '{src}': {src_abs}")

            filename = os.path.basename(rel) if rel else (os.path.basename(src_abs) if src_abs else None)
            ext = os.path.splitext(rel)[1] if rel else (os.path.splitext(src_abs)[1] if src_abs else None)
            last_commit, commit_ts, commit_ts_unix = commit_map.get(rel, (None, None, None)) if rel else (None, None, None)

            file_metadata = {
                "account": account,
                "repo": repo_name,
                "branch": branch,
                "path": rel,
                "filename": filename,
                "ext": ext,
                "commit": last_commit,
                "ts_iso": commit_ts,
                "ts_unix": commit_ts_unix,
                "commit_ts": commit_ts,
                "commit_ts_unix": commit_ts_unix,
            }

            d.metadata.update(file_metadata)

        splitter = RecursiveCharacterTextSplitter(chunk_size=1028, chunk_overlap=200, add_start_index=True)

        all_chunked = []
        for doc in documents:
            all_chunked.extend(splitter.split_documents([doc]))

        max_tokens = 0
        total_tokens = 0
        for _, doc in enumerate(all_chunked):
            ntokens = self.num_tokens(doc.page_content)
            max_tokens = max(max_tokens, ntokens)
            total_tokens += ntokens

        logger.info(f"Started loading {len(documents)} documents from {path} into ChromaDB collection {self.collection_name}, " \
                    f"max chunk tokens: {max_tokens}, total tokens: {total_tokens}, number of chunks: {len(all_chunked)}, " \
                    f"default branch: {branch}.")        

        if len(all_chunked) == 0:
            logger.warning(f"No documents loaded from {path}. Skipping.")
            return

        for start in range(0, len(all_chunked), CHROMA_DB_MAX_BATCH_SIZE):
            end = start + CHROMA_DB_MAX_BATCH_SIZE
            self.vectorstore.add_documents(all_chunked[start:end])

        logger.info(f"Added {len(all_chunked)} documents to ChromaDB collection {self.collection_name} from {path}.") 
