"""
Unit tests for filter-value resolution.

The cases are drawn from live stores, not invented: a caller naming an author by
surname, an account name standing in for a repository, a truncated repository name,
and a file with no extension. Each one returned zero hits with no error before
resolution existed -- the failure this module was written to remove.

``resolve`` reads only through the two class caches, so these run with no database.
"""

import pytest

from apps.agentic.db.vocabulary import (
    NO_EXTENSION,
    Resolution,
    Vocabulary,
    split_authors,
    surname,
)

# Taken from the built vocabulary on 2026-10-24.
AUTHORS = {
    "Troy Stribling": 61,
    "Troy Stribling, W. H. Matthaeus": 40,
    "Troy Stribling, S. Oughton, W. H. Matthaeus": 33,
    "Sanjoy Ghosh, Troy Stribling, W. H. Matthaeus, Melvyn Goldstein": 21,
    "E. T. Jaynes": 804,
}
EXTENSIONS = {".py": 51_000, ".ipynb": 96_000, ".pyi": 300, ".pyx": 40, "": 1_995}
REPOS = {"zgomot": 1_200, "BlueCap": 900, "bokeh": 400}


@pytest.fixture(autouse=True)
def vocabulary():
    """Seed the caches directly; cleared afterwards so no test leaks into another."""
    Vocabulary._cache = {
        ("research_library", "authors"): dict(AUTHORS),
        ("github", "ext"): dict(EXTENSIONS),
        ("github", "repo"): dict(REPOS),
    }
    Vocabulary._alias_cache = {
        ("research_library", "authors"): {
            s: (tuple(sorted(v for v in AUTHORS if n in v)), "surname")
            for s, n in [("Matthaeus", "Matthaeus"), ("Jaynes", "Jaynes"),
                         ("Stribling", "Stribling")]
        },
        ("github", "repo"): {"glyfish": (("bokeh", "zgomot"), "account")},
        ("github", "ext"): {},
    }
    yield
    Vocabulary._cache = {}
    Vocabulary._alias_cache = {}


# --------------------------------------------------------------------- helpers

@pytest.mark.parametrize("name,expected", [
    ("W. H. Matthaeus", "Matthaeus"),
    ("William H. Matthaeus", "Matthaeus"),   # the variant spelling reduces the same way
    ("E. T. Jaynes", "Jaynes"),
    ("Jaynes", "Jaynes"),
    ("", ""),
])
def test_surname(name, expected):
    assert surname(name) == expected


@pytest.mark.parametrize("value,expected", [
    ("Troy Stribling", ["Troy Stribling"]),
    ("Troy Stribling, W. H. Matthaeus", ["Troy Stribling", "W. H. Matthaeus"]),
    ("A. Smith and B. Jones", ["A. Smith", "B. Jones"]),       # the corpus has one of these
    ("A. Smith, B. Jones, and C. Lee", ["A. Smith", "B. Jones", "C. Lee"]),
    ("  Troy Stribling ,  ", ["Troy Stribling"]),
])
def test_split_authors(value, expected):
    assert split_authors(value) == expected


# ------------------------------------------------------------------ resolution

def test_surname_reaches_every_spelling():
    """The original failure: 'Matthaeus' is not a stored value, so equality found none."""
    r = Vocabulary.resolve("research_library", "authors", "Matthaeus")
    assert r.kind == "alias"
    assert r.alias_kind == "surname"
    assert len(r.values) == 3
    assert all("Matthaeus" in v for v in r.values)
    assert r.where() == {"authors": {"$in": list(r.values)}}


def test_sole_author_resolves_to_one_value():
    r = Vocabulary.resolve("research_library", "authors", "Jaynes")
    assert r.values == ("E. T. Jaynes",)
    assert r.where() == {"authors": "E. T. Jaynes"}   # one value, no $in


def test_exact_value_wins_over_alias():
    """A caller who passes a stored value back verbatim gets it, not its surname's set."""
    r = Vocabulary.resolve("research_library", "authors", "Troy Stribling")
    assert r.kind == "exact"
    assert r.values == ("Troy Stribling",)


def test_account_reaches_its_repositories():
    """'glyfish' shares no characters with 'bokeh', so only an alias can reach it."""
    r = Vocabulary.resolve("github", "repo", "glyfish")
    assert r.kind == "alias"
    assert r.alias_kind == "account"        # the tool layer refuses this for enumeration
    assert r.values == ("bokeh", "zgomot")


def test_truncated_repository_resolves_by_substring():
    r = Vocabulary.resolve("github", "repo", "zgom")
    assert r.kind == "substring"
    assert r.values == ("zgomot",)


def test_unknown_value_resolves_to_nothing():
    """Reportable, not silent: no where clause is built and the caller is told."""
    r = Vocabulary.resolve("github", "repo", "nonesuch")
    assert r.kind == "none"
    assert not r.matched
    assert r.where() is None


# ------------------------------------------------------------------ extensions

@pytest.mark.parametrize("proposed", ["py", ".py", "PY", ".PY"])
def test_extension_spelling_is_normalised(proposed):
    """Dot and case are spelling. Without this, 'py' widens to .ipynb/.py/.pyi/.pyx."""
    r = Vocabulary.resolve("github", "ext", proposed)
    assert r.kind == "exact"
    assert r.values == (".py",)


@pytest.mark.parametrize("proposed", ["", NO_EXTENSION])
def test_blank_extension_selects_files_without_one(proposed):
    """A blank ext means LICENSE and Makefile -- not 'every extension', which is omission."""
    r = Vocabulary.resolve("github", "ext", proposed)
    assert r.kind == "empty"
    assert r.where() == {"ext": ""}


def test_unknown_extension_resolves_to_nothing():
    assert Vocabulary.resolve("github", "ext", "notarealext").kind == "none"


# ---------------------------------------------------------------------- output

def test_available_orders_by_size_and_names_the_blank():
    available = Vocabulary.available("github", "ext")
    assert available[0] == ".ipynb"                 # 96,000 chunks, the largest
    assert NO_EXTENSION in available                # never surfaced as an empty string
    assert "" not in available


def test_where_is_none_when_nothing_matched():
    assert Resolution("repo", "x", (), "none").where() is None
