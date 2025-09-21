from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

import os
import requests
from urllib.parse import urlparse

from lib.logger import get_logger
from apps.agentic.core.constants import (GITHUB_ACCOUNTS, GITHUB_API)

from git import Repo
from apps.agentic.core.github_document_loader import GitHubChromaDocumentLoader
from apps.agentic.core.research_note_document_loader import ResearchNoteChromaDocumentLoader
from langchain_community.vectorstores import Chroma


router = APIRouter()
logger = get_logger("YADA")

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

"""
Load all GitHub repositories for the configured accounts.
"""
@router.post("/document/load_all_github_repos")
async def load_all_github_repos():
    GITHUB_API_KEY = os.environ["GITHUB_API_KEY"]
    HEADERS = {"Authorization": f"token {GITHUB_API_KEY}"}

    doc_loader = GitHubChromaDocumentLoader()
    
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
        logger.debug(f"Fetching repos for account {account} and user {auth_username} from {url}")

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

    await doc_loader.load_all_documents()

    return {"status": "Success", "message": "All repositories cloned or updated successfully."}

"""
Load all configured GitHub repositories for the configured accounts.
"""
class GitHubRepoLoadPayload(BaseModel):
    account: str
    repo: str

@router.post("/document/load_github_repo")
async def load_github_repo(payload: GitHubRepoLoadPayload):
    GITHUB_API_KEY = os.environ["GITHUB_API_KEY"]
    HEADERS = {"Authorization": f"token {GITHUB_API_KEY}"}

    doc_loader = GitHubChromaDocumentLoader()
    
    # Determine authenticated user for retrieving private repos
    user_resp = requests.get(f"{GITHUB_API}/user", headers=HEADERS)
    if user_resp.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to fetch authenticated user")
    
    auth_username = user_resp.json()["login"]
    account = payload.account
    repo_name = payload.repo

    logger.debug(f"Received request to clone GitHub repository: {repo_name} for account: {account}, authenticated user: {auth_username}")
    clone_url = f"https://github.com/{account}/{repo_name}.git"
    auth_clone_url = clone_url.replace("https://", f"https://{auth_username}:{GITHUB_API_KEY}@")
    local_path = os.path.join(".repos", account, repo_name)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    clone_or_pull(repo_name, auth_clone_url, local_path)

    await doc_loader.load_document(local_path)

    return {"status": "Success", "message": f"Updated gitHub Repository {repo_name}."}


"""
Load specified GitHub repository for the configured accounts.
"""
class GitHubRepoLoadPayload(BaseModel):
    account: str
    repo: str
    
@router.post("/document/load_github_repo")
async def load_github_repo(payload: GitHubRepoLoadPayload):
    GITHUB_API_KEY = os.environ["GITHUB_API_KEY"]
    HEADERS = {"Authorization": f"token {GITHUB_API_KEY}"}

    doc_loader = GitHubChromaDocumentLoader()
    
    # Determine authenticated user for retrieving private repos
    user_resp = requests.get(f"{GITHUB_API}/user", headers=HEADERS)
    if user_resp.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to fetch authenticated user")
    
    auth_username = user_resp.json()["login"]
    account = payload.account
    repo_name = payload.repo

    logger.debug(f"Received request to clone GitHub repository: {repo_name} for account: {account}, authenticated user: {auth_username}")
    clone_url = f"https://github.com/{account}/{repo_name}.git"
    auth_clone_url = clone_url.replace("https://", f"https://{auth_username}:{GITHUB_API_KEY}@")
    local_path = os.path.join(".repos", account, repo_name)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    clone_or_pull(repo_name, auth_clone_url, local_path)

    await doc_loader.load_github_documents(local_path)

    return {"status": "Success", "message": f"Updated gitHub Repository {repo_name}."}


"""
Load specified research note into the document store.
"""
class LoadResearchNotePayload(BaseModel):
    filename:str
    title: str
    author: str
    start_date: str
    topic: str
    tags: list[str]

@router.post("/document/load_research_note")
async def load_research_note(payload: LoadResearchNotePayload):

    meta_data = {
        "filename": payload.filename,
        "title": payload.title,
        "author": payload.author,
        "start_date": payload.start_date,
        "topic": payload.topic,
        "tags": payload.tags
    }

    doc_loader = ResearchNoteChromaDocumentLoader(meta_data)

    logger.debug((f"Received request to load research note: "
                  f"file_name={meta_data['filename']}, title={meta_data['title']}, author={meta_data['author']}, "
                  f"start_date={meta_data['start_date']}, topic={meta_data['topic']}, tags={meta_data['tags']}."))

    await doc_loader.load_document(meta_data)

    return {"status": "Success", "message": f"Loaded research note: {payload.title}."}