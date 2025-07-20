from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

import os
import requests
from urllib.parse import urlparse

from lib.logger import get_logger
from apps.agentic.core.utils import GITHUB_ACCOUNTS 

from git import Repo

from apps.agentic.core.chroma_document_loader import ChromaDocumentLoader

from langchain_community.vectorstores import Chroma


router = APIRouter()
logger = get_logger("YADA")

GITHUB_API = "https://api.github.com"
GITHUB_DB_NAME = "github"
GITHUB_COLLECTION_NAME = "github-repos"

class CloneRequest(BaseModel):
    accounts: list[str]  # GitHub usernames/orgs


def clone_or_pull(repo_name, repo_url, local_path):
    logger.debug(f"CHECKING {repo_name} from {repo_url} to {local_path}")
    if os.path.exists(local_path):
        try:
            repo = Repo(local_path)
            repo.remotes.origin.pull()
            logger.info(f"PULLED {local_path}")
        except Exception as e:
            logger.error(f"Failed to update {local_path}: {e}")
    else:
        try:
            Repo.clone_from(repo_url, local_path)
            logger.info(f"CLONED {repo_name} from {repo_url} to {local_path}")
        except Exception as e:
            logger.error(f"Failed to clone {repo_name} from {repo_url}: {e}")



@router.post("/github/clone")
async def clone_github_repos():
    GITHUB_API_KEY = os.environ["GITHUB_API_KEY"]
    HEADERS = {"Authorization": f"token {GITHUB_API_KEY}"}

    doc_loader = ChromaDocumentLoader(GITHUB_DB_NAME, GITHUB_COLLECTION_NAME)
    
    # Determine authenticated user for retrieving private repos
    user_resp = requests.get(f"{GITHUB_API}/user", headers=HEADERS)
    if user_resp.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to fetch authenticated user")
    
    auth_username = user_resp.json()["login"]
    logger.debug(f"Received request to clone GitHub repos for accounts: {GITHUB_ACCOUNTS} and authenticated user: {auth_username}")

    for account in GITHUB_ACCOUNTS:
        # Use the appropriate endpoint to include private repos
        if account == auth_username:
            # fetch all repos (public + private) for the authenticated user
            url = f"{GITHUB_API}/user/repos?per_page=100&visibility=all"
        else:
            # fetch org repos (public + private if member)
            url = f"{GITHUB_API}/orgs/{account}/repos?per_page=100&type=all"
        logger.debug(f"Fetching repos for {account} and {auth_username} from {url}")

        resp = requests.get(url, headers=HEADERS)
        
        if resp.status_code != 200:
            logger.error(f"Fetching repos for {account} from {url}, failed with status code {resp.status_code}")
            return {"status": "Error", "message": f"Failed to fetch repos for {account}: {resp.text}"}

        for repo in resp.json():
            repo_name = repo["name"]
            clone_url = repo["clone_url"]
            auth_clone_url = clone_url.replace("https://", f"https://{auth_username}:{GITHUB_API_KEY}@")
            parsed_url = urlparse(auth_clone_url)
            owner = parsed_url.path.split('/')[1]
            local_path = os.path.join(".repos", owner, repo_name)
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            clone_or_pull(repo_name, auth_clone_url, local_path)

        logger.info(f"Updated all repos for {account}")

    await doc_loader.load_github_documents()

    return {"status": "Success", "message": "All repositories cloned or updated successfully."}