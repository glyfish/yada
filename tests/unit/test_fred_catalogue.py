"""
Unit tests for the two FRED columns that are derived rather than copied.

Both encode a measurement, and both were wrong in the obvious form before it was taken:
`frequency = 'Quarterly'` drops a thousand quarterly series, and a flat date cutoff for
"currently relevant" marks 22,200 current annual series as dead. The tests below are
written against those two failures rather than against the happy path.

No database -- the rules are pure functions over parsed rows, which is why they were
separated from the write.
"""

from datetime import date

import pytest

from apps.agentic.db import fred_catalogue as fc


# ------------------------------------------------------------ frequency_class

@pytest.mark.parametrize("raw,expected", [
    # The three spellings that made an equality filter drop 1,109 quarterly series.
    ("Quarterly", "quarterly"),
    ("Quarterly, End of Quarter", "quarterly"),
    ("Quarterly, End of Period", "quarterly"),
    # Prefix collisions: a naive startswith in the wrong order makes these weekly
    # and annual respectively.
    ("Biweekly", "biweekly"),
    ("Biweekly, Ending Wednesday", "biweekly"),
    ("Biennial", "biennial"),
    ("Weekly, Ending Wednesday", "weekly"),
    ("Semiannual", "semiannual"),
    ("Annual", "annual"),
    ("Daily, 7-Day", "daily"),
    ("Monthly", "monthly"),
    # Unparseable must land somewhere nameable rather than guess.
    ("Every 20 Years", fc.OTHER),
    ("", fc.OTHER),
    (None, fc.OTHER),
])
def test_frequency_class(raw, expected):
    assert fc.frequency_class(raw) == expected


def test_biweekly_is_not_weekly():
    """
    The ordering guard, stated as its own case because it is invisible in review.

    `_CLASS_KEYS` is sorted longest-first; a plain dict iteration would classify
    "Biweekly" as weekly on any Python that happened to visit "weekly" first.
    """
    assert fc.frequency_class("Biweekly") != fc.frequency_class("Weekly")
    assert fc.frequency_class("Biennial") != fc.frequency_class("Annual")


# ----------------------------------------------------------- currency cutoffs

def series(klass, end, n=1, start=0):
    """n synthetic series of one class, all ending on the same date."""
    return {
        f"{klass}-{start + i}": {
            "frequency_class": klass,
            "observation_end": end,
            "observation_start": date(1950, 1, 1),
        }
        for i in range(n)
    }


def test_the_cutoff_is_p95_not_max():
    """
    The projection trap. Annual's max is 2030-01-01 against a p95 of 2024-01-01, so a
    max-anchored cutoff lands in 2028 and matches nothing. 95 series end in 2024 and
    five in 2030; the cutoff must follow the 95.
    """
    rows = {**series("annual", date(2024, 1, 1), 95),
            **series("annual", date(2030, 1, 1), 5, start=95)}
    cutoff = fc.currency_cutoffs(rows)["annual"]["currency_cutoff"]
    assert cutoff == date(2022, 1, 1)          # p95 2024-01-01 minus two 365-day periods
    assert cutoff < date(2024, 1, 1)           # so the bulk of the class qualifies


def test_an_annual_series_ending_last_year_is_current():
    """
    The regression this column exists for.

    A flat `observation_end >= '2025-01-01'` marked 22,200 annual series as dead --
    99.7% of the largest class in the store -- because an annual series reporting 2024
    is exactly on schedule.
    """
    rows = series("annual", date(2024, 1, 1), 100)
    cutoff = fc.currency_cutoffs(rows)["annual"]["currency_cutoff"]
    assert date(2024, 1, 1) >= cutoff


def test_a_daily_series_ending_last_year_is_not_current():
    """The same date, the other verdict -- which is the whole point of per-class slack."""
    rows = {**series("daily", date(2026, 1, 2), 100),
            **series("daily", date(2025, 1, 10), 1, start=100)}
    cutoff = fc.currency_cutoffs(rows)["daily"]["currency_cutoff"]
    assert date(2025, 1, 10) < cutoff
    assert date(2026, 1, 2) >= cutoff


def test_slack_scales_with_the_period():
    """Two periods, so a longer period buys proportionally more tolerance."""
    cuts = fc.currency_cutoffs({**series("daily", date(2026, 1, 1), 10),
                                **series("annual", date(2026, 1, 1), 10, start=10)})
    daily_slack = date(2026, 1, 1) - cuts["daily"]["currency_cutoff"]
    annual_slack = date(2026, 1, 1) - cuts["annual"]["currency_cutoff"]
    assert daily_slack.days == 2
    assert annual_slack.days == 730


def test_a_class_with_no_end_dates_gets_no_cutoff():
    """None, not a date -- an invented cutoff would silently classify every member."""
    rows = {"x": {"frequency_class": "other", "observation_end": None,
                  "observation_start": None}}
    out = fc.currency_cutoffs(rows)["other"]
    assert out["currency_cutoff"] is None and out["series_count"] == 1


def test_every_class_present_is_counted():
    rows = {**series("annual", date(2024, 1, 1), 3),
            **series("monthly", date(2025, 11, 1), 7, start=3)}
    out = fc.currency_cutoffs(rows)
    assert out["annual"]["series_count"] == 3
    assert out["monthly"]["series_count"] == 7
    assert out["monthly"]["period_days"] == fc.PERIOD_DAYS["monthly"]


# ------------------------------------------------------------------- parsing

@pytest.mark.parametrize("raw,expected", [
    ("1955-01-01", date(1955, 1, 1)),
    ("1955-01-01T00:00:00", date(1955, 1, 1)),
    ("", None), (None, None), ("not a date", None),
])
def test_dates_parse_or_return_none(raw, expected):
    assert fc._date(raw) == expected


@pytest.mark.parametrize("raw,expected", [("7", 7), (7, 7), ("", None), (None, None)])
def test_popularity_parses_or_returns_none(raw, expected):
    assert fc._int(raw) == expected
