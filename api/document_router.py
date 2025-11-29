from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import Response
from pydantic import BaseModel

import os
import requests
from urllib.parse import urlparse
from pathlib import Path
from fastapi.responses import FileResponse

from lib.logger import get_logger
from apps.agentic.core.constants import (
    GITHUB_ACCOUNTS,
    GITHUB_API,
    RESEARCH_LIBRARY_LOCAL_PATH,
    PDF_DOCUMENT_LIBRARY_LOCAL_PATH,
)

from git import Repo
from apps.agentic.core.document_loaders.github_document_loader import GitHubChromaDocumentLoader
from apps.agentic.core.document_loaders.research_library_document_loader import ResearchLibraryChromaDocumentLoader
from apps.agentic.core.document_loaders.document_library_loader import DocumentLibraryLoader
from langchain_community.vectorstores import Chroma

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DOCUMENT_LIBRARY_DIR = Path("./document_library").resolve()

router = APIRouter()
logger = get_logger("YADA")


def _resolve_research_note_path(filename: str) -> Path:
    """Return an absolute path inside RESEARCH_LIBRARY_LOCAL_PATH for the provided filename."""
    base_dir = Path(RESEARCH_LIBRARY_LOCAL_PATH).resolve()
    if not base_dir.exists():
        raise HTTPException(
            status_code=404,
            detail=f"Research library directory '{base_dir}' not found.",
        )

    # First, treat the filename as a relative path beneath the base directory
    candidate = (base_dir / filename).resolve()
    try:
        candidate.relative_to(base_dir)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Filename must be inside the research library directory.",
        )

    if candidate.exists() and candidate.is_file():
        return candidate

    # Fall back to searching by basename anywhere under the research library
    matches = list(base_dir.rglob(Path(filename).name))
    for match in matches:
        if match.is_file():
            return match

    raise HTTPException(
        status_code=404,
        detail=f"Research document '{filename}' not found under {base_dir}.",
    )

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
class LoadResearchDocumentPayload(BaseModel):
    filename:str
    title: str
    authors: str
    date: str
    topic: str
    tags: list[str]

@router.post("/document/load_research_document")
async def load_research_document(payload: LoadResearchDocumentPayload):

    note_path = _resolve_research_note_path(payload.filename)
    try:
        relative_note_path = note_path.relative_to(PROJECT_ROOT)
    except ValueError:
        relative_note_path = note_path

    meta_data = {
        "filename": payload.filename,
        "path": str(relative_note_path),
        "title": payload.title,
        "authors": payload.authors,
        "date": payload.date,
        "topic": payload.topic,
        "tags": ",".join(payload.tags)
    }

    doc_loader = ResearchLibraryChromaDocumentLoader()

    logger.debug((f"Received request to load research note: "
                  f"file_name={meta_data['filename']}, title={meta_data['title']}, authors={meta_data['authors']}, "
                  f"start_date={meta_data['date']}, topic={meta_data['topic']}, tags={meta_data['tags']}."))

    await doc_loader.load_document(str(note_path), meta_data=meta_data)

    return {"status": "Success", "message": f"Loaded research note: {payload.title}."}


"""
Load specified PDF document to the document library.
"""
class LoadPDFDocumentPayload(BaseModel):
    filename: str
    title: str
    authors: list[str]
    published_date: str
    topic: str
    tags: list[str]

@router.post("/document/load_pdf_document")
async def load_pdf_document(payload: LoadPDFDocumentPayload):

    pdf_path = os.path.join(PDF_DOCUMENT_LIBRARY_LOCAL_PATH, payload.filename)
    meta_data = {
        "filename": payload.filename,
        "path": pdf_path,
        "title": payload.title,
        "authors": payload.authors,
        "published_date": payload.published_date,
        "topic": payload.topic,
        "tags": ",".join(payload.tags)
    }

    doc_loader = DocumentLibraryLoader()

    logger.debug((f"Received request to load research note: "
                  f"file_name={meta_data['filename']}, title={meta_data['title']}, authors={meta_data['authors']}, "
                  f"published_date={meta_data['published_date']}, topic={meta_data['topic']}, tags={meta_data['tags']}."))

    await doc_loader.load_document(pdf_path, meta_data=meta_data)

    return {"status": "Success", "message": f"Loaded PDF document: {payload.title}."}


"""
Stream specified PDF document
"""
@router.get("/document/stream_pdf_document")
async def serve_pdf(
    name: str = Query(..., description="basename of the PDF, e.g. foo.pdf")
):
    """
    Return a PDF in a browser-displayable way (no download prompt).
    The front end calls this like:
      /api/document/pdf?name=Discrete%20State%20Markov%20Chain%20Equilibrium.pdf
    """

    # 1. Lock it to just a filename, to avoid "../../etc/passwd" nonsense
    safe_name = Path(name).name
    if safe_name != name:
        # user tried to include a path
        raise HTTPException(status_code=400, detail="Invalid filename")

    # 2. Build absolute path under your pdf library dir
    pdf_path = (DOCUMENT_LIBRARY_DIR / safe_name).resolve()

    # 3. Double-check it's still under the allowed root
    if not str(pdf_path).startswith(str(DOCUMENT_LIBRARY_DIR)):
        raise HTTPException(status_code=400, detail="Invalid filename")

    # 4. Check that it actually exists
    if not pdf_path.exists() or not pdf_path.is_file():
        raise HTTPException(status_code=404, detail="PDF not found")

    # 5. Read the bytes
    data = pdf_path.read_bytes()

    # 6. Return them with headers that tell the browser:
    #    - it's a PDF
    #    - render inline (DON'T force download)
    return Response(
        content=data,
        media_type="application/pdf",
        headers={
            # this is the important part:
            "Content-Disposition": f'inline; filename="{safe_name}"',
            # optional: reduce caching weirdness while you're iterating
            "Cache-Control": "no-store",
        },
    )
