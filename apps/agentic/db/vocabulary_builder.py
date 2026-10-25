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
from collections import defaultdict
from typing import Any, Iterator, Mapping

import chromadb

from apps.agentic.core.constants import (
    DB_PATH,
    GITHUB_COLLECTION_NAME,
    GITHUB_DB_NAME,
    RESEARCH_LIBRARY_COLLECTION_NAME,
    RESEARCH_LIBRARY_DB_NAME,
)
from apps.agentic.db.vocabulary import Vocabulary
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


def rebuild(store: str) -> dict[str, int]:
    """
    Rescan one store and replace its vocabulary. Returns {field: distinct values}.

    Safe to call repeatedly: the write is a single transaction that deletes the store's
    old rows first, so there is no window in which some values resolve and others do not.
    """
    fields = STORE_FIELDS[store]
    collection = open_collection(store)

    # One entry per distinct tuple of this store's fields -> [chunks, {file paths}].
    # This is the whole output: marginals, coverage and aliases are all derived from it
    # at read time (see Vocabulary.values / .aliases / .coverage), so there is one write
    # path and nothing that can fall out of step with anything else.
    combinations: dict[tuple[tuple[str, str], ...], list] = defaultdict(lambda: [0, set()])
    chunks = 0

    for metadata in iter_metadatas(collection):
        chunks += 1
        key = tuple((f, str(metadata.get(f))) for f in fields if metadata.get(f) is not None)
        entry = combinations[key]
        entry[0] += 1
        entry[1].add(metadata.get("path"))

    Vocabulary.replace_store(
        store=store,
        collection=STORE_COLLECTIONS[store],
        chunks=chunks,
        combinations=[(dict(k), n, len(paths)) for k, (n, paths) in combinations.items()],
    )
    return {"combinations": len(combinations), "chunks": chunks}


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
