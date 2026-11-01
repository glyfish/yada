"""
Build the FRED series catalogue in Postgres from the source YAML.

Reads `clients/fred/{categories,series}/*.yaml` -- the same files the Chroma loader
reads -- and writes `fred_series`, `fred_category`, `fred_series_category` and
`fred_frequency_class`. It deliberately does **not** read the Chroma store: Postgres
replaces it, and a loader that depended on it would have to be rewritten the day it goes.

Two columns are derived here because neither can be reconstructed by a query:

``frequency_class``
    The source spells 41 variants of about eight frequencies. Filtering on the raw
    string drops the 1,109 series spelled "Quarterly, End of Quarter" or
    "Quarterly, End of Period" from any search for quarterly data -- silently, since a
    narrower result looks like a narrower corpus.

``currently_relevant``
    Two-thirds of the store is discontinued, so this is the most selective filter
    available. It cannot be a flat date. Annual is the largest class (56,170 series) and
    only 176 end in 2025 or later, so `observation_end >= '2025-01-01'` marks 22,200
    current annual series as dead, while keeping a daily series that stopped eleven
    months ago. Currency is measured in **periods**:

        currently_relevant  <=>  observation_end >= p95(observation_end within class)
                                                    - 2 x period_days(class)

    p95 rather than max because projections skew the tail -- annual's max is 2030-01-01
    against a p95 of 2024-01-01, so a max-anchored cutoff would sit in 2028 and match
    nothing. Two periods of slack: one for ordinary publication lag, one for the store's
    own staleness. Self-calibrating, so a fresher load moves every cutoff together.

The derived cutoffs are stored in `fred_frequency_class` so a tool can state the
definition it applied instead of hiding it behind a boolean.
"""

from __future__ import annotations

import math
import os
import re
from collections import defaultdict
from datetime import date, datetime, timedelta
from typing import Any, Iterator

import yaml
from sqlalchemy import MetaData, Table, create_engine, delete
from sqlalchemy.engine import Engine

from apps.agentic.core.constants import FRED_LOCAL_PATH
from apps.core.environment import db_url as environment_db_url
from lib.logger import get_logger

logger = get_logger("YADA")

#: Nominal period of each frequency class, in days. The key is matched against the
#: leading word of FRED's frequency string, so "Quarterly, End of Period" is quarterly.
#: Order matters only in that longer keys must be tried first (see _CLASS_KEYS).
PERIOD_DAYS: dict[str, int] = {
    "daily": 1,
    "weekly": 7,
    "biweekly": 14,
    "bimonthly": 61,
    "biennial": 730,
    "monthly": 30,
    "quarterly": 91,
    "semiannual": 182,
    "annual": 365,
    "decadal": 3650,
}

#: Longest first, so "biweekly" is not classified as "weekly" and "biennial" not as
#: "annual" by a prefix test that happens to run in the wrong order.
_CLASS_KEYS = sorted(PERIOD_DAYS, key=len, reverse=True)

OTHER = "other"

#: Slack allowed before a series counts as discontinued, in periods of its own class.
CURRENCY_SLACK_PERIODS = 2

#: Percentile of observation_end used as each class's reference point.
CURRENCY_PERCENTILE = 0.95


def frequency_class(frequency: str | None) -> str:
    """
    The frequency's class, from the leading word of FRED's string.

    "Quarterly", "Quarterly, End of Quarter" and "Quarterly, End of Period" are one
    thing to a caller asking for quarterly data, and three to an equality filter.
    """
    head = re.split(r"[,(]", (frequency or "").strip())[0]
    head = head.strip().lower().replace("-", "").replace(" ", "")
    for key in _CLASS_KEYS:
        if head.startswith(key):
            return key
    return OTHER


def _date(value: Any) -> date | None:
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    if isinstance(value, datetime):
        return value.date()
    text = str(value or "").strip()
    if not text:
        return None
    try:
        return date.fromisoformat(text[:10])
    except ValueError:
        return None


def _timestamp(value: Any) -> datetime | None:
    text = str(value or "").strip()
    if not text:
        return None
    try:
        return datetime.fromisoformat(text)
    except ValueError:
        return None


def _int(value: Any) -> int | None:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def source_files() -> list[str]:
    """Every category file that has a matching series file."""
    categories = os.path.join(FRED_LOCAL_PATH, "categories")
    series = os.path.join(FRED_LOCAL_PATH, "series")
    if not os.path.isdir(categories):
        return []
    return sorted(
        name for name in os.listdir(categories)
        if name.endswith((".yaml", ".yml"))
        and os.path.isfile(os.path.join(series, name))
    )


def _load_yaml(path: str) -> list[dict]:
    with open(path, encoding="utf-8", errors="ignore") as handle:
        parsed = yaml.safe_load(handle) or []
    if not isinstance(parsed, list):
        parsed = [parsed]
    return [item for item in parsed if isinstance(item, dict)]


def iter_source() -> Iterator[tuple[dict, dict]]:
    """
    Yield (series, category) for every series in every file.

    A series is yielded once per category it belongs to -- that is the source's shape,
    and collapsing it is this module's job, not the reader's.
    """
    for name in source_files():
        categories = _load_yaml(os.path.join(FRED_LOCAL_PATH, "categories", name))
        groups = _load_yaml(os.path.join(FRED_LOCAL_PATH, "series", name))

        by_leaf = {c.get("leaf_id"): c for c in categories if c.get("leaf_id") is not None}

        for group in groups:
            category_id = group.get("category_id")
            matched = by_leaf.get(category_id, {})
            path = matched.get("path") or []
            category = {
                "category_id": _int(category_id),
                "category_name": group.get("category_name") or matched.get("leaf_name"),
                "category_path": " > ".join(
                    p.get("name", "") if isinstance(p, dict) else str(p) for p in path
                ).strip() or None,
            }
            for series in group.get("seriess") or []:
                if isinstance(series, dict) and series.get("id"):
                    yield series, category


def _percentile(values: list[date], fraction: float) -> date | None:
    """
    Nearest-rank percentile: the smallest value at or above `fraction` of the data.

    `ordered[int(n * fraction)]` is off by one -- for 95 values at 2024 and 5 at 2030 it
    returns the 96th, i.e. 2030, which is precisely the projection tail this percentile
    exists to exclude. On the live data the two agree, so the error is invisible until
    the tail is wide enough to matter.
    """
    if not values:
        return None
    ordered = sorted(values)
    rank = max(1, math.ceil(fraction * len(ordered)))
    return ordered[min(len(ordered), rank) - 1]


def currency_cutoffs(series: dict[str, dict]) -> dict[str, dict]:
    """
    Per class: the p95 observation_end, the derived cutoff, and the series count.

    Separated from the write so it can be tested without a database -- the rule is the
    part worth testing, and it is the part that was wrong before it was measured.
    """
    ends: dict[str, list[date]] = defaultdict(list)
    counts: dict[str, int] = defaultdict(int)
    for row in series.values():
        klass = row["frequency_class"]
        counts[klass] += 1
        if row["observation_end"]:
            ends[klass].append(row["observation_end"])

    out: dict[str, dict] = {}
    for klass, count in counts.items():
        period = PERIOD_DAYS.get(klass, 365)
        p95 = _percentile(ends.get(klass, []), CURRENCY_PERCENTILE)
        cutoff = p95 - timedelta(days=CURRENCY_SLACK_PERIODS * period) if p95 else None
        out[klass] = {
            "frequency_class": klass,
            "period_days": period,
            "p95_observation_end": p95,
            "currency_cutoff": cutoff,
            "series_count": count,
        }
    return out


def read_source() -> tuple[dict[str, dict], dict[int, dict], set[tuple[str, int]]]:
    """Parse the YAML into (series by id, categories by id, memberships)."""
    series: dict[str, dict] = {}
    categories: dict[int, dict] = {}
    memberships: set[tuple[str, int]] = set()

    for raw, category in iter_source():
        series_id = str(raw["id"])
        if series_id not in series:
            frequency = raw.get("frequency")
            series[series_id] = {
                "series_id": series_id,
                "series_title": raw.get("title") or "Unknown Series",
                "units": raw.get("units"),
                "frequency": frequency,
                "frequency_class": frequency_class(frequency),
                "seasonal_adjustment": raw.get("seasonal_adjustment"),
                "observation_start": _date(raw.get("observation_start")),
                "observation_end": _date(raw.get("observation_end")),
                "last_updated": _timestamp(raw.get("last_updated")),
                "popularity": _int(raw.get("popularity")),
                "currently_relevant": False,
            }
        category_id = category["category_id"]
        if category_id is not None:
            if category_id not in categories and category.get("category_name"):
                categories[category_id] = category
            if category_id in categories:
                memberships.add((series_id, category_id))

    return series, categories, memberships


def _engine(url: str | None = None) -> Engine:
    return create_engine(url or environment_db_url(), pool_pre_ping=True)


def build(url: str | None = None) -> dict[str, int]:
    """
    Rebuild the catalogue from the source YAML. One transaction, replacing everything.

    Atomic for the same reason `Vocabulary.replace_store` is: a half-written catalogue
    resolves some values and not others, which is the silent partial failure this whole
    design exists to remove.
    """
    series, categories, memberships = read_source()
    classes = currency_cutoffs(series)

    for row in series.values():
        cutoff = classes[row["frequency_class"]]["currency_cutoff"]
        row["currently_relevant"] = bool(
            cutoff and row["observation_end"] and row["observation_end"] >= cutoff
        )

    engine = _engine(url)
    metadata = MetaData()
    metadata.reflect(bind=engine, only=[
        "fred_series", "fred_category", "fred_series_category", "fred_frequency_class"])
    t_series = metadata.tables["fred_series"]
    t_category = metadata.tables["fred_category"]
    t_member = metadata.tables["fred_series_category"]
    t_class = metadata.tables["fred_frequency_class"]

    with engine.begin() as conn:
        # Membership first: it references both of the others.
        conn.execute(delete(t_member))
        conn.execute(delete(t_series))
        conn.execute(delete(t_category))
        conn.execute(delete(t_class))

        if categories:
            conn.execute(t_category.insert(), list(categories.values()))
        if series:
            rows = list(series.values())
            for start in range(0, len(rows), 5_000):
                conn.execute(t_series.insert(), rows[start:start + 5_000])
        if memberships:
            pairs = [{"series_id": s, "category_id": c} for s, c in sorted(memberships)]
            for start in range(0, len(pairs), 5_000):
                conn.execute(t_member.insert(), pairs[start:start + 5_000])
        if classes:
            conn.execute(t_class.insert(), list(classes.values()))

    current = sum(1 for r in series.values() if r["currently_relevant"])
    logger.info(
        f"FRED catalogue: {len(series):,} series, {len(categories):,} categories, "
        f"{len(memberships):,} memberships, {current:,} currently relevant "
        f"({100 * current / max(1, len(series)):.1f}%)"
    )
    return {
        "series": len(series),
        "categories": len(categories),
        "memberships": len(memberships),
        "currently_relevant": current,
    }
