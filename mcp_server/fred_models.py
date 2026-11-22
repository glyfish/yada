"""
The result contract for the FRED catalogue tools.

Mirrors ``document_models`` in shape -- an outcome envelope that says what was asked,
what actually ran, and how the two differ -- but does not inherit from it. The stores
have genuinely different failure modes, and a shared ``Status`` Literal would have to
carry both sets, so each is honest about its own.

What FRED has that the document stores do not:

``ambiguous_filter``  `category="Housing"` names FOUR categories -- 53,187 series under
                      Production & Business Activity, and 51 under Prices > CPI, which
                      is housing *inflation*. Merging them is wrong and picking the
                      biggest is wrong half the time, so the tool reports the candidates
                      and runs nothing. This is ``unresolvable_filter``'s mirror image:
                      there, nothing matched; here, too much did.
``total``             every hit list is truncated to ``limit``, and the top 10 of 53,187
                      reads exactly like the top 10 of 10 unless the count is published.
``fetch_tool``        each row names the MCP tool that fetches its observations, so a
                      listing stays actionable across the server boundary -- yada
                      searches, meida fetches. The pattern is meida's own
                      ``series_catalog`` retrieval block.

What it deliberately does NOT have: ``best_score``. Ranking here is FRED's popularity
score, which is a property of the series and not of the match, so a "best score" would
say nothing about whether the search worked.
"""

from __future__ import annotations

from datetime import date
from typing import Literal

from pydantic import BaseModel, Field

FredStatus = Literal[
    "ok",                    # series returned
    "no_match",              # searched, nothing matched
    "unresolvable_filter",   # a value matches nothing stored; NO search was performed
    "ambiguous_filter",      # a value matches several; NO search was performed
    "empty_request",         # neither query nor category given
]


class FredOutcome(BaseModel):
    """What was asked, what actually ran, and how the two differ."""

    status: FredStatus
    request: str = Field(
        description="The arguments as received, rendered for the log. Echoed because a "
                    "routing model paraphrases, and a paraphrase that drops a filter is "
                    "invisible otherwise")
    filters_requested: dict[str, str] = Field(
        default_factory=dict, description="What the caller proposed")
    filters_applied: dict[str, str] = Field(
        default_factory=dict,
        description="What actually ran. A category resolves to a SUBTREE, so this says "
                    "how many categories were searched, not just the one named")
    available: dict[str, list[str]] = Field(
        default_factory=dict,
        description="On unresolvable_filter or ambiguous_filter: the values that DO "
                    "exist, so a dead end becomes a next step")
    detail: str | None = Field(
        default=None, description="One line of explanation when the status needs it")


class FredSeries(BaseModel):
    """One series, carrying everything needed to choose it without a second call."""

    rank: int
    series_id: str = Field(description="Pass this to fetch_tool to get the observations")
    title: str
    frequency: str | None = Field(
        description="As FRED publishes it, e.g. 'Quarterly', 'Annual, As of January 1'. "
                    "46 distinct spellings exist, so filter on frequency_class instead")
    frequency_class: str | None = Field(
        description="Normalised, and what the `frequency` argument matches: annual, "
                    "monthly, quarterly, daily, weekly, semiannual, biweekly, other")
    units: str | None
    observation_start: date | None
    observation_end: date | None = Field(
        description="May be in the FUTURE for projection series such as CBO estimates")
    seasonal_adjustment: str | None = Field(
        description="Often the ONLY thing separating two rows: TXUR and TXURN are both "
                    "titled 'Unemployment Rate in Texas' and differ only here")
    popularity: int | None = Field(description="FRED's own usage score, 0-100. The sort key")
    category_path: str = Field(
        description="FRED's own curated path. Provenance, not a filter value -- pass "
                    "category to describe_fred to narrow")
    currently_relevant: bool | None = Field(
        description="False for discontinued series. Not filtered by default: popularity "
                    "already sinks them, and a dead series is sometimes the one wanted")
    fetch_tool: str = Field(
        default="fred_series_observations",
        description="The MCP tool that returns this series' observations")


class FredHits(FredOutcome):
    series: list[FredSeries] = Field(default_factory=list)
    total: int = Field(
        default=0,
        description="Matches BEFORE the limit was applied. The top 10 of 53,187 is not "
                    "the top 10 of 10, and nothing else in the reply says which it was")
    limit: int = Field(default=10)


class FredCategory(BaseModel):
    category_id: int
    category_path: str
    children: int = Field(description="Child categories directly beneath this one")
    series_here: int = Field(
        description="Series attached to THIS category. 177 categories hold series and "
                    "have children, so this and `children` are both non-zero there")
    series_in_subtree: int = Field(
        description="Series anywhere beneath it, deduplicated. What search_fred(category=) "
                    "would search")


class FredCategories(FredOutcome):
    """What the catalogue holds, as categories and counts. No series."""

    categories: list[FredCategory] = Field(default_factory=list)
    total: int = Field(default=0, description="Categories matched before the limit")
    limit: int = Field(default=25)
