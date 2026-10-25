"""
The four document-store tools: search and describe, over code and over the research
library.

Two stores, two verbs, one implementation of each. The tools differ only in which
filters they publish and which metadata model they return.

Why four and not two
--------------------
A merged `search(store=...)` would admit `repo="zgomot" AND shelf="jaynes"` -- two
values that are individually real and jointly empty *by category*. Progressive
relaxation would then drop one and return the other store's documents under
`status="filters_relaxed"`, which reads as a successful widening. Split per store, that
failure is unrepresentable: every conjunction a tool can express is within one corpus,
so the worst a dropped term costs is a broader answer from the right place.

Why descriptions are generated
------------------------------
`shelf`'s five values and `authors`' 22 surnames come from the vocabulary at
registration, not from a literal in this file. A hand-maintained list is wrong the
first time a document is added, and wrong silently -- the model proposes a value that
no longer exists and the filter matches nothing. `repo` and `ext` are deliberately NOT
listed: 101 and 190 values are too many for a description that sits in the client's
context on every turn, and `describe_code` answers that question on demand.

See sefer/planning/yada-document-mcp-design.md.
"""

from __future__ import annotations

from typing import Any

from apps.agentic.core.agents.chroma_rag_agent import ChromaRAGAgent, SearchOutcome
from apps.agentic.core.constants import GITHUB_DB_NAME, RESEARCH_LIBRARY_DB_NAME
from apps.agentic.db.vocabulary import NO_EXTENSION, Vocabulary
from lib.logger import get_logger

from mcp_server.document_models import (
    CodeHits,
    CodeVocabulary,
    GithubMeta,
    Hit,
    LibraryHits,
    LibraryMeta,
    LibraryVocabulary,
)

logger = get_logger("YADA")

#: The filters each tool publishes. A subset of what vocabulary_builder indexes:
#: `account` is indexed but
#: not published, because `repo` already accepts an account name and the server decides
#: which it is -- a parameter whose only job is to classify a name the server can
#: classify itself is a parameter the model can get wrong.
PUBLISHED_FILTERS: dict[str, tuple[str, ...]] = {
    GITHUB_DB_NAME: ("repo", "ext"),
    RESEARCH_LIBRARY_DB_NAME: ("authors", "title", "shelf"),
}

_agents: dict[str, ChromaRAGAgent] = {}


def _agent(store: str) -> ChromaRAGAgent:
    """
    One agent per store, built on first use and reused.

    Constructing one builds a Chroma client, an embeddings client and two LLM clients,
    so it must not be a cost of merely listing tools -- and with the filter supplied per
    call it no longer needs to be per request either.

    `widen_on_empty=False`: the agent's unfiltered fallback is right for a conversation
    and wrong here. A tool can say which filter matched nothing and offer what exists;
    silently answering from a different set would be the failure this design removes.
    """
    if store not in _agents:
        if store == GITHUB_DB_NAME:
            from apps.agentic.agents.document.code_repo_agent import CodeRepoAgent
            _agents[store] = CodeRepoAgent(None, widen_on_empty=False)
        else:
            from apps.agentic.agents.document.research_library_agent import ResearchLibraryAgent
            _agents[store] = ResearchLibraryAgent(None, widen_on_empty=False)
        logger.info(f"Document tools: built the {store} agent")
    return _agents[store]


# ------------------------------------------------------------------ shared helpers

def _resolve(store: str, proposed: dict[str, str | None]):
    return Vocabulary.resolve_filters(store, proposed)


def _available(store: str, resolutions) -> dict[str, list[str]]:
    """What exists for each field that matched nothing -- the next step after a dead end."""
    return {r.field: Vocabulary.available(store, r.field) for r in resolutions if not r.matched}


def _facets_of(chunks, fields: tuple[str, ...]) -> dict[str, dict[str, int]]:
    """Values among the returned hits. Free -- the metadata is already in hand."""
    out: dict[str, dict[str, int]] = {}
    for chunk in chunks:
        for field in fields:
            value = chunk.metadata.get(field)
            if value is None:
                continue
            label = NO_EXTENSION if field == "ext" and value == "" else str(value)
            out.setdefault(field, {})
            out[field][label] = out[field].get(label, 0) + 1
    return out


def _store_is_built(store: str) -> bool:
    return Vocabulary.scan_info(store) is not None


def _search(store: str, query: str, proposed: dict[str, str | None], limit: int,
            hits_model, meta_model) -> Any:
    """
    The shared search. Resolve, then retrieve and rank -- never the other way round.

    The order is the whole point. Chroma's `where` is exact equality, so an unresolved
    value matches zero rows and returns no error, which is indistinguishable from an
    empty corpus. Resolving first means a value that cannot match is answered in
    microseconds with what does exist, instead of after a 3 s search that found the
    wrong thing.
    """
    requested = {k: v for k, v in proposed.items() if v is not None}
    base = dict(status="ok", request=query, filters_requested=requested)

    if not _store_is_built(store):
        return hits_model(**{**base, "status": "store_empty", "query": query,
                             "detail": f"The {store} vocabulary has never been built; "
                                       f"run a rebuild before searching."})

    resolved = _resolve(store, proposed)
    base["filters_resolved"] = resolved.resolved

    if resolved.unresolvable:
        dead = ", ".join(f"{r.field}={r.proposed!r}" for r in resolved.unresolvable)
        return hits_model(**{**base, "status": "unresolvable_filter", "query": query,
                             "available": _available(store, resolved.resolutions),
                             "detail": f"{dead} matches no stored value, so no search was run. "
                                       f"`available` lists what exists."})

    base["filters_applied"] = resolved.applied
    outcome: SearchOutcome = _agent(store).search(query, where=resolved.where, k=limit)

    if outcome.error is not None:
        return hits_model(**{**base, "status": "retrieval_error", "query": query,
                             "detail": outcome.error})

    fields = PUBLISHED_FILTERS[store]
    hits = [
        Hit[meta_model](
            rank=i,
            score=chunk.score if chunk.score is not None else 0.0,
            source=store,
            path=chunk.path,
            snippet=chunk.text[:1200],
            metadata=meta_model(**{f: _meta_value(chunk.metadata, f) for f in fields}),
            uri=_uri_for(store, chunk.metadata, chunk.path),
        )
        for i, chunk in enumerate(outcome.chunks, 1)
    ]

    if not hits:
        # Two different failures, and the caller needs to tell them apart: nothing was
        # retrieved at all (the filter is too narrow), or everything retrieved was
        # irrelevant (the corpus has nothing on this).
        detail = ("The filters matched no chunks to rank."
                  if outcome.retrieved == 0 else
                  f"Retrieved {outcome.retrieved} candidates; none scored as relevant.")
        return hits_model(**{**base, "status": "no_match", "query": query,
                             "best_score": outcome.best_score, "retrieved": outcome.retrieved,
                             "available": _available(store, resolved.resolutions),
                             "detail": detail})

    return hits_model(**{**base, "query": query, "hits": hits,
                         "facets": _facets_of(outcome.chunks, fields),
                         "best_score": outcome.best_score, "retrieved": outcome.retrieved})


def _meta_value(metadata: dict, field: str) -> str:
    value = metadata.get(field)
    return "" if value is None else str(value)


def _uri_for(store: str, metadata: dict, path: str) -> str:
    """
    A stable identifier for the file a chunk came from.

    Store-specific because the stored ``path`` means different things. On github it is
    repo-relative, so `yada://github/<path>` would not identify a file at all -- paths
    like `.document` and `README.md` recur across the 101 repositories. Prefixing the
    account and repo matches the on-disk `.repos` layout and is unique.

    research_library stores a path that already begins with `research_library/`, so the
    segment is dropped rather than repeated.
    """
    if store == GITHUB_DB_NAME:
        account, repo = metadata.get("account"), metadata.get("repo")
        prefix = "/".join(p for p in (account, repo) if p)
        return f"yada://{store}/{prefix}/{path}" if prefix else f"yada://{store}/{path}"
    trimmed = path[len(store) + 1:] if path.startswith(f"{store}/") else path
    return f"yada://{store}/{trimmed}"


def _describe(store: str, proposed: dict[str, str | None], vocab_model) -> Any:
    """
    The shared describe. Counts only, never content.

    Answered from the combination rows, which is why it can be filtered at all: the
    per-field marginals cannot answer a conjunction, and asking Chroma costs 3.8 s for
    a filter matching 384 chunks.
    """
    requested = {k: v for k, v in proposed.items() if v is not None}
    base = dict(status="ok", request="", filters_requested=requested)

    if not _store_is_built(store):
        return vocab_model(**{**base, "status": "store_empty",
                              "detail": f"The {store} vocabulary has never been built."})

    resolved = _resolve(store, proposed)
    base["filters_resolved"] = resolved.resolved

    if resolved.unresolvable:
        dead = ", ".join(f"{r.field}={r.proposed!r}" for r in resolved.unresolvable)
        return vocab_model(**{**base, "status": "unresolvable_filter",
                              "available": _available(store, resolved.resolutions),
                              "detail": f"{dead} matches no stored value. "
                                        f"`available` lists what exists."})

    base["filters_applied"] = resolved.applied
    documents, chunks = Vocabulary.counts(store, resolved.resolutions)
    facets = Vocabulary.facets(store, resolved.resolutions, fields=PUBLISHED_FILTERS[store])

    if chunks == 0:
        return vocab_model(**{**base, "status": "no_match",
                              "detail": "Each value exists, but nothing carries all of "
                                        "them together."})
    return vocab_model(**{**base, "facets": facets, "documents": documents, "chunks": chunks})


# ----------------------------------------------------------- generated descriptions

def _shelf_values() -> str:
    try:
        return ", ".join(sorted(Vocabulary.values(RESEARCH_LIBRARY_DB_NAME, "shelf")))
    except Exception:
        return "notes, posts, publications, jaynes, reading_list"


def _surnames() -> str:
    try:
        names = sorted(a for a, (_, kind) in
                       Vocabulary.aliases(RESEARCH_LIBRARY_DB_NAME, "authors").items()
                       if kind == "surname")
        return ", ".join(names)
    except Exception:
        return ""


def _counts(store: str) -> str:
    try:
        _, chunks = Vocabulary.counts(store)
        documents, _ = Vocabulary.counts(store)
        return f"{documents:,} files, {chunks:,} indexed chunks"
    except Exception:
        return "an indexed corpus"


def register(server) -> None:
    """
    Register the four tools.

    Uses ``add_tool`` rather than the decorator because the descriptions are built from
    the vocabulary at call time and a decorator takes a literal. Registration must come
    after the server exists, which is the opposite of the ``@apps.tool`` rule in
    server.py -- those are collected at construction.
    """
    surnames = _surnames()
    surname_line = (f" A surname alone is enough and is preferred -- it reaches every "
                    f"spelling of that name and every co-authored paper: {surnames}."
                    if surnames else "")

    def search_code(query: str, repo: str | None = None, ext: str | None = None,
                    limit: int = 10) -> CodeHits:
        return _search(GITHUB_DB_NAME, query, {"repo": repo, "ext": ext}, limit,
                       CodeHits, GithubMeta)

    def describe_code(repo: str | None = None, ext: str | None = None) -> CodeVocabulary:
        return _describe(GITHUB_DB_NAME, {"repo": repo, "ext": ext}, CodeVocabulary)

    def search_research_library(query: str, authors: str | None = None,
                                title: str | None = None, shelf: str | None = None,
                                limit: int = 10) -> LibraryHits:
        return _search(RESEARCH_LIBRARY_DB_NAME, query,
                       {"authors": authors, "title": title, "shelf": shelf}, limit,
                       LibraryHits, LibraryMeta)

    def describe_research_library(authors: str | None = None, title: str | None = None,
                                  shelf: str | None = None) -> LibraryVocabulary:
        return _describe(RESEARCH_LIBRARY_DB_NAME,
                         {"authors": authors, "title": title, "shelf": shelf},
                         LibraryVocabulary)

    server.add_tool(
        search_code, name="search_code",
        description=(
            "Search Troy Stribling's indexed code repositories by meaning and return "
            f"ranked excerpts with their file paths ({_counts(GITHUB_DB_NAME)}).\n"
            "- query: what to look for, in natural language.\n"
            "- repo: a repository name, or a GitHub account name to search everything "
            "under it. A partial name works. Omit to search every repository. "
            "Call describe_code to see what exists.\n"
            "- ext: a file extension such as '.py', or a language name such as 'Python', "
            "which maps to the extensions that language uses. Pass '(no extension)' for "
            "files that have none, such as LICENSE and Makefile. Omit to search all types.\n"
            "A value that matches nothing is reported with what does exist, and no "
            "search is run."),
    )

    server.add_tool(
        describe_code, name="describe_code",
        description=(
            "What the code repositories contain: repositories, file types and counts, "
            "under any filters given. No file contents. "
            "describe_code(repo='zgomot') answers 'what is this repository written in'. "
            "Call it before search_code when a name or language is uncertain."),
    )

    server.add_tool(
        search_research_library, name="search_research_library",
        description=(
            "Search Troy Stribling's research library -- papers, research notes and blog "
            f"posts -- by meaning, returning ranked excerpts ({_counts(RESEARCH_LIBRARY_DB_NAME)}).\n"
            "- query: what to look for, in natural language.\n"
            f"- authors: who wrote it.{surname_line}\n"
            "- title: a document title, in full or in part. Call "
            "describe_research_library to list them.\n"
            f"- shelf: one of {_shelf_values()}.\n"
            "A value that matches nothing is reported with what does exist, and no "
            "search is run."),
    )

    server.add_tool(
        describe_research_library, name="describe_research_library",
        description=(
            "What the research library contains: authors, titles, shelves and counts, "
            "under any filters given. No document contents. "
            "describe_research_library(shelf='jaynes') answers 'who wrote the papers on "
            "the Jaynes shelf'. Use it to find exact spellings before searching."),
    )

    logger.info("Document tools registered: search_code, describe_code, "
                "search_research_library, describe_research_library")
