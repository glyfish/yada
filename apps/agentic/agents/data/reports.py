"""
Report operations with no LLM in them: resolve a reference, create a report.

Both are things three different doors need — the browser, the MCP server and the
chat agent — and neither needs a model. They live here, beside
`series_fetch.fetch_series_into_cache`, for the same reason that one does: a
capability every surface reaches should have exactly one implementation, or the
surfaces drift apart. That is not hypothetical for reports. Plotting was
implemented twice, once deterministically and once as five agent tools, and the
copies diverged on the legend table, on batching, on when a series is refreshed
and on what an ambiguous title returns, until a one-line fix had to be applied by
hand to both.

Nothing here raises on an unknown owner or invents one: `created_by` comes from
the caller installed for the request, never from an argument.
"""
from __future__ import annotations

import uuid as _uuid
from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence, TypedDict

from apps.agentic.core.agents.series_metadata import report_metadata_from_series
from apps.agentic.db.report_cache import ReportCache
from apps.agentic.db.series_cache import SeriesCache
from apps.core.identity import current_user_id

from lib.logger import get_logger

logger = get_logger("YADA")


class TimeSeriesInfoEntry(TypedDict):
    cache_id: str
    title: str
    source: str
    native_id: str
    frequency: str
    observation_start: str
    observation_end: str
    metadata: dict[str, Any]


# ----------------------------------------------------------------- resolution

@dataclass(frozen=True)
class ReportResolution:
    """What a reference resolved to: one report, or the candidates it could mean.

    A reference is a UUID or a title SUBSTRING, and substrings are not unique --
    nothing enforces unique titles, so "GDP" legitimately means both "GDP Overview"
    and "GDP Deflator" for one user. Returning the candidates rather than guessing
    is what lets every door answer the same question its own way: the browser draws
    them as a picker, MCP and chat list them as text.
    """
    record: dict | None = None
    candidates: list[dict] = field(default_factory=list)

    @property
    def resolved(self) -> bool:
        return self.record is not None

    @property
    def ambiguous(self) -> bool:
        return self.record is None and len(self.candidates) > 1


def resolve_report(reference: str, owner: str | None = None) -> ReportResolution:
    """Resolve a report id or title fragment, scoped to one owner.

    Tried as a UUID first, then as a title substring. A single title match resolves;
    several do not, and are returned as candidates for the caller to present.
    """
    try:
        _uuid.UUID(reference)
    except ValueError:
        pass
    else:
        record = ReportCache._get_by_report_id_sync(reference, owner=owner)
        if record is not None:
            return ReportResolution(record=record)

    matches = ReportCache._search_by_title_sync(reference, owner=owner)
    if len(matches) == 1:
        return ReportResolution(
            record=ReportCache._get_by_report_id_sync(matches[0]["report_id"],
                                                      owner=owner))
    return ReportResolution(candidates=list(matches))


def resolve_report_or_raise(reference: str, owner: str | None = None,
                            action: str = "plot") -> dict:
    """`resolve_report`, raising the message a caller would otherwise write itself.

    `action` only names the verb in the ambiguity message, so each door can say what
    the caller was trying to do with the report it could not pick.
    """
    resolution = resolve_report(reference, owner=owner)
    if resolution.resolved:
        assert resolution.record is not None
        return resolution.record
    if resolution.ambiguous:
        listed = "; ".join(f"{m['report_title']} ({m['report_id']})"
                           for m in resolution.candidates)
        raise ValueError(
            f"{len(resolution.candidates)} reports match '{reference}' — {action} "
            f"one by its id: {listed}")
    raise ValueError(f"No report found matching '{reference}'.")


# ------------------------------------------------------------------- creation

def resolve_series_entries(cache_ids: Sequence[str]) -> list[TimeSeriesInfoEntry]:
    """Project cache rows into the snapshot a report stores.

    Every id is resolved before anything is written, and a single miss aborts naming
    the ids that failed. A report that references a series it cannot load is worse
    than no report: it saves cleanly and fails later, at plot time, for a reason that
    no longer points at the request that caused it.

    `include_expired=True` deliberately: an expired entry is still the right series,
    and the render path refreshes it. Rejecting it here would make report creation
    fail for data that plots perfectly well.
    """
    entries: list[TimeSeriesInfoEntry] = []
    missing: list[str] = []
    for cache_id in cache_ids:
        try:
            entry = SeriesCache._get_by_cache_id_sync(cache_id, include_expired=True)
        except ValueError:
            # Not a UUID at all. A malformed id matches no row, so it is a miss --
            # the same answer this gives for an id that simply is not there, and the
            # same rule `ReportCache._as_report_id` already applies to report ids.
            # Letting uuid's "badly formed hexadecimal UUID string" out instead says
            # nothing about which id was wrong, and reaches a model as a crash.
            entry = None
        if not entry:
            missing.append(cache_id)
            continue
        raw_metadata = entry.get("metadata")
        entries.append({
            "cache_id": str(entry["cache_id"]),
            "title": str(entry.get("title") or ""),
            "source": str(entry.get("source") or ""),
            "native_id": str(entry.get("native_id") or ""),
            "frequency": str(entry.get("frequency") or ""),
            "observation_start": str(entry.get("observation_start") or ""),
            "observation_end": str(entry.get("observation_end") or ""),
            "metadata": raw_metadata if isinstance(raw_metadata, dict) else {},
        })

    if missing:
        raise ValueError("Report creation aborted. Missing cache IDs: "
                         + ", ".join(missing))
    return entries


def create_report(
    report_title: str,
    report_description: str,
    cache_ids: Sequence[str],
    time_range_from: str = "",
    time_range_to: str | None = None,
) -> dict:
    """Write a report and return {report_id, report_title, time_series_info}.

    The owner is `current_user_id()` — the caller installed for this request, which
    is None only when no users are configured. Never an argument: a report is
    readable only by its owner, so letting a caller name one would be a way to write
    a report into somebody else's account, or out of reach of every account.
    """
    ids = [str(c).strip() for c in cache_ids if str(c).strip()]
    if not ids:
        raise ValueError("No time series cache IDs were provided.")

    time_series_info = resolve_series_entries(ids)

    # `time_range_from` is NOT NULL in the table, and a blank reaches the insert as
    # NULL, so an omitted start date used to fail as an IntegrityError -- a 500 for
    # what is really a missing default. Derive it the way the browser's series picker
    # already does: the earliest observation among the chosen series, which is the
    # widest range the report can actually show.
    if not str(time_range_from).strip():
        starts = [e["observation_start"] for e in time_series_info
                  if e.get("observation_start")]
        if not starts:
            raise ValueError(
                "No start date given and none of the series records one, so the "
                "report has no time range. Pass time_range_from as YYYY-MM-DD.")
        time_range_from = min(starts)

    report_id = ReportCache._put_sync(
        report_title=report_title,
        report_description=report_description,
        time_series_info=time_series_info,
        time_range_from=time_range_from,
        time_range_to=time_range_to,
        metadata=report_metadata_from_series(time_series_info),
        created_by=current_user_id(),
    )
    logger.debug(f"create_report: '{report_title}' → {report_id}")
    # The EFFECTIVE range, not what was passed: a derived start date is the report's
    # real one, and a caller that echoes the argument would report a blank range for
    # a report that has a range.
    return {"report_id": str(report_id),
            "report_title": report_title,
            "report_description": report_description,
            "time_range_from": str(time_range_from),
            "time_range_to": time_range_to,
            "time_series_info": time_series_info}


# -------------------------------------------------------------- membership

@dataclass(frozen=True)
class ReportSeriesChange:
    """The outcome of adding to or removing from a report's series.

    `record` is the report as it now stands. `skipped` names references the change did
    not act on -- series already present on an add, or not present on a remove -- which
    is reported rather than raised: asking to add a series twice is not an error, and a
    caller that got a partial result has to be told which part.
    """
    record: dict
    changed: list[str] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)
    previous_range: tuple[str, str | None] = ("", None)

    @property
    def range_extended(self) -> bool:
        current = (str(self.record.get("time_range_from") or ""),
                   str(self.record["time_range_to"]) if self.record.get("time_range_to")
                   else None)
        return current != self.previous_range


def series_label(entry: Mapping[str, Any]) -> str:
    """How a stored series is named back to a caller: its source id, else its cache id."""
    return str(entry.get("native_id") or entry.get("cache_id") or "")


def _matches(entry: Mapping[str, Any], reference: str) -> bool:
    """Whether `reference` names this stored series, by cache id or by source id.

    Both, because the two doors hold different ids. The browser has cache ids from the
    series table; a model reading a report back has seen `native_id` ('UNRATE') and that
    is what a person says. Requiring the cache id would make every removal a two-call
    dance through list_reports.
    """
    needle = reference.strip().casefold()
    return needle in {str(entry.get("cache_id") or "").casefold(),
                      str(entry.get("native_id") or "").casefold()}


def _write_membership(record: dict, time_series_info: list[TimeSeriesInfoEntry],
                      time_range_from: str, time_range_to: str | None,
                      owner: str | None) -> dict:
    """Persist a new series list on an existing report, leaving its text alone.

    `_update_report_sync` is a whole-row replace -- it has no concept of a partial
    update -- so title, description and the dates have to be handed back to it. Reading
    them off `record` is what keeps "add a series" from quietly also resetting the title.
    """
    updated = ReportCache._update_report_sync(
        report_id=str(record["report_id"]),
        report_title=record.get("report_title") or "",
        report_description=record.get("report_description") or "",
        time_series_info=time_series_info,
        time_range_from=time_range_from,
        time_range_to=time_range_to,
        metadata=report_metadata_from_series(time_series_info),
        owner=owner,
    )
    if updated is None:
        # The resolve above found it under this owner, so losing it here means it was
        # deleted in between. Say that rather than returning a success with no row.
        raise ValueError(f"Report {record['report_id']} could not be updated; it may "
                         f"have just been deleted.")
    return updated


def add_report_series(reference: str, cache_ids: Sequence[str],
                      extend_range: bool = True) -> ReportSeriesChange:
    """Add cached series to an existing report.

    Every id is resolved before anything is written, by the same projection a create
    uses, so a bad id leaves the report untouched instead of half-updated.

    `extend_range` exists because the report's `time_range_from`/`time_range_to` are hard
    clipping bounds at plot time, not decoration: `render_report_plot` passes them to
    every series it loads. Adding a series that begins before the window and leaving the
    window alone would draw it with its early years missing, on a chart that looks
    entirely correct -- so by default the window widens to cover what was added, which is
    the same "widest range the report can show" rule `create_report` applies to a blank
    start date. It only ever widens. Narrowing could clip the series already there.

    `time_range_to` is left at None when it is None: that means "track the latest data",
    and pinning it to today's last observation would freeze the report.
    """
    owner = current_user_id()
    record = resolve_report_or_raise(reference, owner=owner, action="add series to")

    existing: list[TimeSeriesInfoEntry] = list(record.get("time_series_info") or [])
    wanted = [str(c).strip() for c in cache_ids if str(c).strip()]
    if not wanted:
        raise ValueError("No time series cache IDs were provided.")

    fresh, skipped = [], []
    for cache_id in wanted:
        if any(_matches(e, cache_id) for e in existing):
            skipped.append(cache_id)
        elif cache_id not in fresh:
            fresh.append(cache_id)

    previous = (str(record.get("time_range_from") or ""),
                str(record["time_range_to"]) if record.get("time_range_to") else None)
    if not fresh:
        # Nothing to do. Returning the report as it stands is the honest answer, and
        # writing an identical row would only touch updated_at.
        return ReportSeriesChange(record=record, changed=[], skipped=skipped,
                                  previous_range=previous)

    added = resolve_series_entries(fresh)
    merged = existing + added

    range_from, range_to = previous
    if extend_range:
        starts = [e["observation_start"] for e in added if e.get("observation_start")]
        if starts and (not range_from or min(starts) < range_from):
            range_from = min(starts)
        if range_to:
            ends = [e["observation_end"] for e in added if e.get("observation_end")]
            if ends and max(ends) > range_to:
                range_to = max(ends)

    updated = _write_membership(record, merged, range_from, range_to, owner)
    logger.debug(f"add_report_series: {record['report_id']} += "
                 f"{[series_label(e) for e in added]}")
    return ReportSeriesChange(record=updated,
                              changed=[series_label(e) for e in added],
                              skipped=skipped, previous_range=previous)


def remove_report_series(reference: str, series: Sequence[str]) -> ReportSeriesChange:
    """Remove series from an existing report, by cache id or by source id.

    Refuses to remove the last series. A report with none cannot be plotted -- it saves
    cleanly and then fails at render time -- so emptying one is almost certainly meant as
    deleting it, and that is a different verb with a different confirmation.

    The date range is left alone. Narrowing it to what remains would clip the surviving
    series, and widening makes no sense here.
    """
    owner = current_user_id()
    record = resolve_report_or_raise(reference, owner=owner,
                                     action="remove series from")

    existing: list[TimeSeriesInfoEntry] = list(record.get("time_series_info") or [])
    wanted = [str(s).strip() for s in series if str(s).strip()]
    if not wanted:
        raise ValueError("No series were named for removal.")

    doomed, skipped = [], []
    for reference_ in wanted:
        hit = next((e for e in existing if _matches(e, reference_)), None)
        if hit is None:
            skipped.append(reference_)
        elif hit not in doomed:
            doomed.append(hit)

    previous = (str(record.get("time_range_from") or ""),
                str(record["time_range_to"]) if record.get("time_range_to") else None)
    if not doomed:
        held = ", ".join(series_label(e) for e in existing) or "nothing"
        raise ValueError(
            f"None of {', '.join(wanted)} is in '{record.get('report_title')}'. "
            f"It holds: {held}.")

    remaining = [e for e in existing if e not in doomed]
    if not remaining:
        raise ValueError(
            f"That would remove every series from "
            f"'{record.get('report_title')}', leaving a report that cannot be "
            f"plotted. Delete the report instead, or keep at least one series.")

    updated = _write_membership(record, remaining, previous[0], previous[1], owner)
    logger.debug(f"remove_report_series: {record['report_id']} -= "
                 f"{[series_label(e) for e in doomed]}")
    return ReportSeriesChange(record=updated,
                              changed=[series_label(e) for e in doomed],
                              skipped=skipped, previous_range=previous)
