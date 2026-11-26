"""
Report tools: create, list, search, delete, and add/remove series.

`plot_report` already existed and lives in server.py beside the other App-bound
tools. What was missing was everything that gets a report to exist in the first
place. Until now `plot_report` could only draw rows written by yada's own chat
app, because `create_time_series_report` lived inside `TimeSeriesReportAgent` and
nothing on this surface could reach it -- the plotting notebook had to call that
agent's function directly to have anything to plot at all.

Every tool here is deterministic. The writing and the id-resolution are the same
functions the REST routes and the chat agent call
(`apps.agentic.agents.data.reports`), so a report created through Goose and a
report created through the browser are the same row, resolved the same way.

Owner scoping follows `plot_report`: the caller comes from the bearer token on
this message, never from an argument. A model that could name an owner could
write into somebody else's account.
"""
from __future__ import annotations

from time import perf_counter
from typing import Any

from mcp.types import TextContent

from apps.agentic.agents.data.reports import (
    add_report_series, create_report, remove_report_series, resolve_report,
)
from apps.agentic.db.report_cache import ReportCache
from apps.core.identity import current_user_id

from lib.logger import get_logger

logger = get_logger("YADA")


def _log(tool: str, arguments: dict, started: float, outcome: str) -> None:
    shown = " ".join(f"{k}={v!r}" for k, v in arguments.items() if v is not None)
    logger.info(f"{tool} <- {shown} | {outcome} in {perf_counter() - started:.2f}s")


def _row(record: dict) -> dict[str, Any]:
    """The listing projection: enough to choose a report, never its observations."""
    series = record.get("time_series_info") or []
    return {
        "report_id": str(record["report_id"]),
        "report_title": record.get("report_title") or "",
        "report_description": record.get("report_description") or "",
        "series_count": len(series),
        "series": [s.get("native_id") or s.get("cache_id", "") for s in series],
        "time_range_from": str(record.get("time_range_from") or ""),
        "time_range_to": (str(record["time_range_to"])
                          if record.get("time_range_to") else None),
    }


def register(server) -> None:
    """Register the six report tools."""

    def create_report_tool(report_title: str, cache_ids: list[str],
                           report_description: str = "",
                           date_from: str = "", date_to: str | None = None) -> dict:
        started = perf_counter()
        args = {"report_title": report_title, "cache_ids": cache_ids}
        try:
            created = create_report(
                report_title=report_title,
                report_description=report_description,
                cache_ids=cache_ids,
                time_range_from=date_from,
                time_range_to=date_to,
            )
        except ValueError as exc:
            # A bad cache_id is the common case and the model can fix it, so say which
            # one failed rather than returning a protocol error it cannot read.
            _log("create_report", args, started, "refused")
            return {"status": "error", "detail": str(exc)}
        _log("create_report", args, started, created["report_id"])
        return {"status": "ok", **_row(created)}

    def list_reports() -> dict:
        started = perf_counter()
        records = ReportCache._list_reports_sync(owner=current_user_id())
        _log("list_reports", {}, started, f"{len(records)} reports")
        return {"status": "ok", "count": len(records),
                "reports": [_row(r) for r in records]}

    def search_reports(query: str) -> dict:
        started = perf_counter()
        owner = current_user_id()
        resolution = resolve_report(query, owner=owner)
        if resolution.resolved:
            assert resolution.record is not None
            _log("search_reports", {"query": query}, started, "1 report")
            return {"status": "ok", "count": 1,
                    "reports": [_row(resolution.record)]}
        # Zero and many are the same answer shape on purpose. A caller that got one
        # row back can act; a caller that got three has to choose, and a caller that
        # got none has to widen -- all three read the same field to find out which.
        rows = []
        for match in resolution.candidates:
            record = ReportCache._get_by_report_id_sync(match["report_id"], owner=owner)
            if record is not None:
                rows.append(_row(record))
        _log("search_reports", {"query": query}, started, f"{len(rows)} reports")
        return {"status": "ok", "count": len(rows), "reports": rows}

    def add_series_to_report(report_id_or_title: str, cache_ids: list[str],
                             extend_date_range: bool = True) -> dict:
        started = perf_counter()
        args = {"report": report_id_or_title, "cache_ids": cache_ids}
        try:
            change = add_report_series(report_id_or_title, cache_ids,
                                       extend_range=extend_date_range)
        except ValueError as exc:
            # Ambiguous title, unknown report, or a bad cache_id. All three are things
            # the model can act on, so they come back as text, not a protocol error.
            _log("add_series_to_report", args, started, "refused")
            return {"status": "error", "detail": str(exc)}
        _log("add_series_to_report", args, started,
             f"added {len(change.changed)}, already present {len(change.skipped)}")
        return {"status": "ok", "added": change.changed,
                "already_present": change.skipped,
                "date_range_extended": change.range_extended,
                **_row(change.record)}

    def remove_series_from_report(report_id_or_title: str,
                                  series: list[str]) -> dict:
        started = perf_counter()
        args = {"report": report_id_or_title, "series": series}
        try:
            change = remove_report_series(report_id_or_title, series)
        except ValueError as exc:
            _log("remove_series_from_report", args, started, "refused")
            return {"status": "error", "detail": str(exc)}
        _log("remove_series_from_report", args, started,
             f"removed {len(change.changed)}, not present {len(change.skipped)}")
        return {"status": "ok", "removed": change.changed,
                "not_in_report": change.skipped,
                **_row(change.record)}

    def delete_report(report_id: str) -> dict:
        started = perf_counter()
        # Owner-scoped, so this cannot reach another caller's report: an id that is
        # not theirs is simply not found, which is the same answer the store gives
        # for an id that does not exist. Takes an id and not a title on purpose --
        # a substring that matched two reports would make deletion a guess.
        gone = ReportCache._delete_report_sync(report_id, owner=current_user_id())
        _log("delete_report", {"report_id": report_id}, started,
             "deleted" if gone else "not found")
        if not gone:
            return {"status": "error",
                    "detail": f"No report {report_id} to delete. Find it with "
                              f"search_reports and pass its report_id."}
        return {"status": "ok", "report_id": report_id}

    server.add_tool(
        delete_report, name="delete_report",
        description=(
            "Delete one of the caller's saved reports, permanently.\n"
            "- report_id: the id, not a title — search_reports first if the user "
            "named it. A title can match several reports, and deleting the wrong "
            "one cannot be undone.\n"
            "The series themselves are untouched; only the report that grouped them "
            "is removed. Confirm with the user before calling this."),
    )

    server.add_tool(
        add_series_to_report, name="add_series_to_report",
        description=(
            "Add cached series to a report the caller already has, and return the "
            "report as it now stands.\n"
            "- report_id_or_title: the id, or a fragment of the title. A fragment "
            "matching several reports returns the candidates and changes nothing.\n"
            "- cache_ids: ids from fetch_fred_series. Every id is checked before "
            "anything is written, so a bad one leaves the report untouched rather than "
            "half-updated. A series already in the report is reported back under "
            "already_present and added once, never twice.\n"
            "- extend_date_range: default true. A report's date range CLIPS every "
            "series when it is plotted, so adding a series that starts earlier than "
            "the range would otherwise draw it with its early years missing, on a "
            "chart that looks correct. True widens the range to cover what was added; "
            "it never narrows it. Pass false only to keep a deliberately narrow "
            "window, and expect the new series to be clipped to it.\n"
            "Use this when the user wants another series on an existing report. To "
            "start a new one, use create_report."),
    )

    server.add_tool(
        remove_series_from_report, name="remove_series_from_report",
        description=(
            "Remove series from one of the caller's reports, and return the report as "
            "it now stands. The series themselves stay in the cache and on any other "
            "report holding them; only this report's membership changes.\n"
            "- report_id_or_title: the id, or a fragment of the title.\n"
            "- series: which series to drop, each named by its cache_id OR by its "
            "source id as list_reports shows it ('UNRATE'), case-insensitively. A name "
            "that is not on the report is reported under not_in_report rather than "
            "failing the call, unless none of them match, which changes nothing and "
            "says what the report does hold.\n"
            "Removing the last series is refused: a report with none cannot be "
            "plotted. Delete the whole report with delete_report instead.\n"
            "The date range is left as it is, so the remaining series keep the window "
            "they were plotted with."),
    )

    server.add_tool(
        create_report_tool, name="create_report",
        description=(
            "Create a saved time series report from series already in yada's cache, "
            "and return its report_id. A report is a named set of series plus a date "
            "range; plot_report draws it later without re-stating which series it "
            "holds.\n"
            "- report_title: what to call it.\n"
            "- cache_ids: ids from fetch_fred_series. Every id is checked before "
            "anything is written, and an unknown one refuses the whole call rather "
            "than saving a report that cannot be plotted.\n"
            "- report_description: optional note about what it is for.\n"
            "- date_from / date_to: optional ISO dates. Leave date_to empty to keep "
            "the report tracking the latest data.\n"
            "Use this when the user wants to keep a set of series together, or asks "
            "to make or save a report. For a one-off chart use plot_series instead — "
            "it needs no report."),
    )

    server.add_tool(
        list_reports, name="list_reports",
        description=(
            "List the caller's saved reports, with the series each one holds. Returns "
            "metadata only — titles, ids, series counts and date ranges — never "
            "observations. Call this when the user asks what reports they have, or "
            "before plot_report when no report has been named."),
    )

    server.add_tool(
        search_reports, name="search_reports",
        description=(
            "Find saved reports by id or by a fragment of their title, e.g. "
            "'unemployment'. Titles are not unique, so this can return several; when "
            "it does, ask which one rather than guessing, and pass the chosen "
            "report_id to plot_report.\n"
            "- query: a report_id or any part of a title.\n"
            "Returns the same fields as list_reports. An empty result is a normal "
            "answer, not an error."),
    )

    logger.info("Report tools registered: create_report, list_reports, search_reports, "
                "delete_report, add_series_to_report, remove_series_from_report")
