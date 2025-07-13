from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

import os
import requests
from lib.logger import get_logger

from git import Repo, GitCommandError

router = APIRouter()
logger = get_logger("YADA")
github_accounts = ["troystribling", "glyfish"]

GITHUB_API = "https://api.github.com"

class CloneRequest(BaseModel):
    accounts: list[str]  # GitHub usernames/orgs


def clone_or_pull(repo_url, local_path):
    if os.path.exists(local_path):
        try:
            repo = Repo(local_path)
            repo.remotes.origin.pull()
            return f"Updated {local_path}"
        except Exception as e:
            return f"Failed to update {local_path}: {e}"
    else:
        try:
            Repo.clone_from(repo_url, local_path)
            return f"Cloned {local_path}"
        except Exception as e:
            return f"Failed to clone {repo_url}: {e}"


@router.post("/github/clone")
def clone_github_repos():
    logger.debug(f"Received request to clone GitHub repos for accounts: {github_accounts}")
    for account in github_accounts:
        # List all public repos for the user/org
        
        url = f"{GITHUB_API}/users/{account}/repos"
        logger.debug(f"Fetching repos for {account} from {url}")
        resp = requests.get(url)
        logger.debug(f"Fetching repos for {account} from {url}")
        
        if resp.status_code != 200:
            logger.error(f"Fetching repos for {account} from {url}, failed with status code {resp.status_code}")
            return {"status": "Error", "message": f"Failed to fetch repos for {account}: {resp.text}"}

        for repo in resp.json():
            repo_name = repo["name"]
            clone_url = repo["clone_url"]
            local_path = os.path.join(".repos", account, repo_name)
            logger.debug(f"Cloning {repo_name} from {clone_url} to {local_path}")

            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            result = clone_or_pull(clone_url, local_path)
            logger.debug(result)

    return {"status": "OK"}