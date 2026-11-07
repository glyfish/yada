#!/usr/bin/env python
"""
Collect FRED's metadata catalogue into Postgres.

The entry point for `apps/agentic/db/fred_discovery.py`. It exists because the catalogue
had none: the 424,634 series now in `yada_dev` were fetched by a throwaway script that no
longer exists, so nothing in the repository recorded how the rows got there. A documented
procedure whose steps nobody can invoke is not reproducible.

This replaces `clients/bin/fred.py`, which loads the superseded YAML export into Chroma.
That one still runs and is still wired to three agents; see
`sefer/planning/yada-todo.md` section 5 for the cutover.

**Every subcommand is idempotent.** Run any of them twice and the second run makes no
requests and changes no rows:

- `walk` skips categories whose `walked_at` is set, queueing their children from the
  database so a resume continues past the previous frontier rather than stopping at it.
- `fetch` skips categories whose scan is already `ok`.
- series are upserted, memberships inserted on-conflict-do-nothing.
- `paths` and `exclusions` update only where the value actually differs.

That is what makes `notebooks/data/fred_meta_data.ipynb` safe to re-run, and it is
asserted by `tests/unit/test_fred_discovery.py`.

Examples
--------
    # what state is the catalogue in
    python clients/bin/fred_metadata.py status

    # walk the tree, resuming; then fetch every category not yet complete
    python clients/bin/fred_metadata.py walk
    python clients/bin/fred_metadata.py fetch

    # both, which is what a full collection run is
    python clients/bin/fred_metadata.py all

    # prove a second run is a no-op
    python clients/bin/fred_metadata.py all --dry-run

    # bound a run while testing
    python clients/bin/fred_metadata.py fetch --limit 5
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from dotenv import load_dotenv

load_dotenv()

from sqlalchemy import text  # noqa: E402

from apps.agentic.db.fred_catalogue import _engine  # noqa: E402
from apps.agentic.db.fred_discovery import (  # noqa: E402
    VOLUME_EXCLUDED,
    FredApi,
    FredApiError,
    fetch_category,
    mark_exclusions,
    pending_categories,
    rebuild_paths,
    refresh_derived,
    walk_categories,
)
from lib.logger import get_logger  # noqa: E402

logger = get_logger("YADA")


def cmd_status(args: argparse.Namespace) -> dict:
    """Read-only. What the catalogue holds and what is still outstanding."""
    engine = _engine(args.url)
    with engine.connect() as c:
        counts = {
            "series": c.execute(text("SELECT count(*) FROM fred_series")).scalar_one(),
            "memberships": c.execute(
                text("SELECT count(*) FROM fred_series_category")
            ).scalar_one(),
            "categories": c.execute(
                text("SELECT count(*) FROM fred_category")
            ).scalar_one(),
            "walked": c.execute(
                text("SELECT count(*) FROM fred_category WHERE walked_at IS NOT NULL")
            ).scalar_one(),
            "excluded": c.execute(
                text(
                    "SELECT count(*) FROM fred_category WHERE excluded_reason IS NOT NULL"
                )
            ).scalar_one(),
            "scans_ok": c.execute(
                text("SELECT count(*) FROM fred_category_scan WHERE status = 'ok'")
            ).scalar_one(),
            "scans_bad": c.execute(
                text("SELECT count(*) FROM fred_category_scan WHERE status <> 'ok'")
            ).scalar_one(),
            # The reconciliation: what FRED said, beside what we wrote.
            "api_reported": c.execute(
                text("SELECT COALESCE(sum(api_series_count), 0) FROM fred_category_scan")
            ).scalar_one(),
            "written": c.execute(
                text(
                    "SELECT COALESCE(sum(fetched_series_count), 0) FROM fred_category_scan"
                )
            ).scalar_one(),
            "deferred_by_cap": c.execute(
                text(
                    """
                    SELECT COALESCE(sum(api_series_count - fetched_series_count), 0)
                      FROM fred_category_scan WHERE page_limit IS NOT NULL
                    """
                )
            ).scalar_one(),
        }
    counts["unwalked"] = counts["categories"] - counts["walked"]
    counts["pending_fetch"] = len(pending_categories(engine))
    counts["volume_excluded_roots"] = sorted(VOLUME_EXCLUDED)
    return counts


def cmd_walk(args: argparse.Namespace) -> dict:
    """Walk the category tree, resuming by default."""
    engine = _engine(args.url)
    if args.dry_run:
        with engine.connect() as c:
            unwalked = c.execute(
                text("SELECT count(*) FROM fred_category WHERE walked_at IS NULL")
            ).scalar_one()
        return {"dry_run": True, "categories_to_visit": unwalked}
    api = FredApi()
    result = {"tree": walk_categories(engine, api, revisit=args.revisit)}
    result["paths"] = rebuild_paths(engine)
    result["exclusions"] = mark_exclusions(engine)
    result["requests"] = api.requests
    return result


def cmd_fetch(args: argparse.Namespace) -> dict:
    """Fetch series for every category whose scan is not already `ok`."""
    engine = _engine(args.url)
    pending = pending_categories(engine)
    if args.limit is not None:
        pending = pending[: args.limit]
    if args.dry_run:
        return {"dry_run": True, "categories_to_fetch": len(pending)}

    api = FredApi()
    started = time.monotonic()
    done = incomplete = failed = capped = 0
    for index, (category_id, page_limit) in enumerate(pending, 1):
        try:
            outcome = fetch_category(engine, api, category_id, page_limit)
        except FredApiError:
            raise  # key or protocol failure: stop rather than grind through it
        except Exception as error:  # noqa: BLE001
            failed += 1
            logger.warning(f"category {category_id} failed: {error}")
            continue
        done += 1
        incomplete += outcome["status"] == "incomplete"
        capped += bool(outcome["capped"])
        if index % 50 == 0:
            rate = api.requests / max(time.monotonic() - started, 1) * 60
            logger.info(
                f"fetch: {index}/{len(pending)} categories, {api.requests} requests, "
                f"{rate:.0f}/min"
            )

    result = {
        "attempted": len(pending), "completed": done, "incomplete": incomplete,
        "capped": capped, "failed": failed, "requests": api.requests,
        "elapsed_s": round(time.monotonic() - started, 1),
    }
    if done:
        # Once, at the end. The currency cutoffs are per-frequency p95s, so they are only
        # correct when every series in a class is present -- computing them mid-run gives
        # each category its own definition of "current".
        result["derived"] = refresh_derived(engine)
    return result


def cmd_resync(args: argparse.Namespace) -> dict:
    """Re-walk, re-fetch anything not `ok`, and reconcile the derived subcategory tree."""
    from apps.agentic.db.fred_subcategory import resync as subcategory_resync

    result = {"walk": cmd_walk(args), "fetch": cmd_fetch(args)}
    if not args.dry_run:
        result["subcategories"] = subcategory_resync(
            args.url, split_over_cap=args.split_over_cap
        )
    return result


def cmd_all(args: argparse.Namespace) -> dict:
    return {"walk": cmd_walk(args), "fetch": cmd_fetch(args)}


COMMANDS = {
    "status": cmd_status,
    "walk": cmd_walk,
    "fetch": cmd_fetch,
    "all": cmd_all,
    "resync": cmd_resync,
}


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("command", choices=sorted(COMMANDS))
    parser.add_argument(
        "--url", default=None,
        help="Database URL. Defaults to the one YADA_ENV selects.",
    )
    parser.add_argument(
        "--limit", type=int, default=None,
        help="Fetch at most this many categories, for proving a run before committing "
             "to ~10,400 requests.",
    )
    parser.add_argument(
        "--revisit", action="store_true",
        help="Re-ask every category for its children instead of resuming. Needed to "
             "notice categories FRED has ADDED; without it a walk skips what it has "
             "already visited.",
    )
    parser.add_argument(
        "--split-over-cap", action="store_true",
        help="resync only: rebuild categories whose leaves exceeded the size cap. Costs "
             "LLM calls, so it is off by default and the debt is reported instead.",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Report what would be done without making a request or a write.",
    )
    args = parser.parse_args()

    try:
        result = COMMANDS[args.command](args)
    except FredApiError as error:
        print(f"FRED API error: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
