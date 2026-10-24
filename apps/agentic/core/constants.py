# GITHUB constants
import os
from pathlib import Path

# RAG retrieval constants
_raw_threshold = os.environ.get("RAG_SCORE_THRESHOLD")
RAG_SCORE_THRESHOLD = float(_raw_threshold) if _raw_threshold is not None else None

# Anchored to the repo root, not the working directory. This was ".db", and the
# agents construct their loaders with no path argument -- CodeRepoAgent does
# GitHubChromaDocumentLoader() -- so the store resolved against whatever cwd the
# process happened to have. Run from anywhere but the repo root, Chroma does not
# error: it CREATES an empty store there and every query returns zero hits. A
# notebook under notebooks/documents/ did exactly that, and notebooks/data/.db/fred
# is older debris from the same mistake. Silent emptiness is the worst failure mode
# this codebase has (cf. GITHUB_LOCAL_PATH, which self-matched yada's .gitignore and
# indexed 0 of 415,006 chunks), so resolve it once, here.
# Override with YADA_DB_PATH when a different store is genuinely wanted.
_ROOT = Path(__file__).resolve().parents[3]
DB_PATH = os.environ.get("YADA_DB_PATH") or str(_ROOT / ".db")

GITHUB_ACCOUNTS = ["troystribling", "glyfish"]
GITHUB_EXCLUDED_REPOS = ["3dmodels"]

GITHUB_API = "https://api.github.com"
GITHUB_DB_NAME = "github"
GITHUB_COLLECTION_NAME = "github-repos"
GITHUB_LOCAL_PATH = str(_ROOT / ".repos")

# ChromaDB constants
CHROMA_DB_MAX_BATCH_SIZE = 1000

# Research note constants
RESEARCH_LIBRARY_DB_NAME = "research_library"
RESEARCH_LIBRARY_COLLECTION_NAME = "research-library"
RESEARCH_LIBRARY_LOCAL_PATH = str(_ROOT / "research_library")
RESEARCH_DOCUMENTS_METADATA_FILE = os.path.join(RESEARCH_LIBRARY_LOCAL_PATH, "research_documents.yml")

# FRED API metadata
FRED_DB_NAME = "fred"
FRED_COLLECTION_NAME = "fred"
FRED_LOCAL_PATH = str(_ROOT / "clients" / "fred")

# ETF document store constants
ETF_DB_NAME = "etf"
ETF_COLLECTION_NAME = "etf-info"

# MCP server
MCP_URL = "http://localhost:8080/sse"

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
    # Present in the store and promised by the extractor's `ext` description, but
    # missing here until 2026-10-24 -- so they rendered as plaintext in a fenced block
    # and no language name could resolve to them. `.ipynb` alone is 191,357 chunks,
    # 46% of the index and its single largest extension.
    ".ipynb": "json",
    ".m": "objectivec",      # this store's .m is iOS, not MATLAB
    ".mm": "objectivec",
    ".erl": "erlang",
    ".hrl": "erlang",
    ".jl": "julia",
    ".sol": "solidity",
    ".pl": "perl",
    ".tex": "latex",
    ".zsh": "bash",
    ".rst": "rst",
    ".svg": "xml",
    ".rake": "ruby",
    ".gemspec": "ruby",
}


def _language_extensions() -> dict[str, tuple[str, ...]]:
    """
    Invert PROGRAMMING_LANGUAGE_MAP into language -> the extensions it covers.

    Derived rather than written out so the two cannot disagree, which is the failure
    the map's own gap just demonstrated. A language reaches every extension mapped to
    it, so 'c' means .c and .h, and 'yaml' means .yaml and .yml.
    """
    out: dict[str, list[str]] = {}
    for ext, language in PROGRAMMING_LANGUAGE_MAP.items():
        out.setdefault(language, []).append(ext)
    return {k: tuple(sorted(v)) for k, v in out.items()}


#: Language name -> the stored extensions it means. Consulted only for a value with no
#: leading dot: a dot says the caller is naming an extension literally, so `.c` is .c
#: alone while `c` is the language and includes its headers.
LANGUAGE_EXTENSIONS: dict[str, tuple[str, ...]] = {
    **_language_extensions(),
    # Names for a language that are not the map's own label for it. Every one of these
    # is already promised by the extractor's `ext` field description; without them the
    # description describes a mapping that does not exist.
    "c++": _language_extensions()["cpp"],
    "c#": _language_extensions()["csharp"],
    "golang": _language_extensions()["go"],
    "js": _language_extensions()["javascript"],
    "ts": _language_extensions()["typescript"],
    "shell": _language_extensions()["bash"],
    "sh": _language_extensions()["bash"],
    "yml": _language_extensions()["yaml"],
    "objective-c": (".m", ".mm"),
    "objectivec": (".m", ".mm"),
    "objc": (".m", ".mm"),
    "jupyter": (".ipynb",),
    "notebook": (".ipynb",),
    "notebooks": (".ipynb",),
    "plaintext": (".txt",),
}

# SSE streaming status labels for agent tool/node events
TOOL_START_LABELS: dict[str, str] = {
    # Orchestrator delegation tools
    "delegate_to_search_agent":                  "Searching the web...",
    "delegate_to_plot_agent":                    "Building plot...",
    "delegate_to_bar_chart_agent":               "Building bar chart...",
    "delegate_to_time_series_plot_agent":        "Building time series plot...",
    "delegate_to_data_info_agent":     "Querying document store info...",
    "delegate_to_code_repository_search_agent":  "Searching code repositories...",
    "delegate_to_research_library_search_agent": "Searching research library...",
    "delegate_to_fred_data_info_search_agent":   "Searching FRED data...",
    "delegate_to_etf_data_info_search_agent":    "Searching ETF data...",
    "delegate_to_time_series_agent":             "Fetching time series...",
    "extract_document_query_from_request":       "Extracting query filters...",
    "load_etf_data":                             "Loading ETF data...",
    "reload_etf_data":                           "Reloading ETF data...",
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
    "delegate_to_plot_agent":                    "Plot ready",
    "delegate_to_bar_chart_agent":               "Bar chart ready",
    "delegate_to_time_series_plot_agent":        "Time series plot ready",
    "delegate_to_data_info_agent":     "Document store query complete",
    "delegate_to_code_repository_search_agent":  "Code repository search complete",
    "delegate_to_research_library_search_agent": "Research library search complete",
    "delegate_to_fred_data_info_search_agent":   "FRED data search complete",
    "delegate_to_etf_data_info_search_agent":    "ETF data search complete",
    "delegate_to_time_series_agent":             "Time series fetch complete",
    "load_etf_data":                             "ETF data loaded",
    "reload_etf_data":                           "ETF data reloaded",
    "bar_chart_tool":                            "Bar chart rendered",
    "time_series_plot_tool":                     "Time series plot rendered",
    "retrieve":                                  "Documents retrieved",
    "grade":                                     "Relevance grading complete",
    "generate":                                  "Response ready",
}
