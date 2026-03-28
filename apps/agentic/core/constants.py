# GITHUB constants
import os

# RAG retrieval constants
_raw_threshold = os.environ.get("RAG_SCORE_THRESHOLD")
RAG_SCORE_THRESHOLD = float(_raw_threshold) if _raw_threshold is not None else None
DB_PATH = ".db"

GITHUB_ACCOUNTS = ["troystribling"]
GITHUB_EXCLUDED_REPOS = ["3dmodels"]

GITHUB_API = "https://api.github.com"
GITHUB_DB_NAME = "github"
GITHUB_COLLECTION_NAME = "github-repos"
GITHUB_LOCAL_PATH = ".repos"

# ChromaDB constants
CHROMA_DB_MAX_BATCH_SIZE = 1000

# Research note constants
RESEARCH_LIBRARY_DB_NAME = "research_library"
RESEARCH_LIBRARY_COLLECTION_NAME = "research-library"
RESEARCH_LIBRARY_LOCAL_PATH = "./research_library"
RESEARCH_DOCUMENTS_METADATA_FILE = os.path.join(RESEARCH_LIBRARY_LOCAL_PATH, "research_documents.yml")

# FRED API metadata
FRED_DB_NAME = "fred"
FRED_COLLECTION_NAME = "fred"
FRED_LOCAL_PATH = "./clients/fred"

# PDF document library constants
PDF_DOCUMENT_LIBRARY_DB_NAME = "pdf_document_library"
PDF_DOCUMENT_LIBRARY_COLLECTION_NAME = "pdf-documents"
PDF_DOCUMENT_LIBRARY_LOCAL_PATH = "./document_library"

# Programming language mapping based on file extensions
PROGRAMMING_LANGUAGE_MAP = {
    ".py": "python",
    ".rb": "ruby",
    ".rs": "rust",
    ".js": "javascript",
    ".ts": "typescript",
    ".jsx": "jsx",
    ".tsx": "tsx",
    ".go": "go",
    ".java": "java",
    ".kt": "kotlin",
    ".c": "c",
    ".h": "c",
    ".cpp": "cpp",
    ".hpp": "cpp",
    ".cs": "csharp",
    ".php": "php",
    ".swift": "swift",
    ".scala": "scala",
    ".sql": "sql",
    ".sh": "bash",
    ".json": "json",
    ".toml": "toml",
    ".ini": "ini",
    ".conf": "ini",
    ".yml": "yaml",
    ".yaml": "yaml",
    ".md": "markdown",
    ".mdx": "markdown",
    ".rdoc": "markdown",
    ".html": "html",
    ".xml": "xml",
    ".css": "css",
    ".txt": "text",
}

# SSE streaming status labels for agent tool/node events
TOOL_START_LABELS: dict[str, str] = {
    # Orchestrator delegation tools
    "delegate_to_search_agent":                  "Searching the web...",
    "delegate_to_bar_chart_agent":               "Building bar chart...",
    "delegate_to_time_series_plot_agent":        "Building time series plot...",
    "delegate_to_document_store_info_agent":     "Querying document store info...",
    "delegate_to_code_repository_search_agent":  "Searching code repositories...",
    "delegate_to_research_library_search_agent": "Searching research library...",
    "delegate_to_fred_data_info_search_agent":   "Searching FRED data...",
    "extract_document_query_from_request":       "Extracting query filters...",
    # Plot tools
    "bar_chart_tool":                            "Rendering bar chart...",
    "time_series_plot_tool":                     "Rendering time series plot...",
    # Subagent graph nodes
    "retrieve":                                  "Retrieving documents...",
    "grade":                                     "Grading document relevance...",
    "generate":                                  "Generating response...",
    "model":                                     "Thinking...",
}

TOOL_END_LABELS: dict[str, str] = {
    "delegate_to_search_agent":                  "Web search complete",
    "delegate_to_bar_chart_agent":               "Bar chart ready",
    "delegate_to_time_series_plot_agent":        "Time series plot ready",
    "delegate_to_document_store_info_agent":     "Document store query complete",
    "delegate_to_code_repository_search_agent":  "Code repository search complete",
    "delegate_to_research_library_search_agent": "Research library search complete",
    "delegate_to_fred_data_info_search_agent":   "FRED data search complete",
    "bar_chart_tool":                            "Bar chart rendered",
    "time_series_plot_tool":                     "Time series plot rendered",
    "retrieve":                                  "Documents retrieved",
    "grade":                                     "Relevance grading complete",
    "generate":                                  "Response ready",
}
