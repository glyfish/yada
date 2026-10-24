"""
Scans a Chroma collection and writes its vocabulary to Postgres.

Separate from ``vocabulary`` so the read path -- which the MCP server runs on every
call -- does not import chromadb or open a 415,006-chunk store. This module is used by
the loader after a document is added, and by the staleness check at first use.

The scan is a full pass over the collection's metadata: 33.5 s for github, 0.2 s for
research_library. That cost is why the result is persisted rather than computed live.
"""

from __future__ import annotations

import os
from collections import Counter, defaultdict
from typing import Any, Iterator, Mapping

import chromadb

from apps.agentic.core.constants import (
    DB_PATH,
    GITHUB_COLLECTION_NAME,
    GITHUB_DB_NAME,
    RESEARCH_LIBRARY_COLLECTION_NAME,
    RESEARCH_LIBRARY_DB_NAME,
)
from apps.agentic.db.vocabulary import Vocabulary, split_authors, surname
from lib.logger import get_logger

logger = get_logger("YADA")

#: SQLite binds one variable per returned id, and SQLITE_MAX_VARIABLE_NUMBER is 32766 --
#: a larger page raises "too many SQL variables" rather than returning fewer rows.
_PAGE = 20_000

#: The fields worth indexing. Every published filter must be here or it cannot be
#: resolved -- but the reverse does not hold. ``account`` is indexed and deliberately
#: NOT a parameter: a name is either an account or a repository and never both, so the
#: server classifies it. Indexing it is what lets a refusal say how much an account
#: holds, and what ``repo="glyfish"`` is ultimately applied against.
STORE_FIELDS: dict[str, tuple[str, ...]] = {
    GITHUB_DB_NAME: ("repo", "ext", "account"),
    RESEARCH_LIBRARY_DB_NAME: ("authors", "title", "shelf"),
}

STORE_COLLECTIONS: dict[str, str] = {
    GITHUB_DB_NAME: GITHUB_COLLECTION_NAME,
    RESEARCH_LIBRARY_DB_NAME: RESEARCH_LIBRARY_COLLECTION_NAME,
}


def open_collection(store: str) -> Any:
    """
    The raw chromadb collection, opened without an embedding function.

    ``.get()`` never embeds, so the builder needs no API key -- which keeps a rebuild
    runnable from the loader and from a test without one.
    """
    client = chromadb.PersistentClient(path=os.path.join(DB_PATH, store))
    return client.get_collection(STORE_COLLECTIONS[store])


def iter_metadatas(collection: Any, page: int = _PAGE) -> Iterator[Mapping[str, Any]]:
    """Every chunk's metadata, paged."""
    offset = 0
    while True:
        batch = collection.get(limit=page, offset=offset, include=["metadatas"])
        metadatas = batch.get("metadatas") or []
        if not metadatas:
            return
        for m in metadatas:
            if m:
                yield m
        if len(metadatas) < page:
            return
        offset += len(metadatas)


def _aliases_for(store: str, values: Mapping[str, Mapping[str, int]],
                 repo_accounts: Mapping[str, set[str]]) -> list[tuple[str, str, str, str]]:
    """
    (field, alias, value, kind) rows -- the names a caller is likely to use that are not
    themselves stored values.

    Two cases, both drawn from observed failures:

    surname   'Matthaeus' is not a stored value; the stored value is the whole author
              list, 'Troy Stribling, William H. Matthaeus'. Substring would also find it,
              but by characters rather than by name -- surname 'Ng' is a substring of
              'Young'. Token-exact first, substring only as a fallback.

    account   'glyfish' is not a repo and shares no characters with most of its repos, so
              substring cannot reach them. The alias is how an account name resolves to
              the repositories it holds.
    """
    rows: list[tuple[str, str, str, str]] = []
    if store == RESEARCH_LIBRARY_DB_NAME:
        seen: set[tuple[str, str]] = set()
        for value in values.get("authors", {}):
            for name in split_authors(value):
                key = (surname(name), value)
                if key not in seen:
                    seen.add(key)
                    rows.append(("authors", key[0], value, "surname"))
    if store == GITHUB_DB_NAME:
        for repo, accounts in repo_accounts.items():
            for account in accounts:
                rows.append(("repo", account, repo, "account"))
    return rows


def rebuild(store: str) -> dict[str, int]:
    """
    Rescan one store and replace its vocabulary. Returns {field: distinct values}.

    Safe to call repeatedly: the write is a single transaction that deletes the store's
    old rows first, so there is no window in which some values resolve and others do not.
    """
    fields = STORE_FIELDS[store]
    collection = open_collection(store)

    counts: dict[str, Counter[str]] = {f: Counter() for f in fields}
    present: Counter[str] = Counter()
    repo_accounts: dict[str, set[str]] = defaultdict(set)
    chunks = 0

    for metadata in iter_metadatas(collection):
        chunks += 1
        for field in fields:
            value = metadata.get(field)
            if value is None:
                continue
            counts[field][str(value)] += 1
            present[field] += 1
        if store == GITHUB_DB_NAME:
            repo, account = metadata.get("repo"), metadata.get("account")
            if repo and account:
                repo_accounts[str(repo)].add(str(account))

    Vocabulary.replace_store(
        store=store,
        collection=STORE_COLLECTIONS[store],
        chunks=chunks,
        values={f: dict(c) for f, c in counts.items()},
        field_chunks=dict(present),
        aliases=_aliases_for(store, counts, repo_accounts),
    )
    return {f: len(c) for f, c in counts.items()}


def is_stale(store: str) -> bool:
    """
    Whether the collection has changed size since the vocabulary was built.

    Checked at first use rather than at boot: ``collection.count()`` alone costs 3.8 s on
    github, and a server that stays up for days should not pay that on every restart.
    A size match is not proof the contents are unchanged -- a replaced document of equal
    chunk count would slip through -- but the loader rebuilds explicitly after a write,
    so this only has to catch a store rebuilt behind the server's back.
    """
    info = Vocabulary.scan_info(store)
    if info is None:
        return True
    return info[1] != open_collection(store).count()
