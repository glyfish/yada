"""
The result contract for the document-store tools.

The SDK derives each tool's ``output_schema`` from its return annotation and populates
``structured_content`` automatically, so these models are the published contract, not a
convenience. Verified against mcp 2.3.0.

Four fields exist because of specific observed failures, and are worth keeping even when
they look like noise:

``filters_resolved``  the caller proposed `Matthaeus`; the search ran `$in` over five
                      author strings. Without this the widening is invisible.
``filters_relaxed``   a filter that matched nothing used to trigger a silent unfiltered
                      retry, so `repo:yada` returned chunks from `BAP3` and `alef` and
                      read as success.
``best_score``        separates *retrieved 8, best 0.05* from *retrieved nothing*. Those
                      are different problems with different fixes, and were identical.
``available``         turns a dead end into a next step: a value that matches nothing is
                      answered with what does exist.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

Status = Literal[
    "ok",                    # hits returned
    "no_match",              # searched, nothing relevant -- see best_score for which kind
    "unresolvable_filter",   # a value matches no stored value; NO search was performed
    "filters_relaxed",       # a term was dropped to avoid an empty conjunction
    "store_empty",           # the vocabulary has never been built for this store
    "retrieval_error",       # the retriever or ranker raised
]


class GithubMeta(BaseModel):
    """Keyed exactly as search_code's filters, so a hit can be narrowed by copying."""

    repo: str
    ext: str = Field(description="Including the leading dot; empty when the file has none")


class LibraryMeta(BaseModel):
    """Keyed exactly as search_research_library's filters."""

    authors: str = Field(description="The full author list as stored, comma-joined")
    title: str
    shelf: Literal["notes", "posts", "publications", "jaynes", "reading_list"]


class Hit[M](BaseModel):
    rank: int
    score: float = Field(ge=0.0, le=1.0,
                         description="Relevance within THIS result set; not comparable across calls")
    source: Literal["github", "research_library"] = Field(
        description="Implied by the tool, kept so a hit stays self-describing once "
                    "results from both stores are collated")
    path: str
    snippet: str
    metadata: M
    uri: str = Field(description="Stable identifier for the file, yada://{source}/{path}. "
                                 "An identifier for citing and de-duplicating, not yet a "
                                 "fetchable resource")


class Outcome(BaseModel):
    """What was asked, what actually ran, and how the two differ."""

    status: Status
    request: str = Field(description="The query argument as received, before any stripping. "
                                     "Echoed because a routing model tends to paraphrase, and "
                                     "a paraphrase that drops a filter is invisible otherwise")
    filters_requested: dict[str, str] = Field(default_factory=dict,
                                              description="What the caller proposed")
    filters_applied: dict = Field(default_factory=dict,
                                  description="What actually ran, including {'$in': [...]}")
    filters_resolved: dict[str, str] = Field(
        default_factory=dict,
        description="How each value resolved: 'exact', 'substring, 5 of 19', "
                    "\"account 'glyfish' -> 22 repositories\", 'no match'")
    filters_relaxed: dict[str, str] = Field(default_factory=dict,
                                            description="Terms dropped to avoid an empty result")
    available: dict[str, list[str]] = Field(
        default_factory=dict,
        description="On unresolvable_filter: the values that DO exist for that field")
    detail: str | None = Field(default=None,
                               description="One line of explanation when the status needs it")


class Hits[M](Outcome):
    query: str = Field(description="The text actually embedded")
    hits: list[Hit[M]] = Field(default_factory=list)
    facets: dict[str, dict[str, int]] = Field(
        default_factory=dict,
        description="Values present among THESE hits -- a free summary of what came back, "
                    "narrower than the store-wide picture a describe gives")
    best_score: float | None = Field(
        default=None,
        description="Highest relevance before filtering. null when nothing was retrieved "
                    "at all, which is a different problem from retrieving only weak hits")
    retrieved: int = Field(default=0, description="Candidates considered before ranking")


class StoreVocabulary(Outcome):
    """What a store holds, optionally under filters. No content, only counts."""

    facets: dict[str, dict[str, int]] = Field(
        default_factory=dict,
        description="Every filter's values with their chunk counts, over the filtered subset")
    documents: int = Field(default=0, description="Distinct files matching the filters")
    chunks: int = Field(default=0, description="Indexed chunks matching the filters")


class CodeHits(Hits[GithubMeta]):
    pass


class LibraryHits(Hits[LibraryMeta]):
    pass


class CodeVocabulary(StoreVocabulary):
    pass


class LibraryVocabulary(StoreVocabulary):
    pass
