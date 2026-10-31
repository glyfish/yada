"""
Unit tests for keeping the vocabulary in step with the store it describes.

The vocabulary is a snapshot of Chroma's metadata held in Postgres, and the tools
resolve filters against the snapshot. Every failure here is therefore the same shape: a
value that exists is reported as not existing, authoritatively and with a facet listing
to prove it, while unfiltered search still works -- so nothing errors and nothing in the
response says the answer is wrong.

Three mechanisms keep that from happening, and each is tested against the specific way
it used to fail:

- the loaders rebuild after a write (nothing called ``rebuild`` at all);
- ``rows`` revalidates against ``built_at`` (the rows were read once per process, so a
  rebuild in the loader's process never reached the server's);
- ``_staleness_note`` reports a store that changed with no rebuild (``is_stale`` had no
  callers either).

No database: the reads are driven through the class caches, and an engine that raises
stands in for one, so a test that touches the database fails loudly instead of silently
needing one.
"""

import logging

import pytest

from apps.agentic.core.document_loaders.chroma_document_loader import ChromaDocumentLoader
from apps.agentic.db import vocabulary_builder
from apps.agentic.db.vocabulary import Vocabulary
from mcp_server import document_tools

STORE = "research_library"
ROWS = [({"shelf": "notes", "authors": "E. T. Jaynes"}, 804, 3)]
BUILT = "2026-10-31T18:00:00"
LATER = "2026-10-31T19:00:00"


class Boom(RuntimeError):
    """Raised by anything a fresh cache must not reach."""


@pytest.fixture(autouse=True)
def caches(monkeypatch):
    """A warm, self-consistent cache, and an engine that must not be used."""
    Vocabulary._rows_cache = {STORE: list(ROWS)}
    Vocabulary._built_at_cache = {STORE: BUILT}
    Vocabulary._cache = {(STORE, "shelf"): {"notes": 804}}
    Vocabulary._alias_cache = {(STORE, "authors"): {"Jaynes": (("E. T. Jaynes",), "surname")}}
    # Non-None so the reflected-table assertion passes and the engine is what the read
    # reaches first; the engine then refuses, which is how a test proves it re-read.
    monkeypatch.setattr(Vocabulary, "_combination", object())
    monkeypatch.setattr(Vocabulary, "_engine_or_raise",
                        classmethod(lambda cls: (_ for _ in ()).throw(Boom("read the database"))))
    document_tools._size_checked.clear()
    yield
    Vocabulary._rows_cache = {}
    Vocabulary._built_at_cache = {}
    Vocabulary._cache = {}
    Vocabulary._alias_cache = {}
    document_tools._size_checked.clear()


def stamp(monkeypatch, value):
    monkeypatch.setattr(Vocabulary, "_built_at", classmethod(lambda cls, store: value))


# ------------------------------------------------------- rows() revalidation

def test_unchanged_build_serves_the_cache_without_reading(monkeypatch):
    """The common case must stay one small SELECT, not a re-read of the rows."""
    stamp(monkeypatch, BUILT)
    assert Vocabulary.rows(STORE) == ROWS


def test_a_rebuild_elsewhere_drops_the_cache(monkeypatch):
    """
    The bug this was written for: the loader rebuilt in its own process, so the
    server's rows -- read once at startup -- stayed behind for as long as it ran.
    """
    stamp(monkeypatch, LATER)
    with pytest.raises(Boom):            # i.e. it went back to the database
        Vocabulary.rows(STORE)
    assert STORE not in Vocabulary._rows_cache
    assert Vocabulary._built_at_cache[STORE] == LATER


def test_a_vocabulary_that_vanished_drops_the_cache(monkeypatch):
    """A store whose rows were deleted must not keep answering from memory."""
    stamp(monkeypatch, None)
    with pytest.raises(Boom):
        Vocabulary.rows(STORE)
    assert STORE not in Vocabulary._built_at_cache


def test_stale_rows_take_the_derived_reads_with_them(monkeypatch):
    """
    Values and aliases are memoised separately, so invalidating only the rows would
    leave the reads that resolution actually uses answering from the old build.
    """
    stamp(monkeypatch, LATER)
    with pytest.raises(Boom):
        Vocabulary.rows(STORE)
    assert Vocabulary._cache == {}
    assert Vocabulary._alias_cache == {}


def test_forget_leaves_other_stores_alone():
    Vocabulary._rows_cache["github"] = [({"repo": "zgomot"}, 1, 1)]
    Vocabulary._cache[("github", "repo")] = {"zgomot": 1}
    Vocabulary.forget(STORE)
    assert set(Vocabulary._rows_cache) == {"github"}
    assert set(Vocabulary._cache) == {("github", "repo")}


# --------------------------------------------- the loader's refresh after a write

class Stub:
    """Enough of a loader for the refresh: it reads only the store name."""
    def __init__(self, db_name):
        self._db_name = db_name

    refresh_vocabulary = ChromaDocumentLoader.refresh_vocabulary


def test_stores_outside_the_vocabulary_are_skipped(monkeypatch):
    """`fred` and `etf` are bound for Postgres and never get rows, so a rebuild
    would raise KeyError on STORE_FIELDS rather than do nothing."""
    monkeypatch.setattr(vocabulary_builder, "rebuild",
                        lambda store: pytest.fail(f"rebuilt {store}"))
    Stub("fred").refresh_vocabulary()
    Stub("etf").refresh_vocabulary()


def test_a_write_rebuilds_its_own_store(monkeypatch):
    called = []
    monkeypatch.setattr(Vocabulary, "ensure_initialized", classmethod(lambda cls: None))
    monkeypatch.setattr(vocabulary_builder, "rebuild",
                        lambda store: called.append(store) or {"combinations": 64, "chunks": 4875})
    Stub(STORE).refresh_vocabulary()
    assert called == [STORE]


def test_a_failed_rebuild_is_logged_not_raised(monkeypatch, caplog):
    """
    The documents are in Chroma by this point, so raising would report a failed load
    for a load that succeeded -- the same wrong answer pointed the other way.
    """
    monkeypatch.setattr(Vocabulary, "ensure_initialized", classmethod(lambda cls: None))
    monkeypatch.setattr(vocabulary_builder, "rebuild",
                        lambda store: (_ for _ in ()).throw(Boom("postgres is down")))
    with caplog.at_level(logging.ERROR, logger="YADA"):
        Stub(STORE).refresh_vocabulary()
    assert "AHEAD of its vocabulary" in caplog.text


# ------------------------------------------------------------ the backstop note

def test_a_store_that_changed_without_a_rebuild_is_reported(monkeypatch):
    monkeypatch.setattr(vocabulary_builder, "is_stale", lambda store: True)
    note = document_tools._staleness_note(STORE)
    assert note is not None and "out of date" in note


def test_the_size_check_runs_once_per_process(monkeypatch):
    """`collection.count()` is 3.8 s on github, so it must not be paid per call."""
    calls = []
    monkeypatch.setattr(vocabulary_builder, "is_stale",
                        lambda store: calls.append(store) or True)
    assert document_tools._staleness_note(STORE) is not None
    assert document_tools._staleness_note(STORE) is None
    assert calls == [STORE]


def test_a_current_vocabulary_says_nothing(monkeypatch):
    monkeypatch.setattr(vocabulary_builder, "is_stale", lambda store: False)
    assert document_tools._staleness_note(STORE) is None


def test_a_broken_check_never_breaks_a_search(monkeypatch):
    """A backstop that can fail a working search is worse than the gap it covers."""
    monkeypatch.setattr(vocabulary_builder, "is_stale",
                        lambda store: (_ for _ in ()).throw(Boom("chroma is gone")))
    assert document_tools._staleness_note(STORE) is None


@pytest.mark.parametrize("detail,note,expected", [
    ("a", "b", "a b"),
    ("a", None, "a"),
    (None, "b", "b"),
    (None, None, None),
])
def test_a_note_joins_whatever_detail_exists(detail, note, expected):
    assert document_tools._with_note(detail, note) == expected
