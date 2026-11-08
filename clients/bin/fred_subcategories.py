#!/usr/bin/env python
"""
Derive, name and reconcile the browsable subcategory tree under each FRED category.

The entry point for `apps/agentic/db/fred_subcategory.py`, and the companion to
`clients/bin/fred_metadata.py`: that one collects FRED's catalogue, this one builds the
levels FRED does not have. Until now `build()` was a library function with no caller,
which is the same defect the discovery procedure was written to fix — a documented step
nobody can invoke is not reproducible.

**Scope is explicit, and `non-regional` is the default.** Regional data is 4,173 of 5,201
categories, and the semantic scheme does not fit it: county titles are one measure with a
place name substituted, so clustering groups Alabama's counties together instead of
grouping unemployment measures. See `SCOPES` in the module, and section 4.4 of
`sefer/planning/yada-fred-subcategory-procedure.md`. Passing `--scope regional` is
possible and costs real money; it is not recommended until that is settled.

**Every subcommand is idempotent.** `pending_builds` skips what is already `ok` or
`skipped`, so a second run makes no model calls and spends nothing, and an interrupted
run is continued by invoking the same command again. A category that died mid-write is
cleared by `clear_category` before it is rebuilt, never appended to.

Examples
--------
    # what the derived tree holds, and whether it still satisfies its invariants
    python clients/bin/fred_subcategories.py status

    # what a run would cost and how long it would take, without spending anything
    python clients/bin/fred_subcategories.py build --dry-run

    # prove the mechanism on the cheap categories first
    python clients/bin/fred_subcategories.py build --max-series 500 --limit 5

    # the committed run: the non-regional half
    python clients/bin/fred_subcategories.py build

    # after a FRED discovery run: assign new series to existing leaves, no model calls
    python clients/bin/fred_subcategories.py resync
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from dotenv import load_dotenv

load_dotenv()

from sqlalchemy import text  # noqa: E402

from apps.agentic.db.fred_catalogue import _engine  # noqa: E402
from apps.agentic.db.fred_subcategory import (  # noqa: E402
    BRANCH_CAP,
    LEAF_CAP,
    NAMING_CONCURRENCY,
    PROMPT_VERSION,
    SCOPES,
    SPLIT_VERSION,
    branch_cap_violations,
    build,
    leaf_cap_violations,
    modelled_nodes,
    pending_builds,
    resync,
    unnamed_nodes,
)
from lib.logger import get_logger  # noqa: E402

logger = get_logger("YADA")

#: Measured 2026-11-08 on a 463-name run under the balanced splitter.
#:
#: $0.000197, up from the $0.000136 measured under plain k-means -- and the rise is a
#: consequence of the fix, not a regression. Balanced leaves are full (22-25 series
#: against a mean of 14.6), so more of the 18-title sample is actually sent and the model
#: spends more output tokens reasoning about it. Fewer, fuller, costlier names: the two
#: probe categories still came out cheaper in total ($0.00586 -> $0.00494).
COST_PER_NAME = 0.000197
#: Wall-clock per name at `NAMING_CONCURRENCY`, from the same run: 426 names in 97 s on
#: the largest category, 4.38/s. The sequential figure was 1.37 s a name.
SECONDS_PER_NAME = 1.37
SECONDS_PER_NAME_CONCURRENT = 0.228
#: Nodes the real splitter produces against `modelled_nodes`. 1.00 because
#: `balanced_clusters` divides each node evenly, so the model is exact rather than an
#: estimate -- see its docstring for the three categories it was checked against. It was
#: 1.58 under plain k-means, where an uneven split recursed further.
LEAF_OVERHEAD = 1.0


def _sizes_for(engine, category_ids: list[int]) -> list[int]:
    if not category_ids:
        return []
    with engine.connect() as connection:
        return [
            row[0]
            for row in connection.execute(
                text(
                    """
                    SELECT count(DISTINCT series_id) FROM fred_series_category
                     WHERE category_id = ANY(:ids) GROUP BY category_id
                    """
                ),
                {"ids": category_ids},
            )
        ]


def cmd_status(args: argparse.Namespace) -> dict:
    """Read-only. What the derived tree holds, and whether it still holds its invariants."""
    engine = _engine(args.url)
    with engine.connect() as c:
        counts = {
            "nodes": c.execute(
                text("SELECT count(*) FROM fred_subcategory")
            ).scalar_one(),
            "leaves": c.execute(
                text("SELECT count(*) FROM fred_subcategory WHERE is_leaf")
            ).scalar_one(),
            "emptied_leaves": c.execute(
                text(
                    "SELECT count(*) FROM fred_subcategory "
                    "WHERE is_leaf AND emptied_at IS NOT NULL"
                )
            ).scalar_one(),
            "memberships": c.execute(
                text("SELECT count(*) FROM fred_series_subcategory")
            ).scalar_one(),
            "max_depth": c.execute(
                text("SELECT COALESCE(max(depth), 0) FROM fred_subcategory")
            ).scalar_one(),
            "spent_usd": float(
                c.execute(
                    text(
                        "SELECT COALESCE(sum(cost_usd), 0) FROM fred_subcategory_build"
                    )
                ).scalar_one()
            ),
            "llm_calls": c.execute(
                text("SELECT COALESCE(sum(llm_calls), 0) FROM fred_subcategory_build")
            ).scalar_one(),
        }
        counts["builds_by_status"] = {
            row[0]: row[1]
            for row in c.execute(
                text(
                    "SELECT status, count(*) FROM fred_subcategory_build "
                    "GROUP BY status ORDER BY 2 DESC"
                )
            )
        }
        counts["recorded_naming_failures"] = c.execute(
            text(
                "SELECT COALESCE(sum(naming_failures), 0) FROM fred_subcategory_build"
            )
        ).scalar_one()

    # Both halves of the invariant, read back from the database. A tree can satisfy the
    # leaf cap completely and still be unbrowsable at the top, which is how `BRANCH_CAP`
    # went unenforced: nothing asserted the upward direction.
    leaves_over = leaf_cap_violations(engine, args.cap)
    branches_over = branch_cap_violations(engine)
    unnamed = unnamed_nodes(engine)
    counts["leaf_cap"] = {
        "cap": args.cap, "violations": len(leaves_over),
        "largest": max((v[2] for v in leaves_over), default=0),
    }
    counts["branch_cap"] = {
        "cap": BRANCH_CAP, "violations": len(branches_over),
        "widest": max((v[2] for v in branches_over), default=0),
    }
    counts["unnamed_nodes"] = len(unnamed)
    if unnamed:
        counts["unnamed_detail"] = [
            {"subcategory_id": sid, "category_id": cid, "name": name}
            for sid, cid, name in unnamed[:10]
        ]

    counts["prompt_version"] = PROMPT_VERSION
    counts["split_version"] = SPLIT_VERSION
    with engine.connect() as c:
        # Rows built under a superseded prompt or splitter. They are not wrong, they are
        # not comparable -- which is why `pending_builds` counts them as work to redo.
        counts["nodes_by_version"] = {
            f"{row[0]} / {row[1]}": row[2]
            for row in c.execute(
                text(
                    "SELECT prompt_version, split_version, count(*) "
                    "  FROM fred_subcategory GROUP BY 1, 2 ORDER BY 3 DESC"
                )
            )
        }
    counts["pending_by_scope"] = {
        scope: len(pending_builds(engine, scope=scope)) for scope in sorted(SCOPES)
    }
    return counts


def cmd_build(args: argparse.Namespace) -> dict:
    """Derive and name subcategories for every pending category in scope."""
    engine = _engine(args.url)
    if args.category:
        return _build_named(engine, args)
    if args.dry_run:
        pending = pending_builds(engine, scope=args.scope)
        if args.limit is not None:
            pending = pending[: args.limit]
        sizes = _sizes_for(engine, pending)
        if args.max_series is not None:
            sizes = [n for n in sizes if n <= args.max_series]
        floor = sum(modelled_nodes(n, args.cap) for n in sizes)
        names = int(floor * LEAF_OVERHEAD)
        return {
            "dry_run": True,
            "scope": args.scope,
            "categories_pending": len(pending),
            "categories_over_cap": sum(1 for n in sizes if n > LEAF_CAP),
            "memberships": sum(n for n in sizes if n > LEAF_CAP),
            "largest_category": max(sizes, default=0),
            "nodes_modelled": floor,
            "names_modelled": names,
            "cost_usd_modelled": round(names * COST_PER_NAME, 2),
            "hours_sequential": round(names * SECONDS_PER_NAME / 3600, 1),
            "hours_at_workers": round(
                names * SECONDS_PER_NAME_CONCURRENT / 3600, 1
            ),
            "note": (
                "node count is exact (it reproduced three real categories); "
                "$0.000197 a name and 4.38 names/s are measured over 463 names at "
                f"{args.workers} workers, so the total is a projection, not a guess -- "
                "it assumes the same leaf fullness and no sustained rate limiting"
            ),
        }
    return build(
        url=args.url, scope=args.scope, limit=args.limit, cap=args.cap,
        max_series=args.max_series, workers=args.workers,
    )


def _build_named(engine, args: argparse.Namespace) -> dict:
    """
    Rebuild exactly the categories asked for, pending or not.

    The repair path. `verify` names the categories holding `UNNAMED` nodes and this is
    how they get fixed, without re-running a scope to reach them -- and `clear_category`
    means a rebuild replaces a category's tree rather than appending a second one.
    """
    from apps.agentic.db.fred_subcategory import (
        Namer, TitleEmbedder, build_category, modelled_nodes,
    )

    sizes = dict(zip(args.category, _sizes_for(engine, args.category)))
    if args.dry_run:
        names = sum(modelled_nodes(n, args.cap) for n in sizes.values())
        return {
            "dry_run": True, "categories": sizes,
            "names_modelled": names,
            "cost_usd_modelled": round(names * COST_PER_NAME, 4),
        }

    embedder, namer = TitleEmbedder(), Namer()
    results = []
    for category_id in args.category:
        results.append(
            build_category(engine, category_id, embedder, namer, args.cap, args.workers)
        )
    return {
        "built": results, "llm_calls": namer.calls,
        "naming_failures": namer.failures, "truncated_replies": namer.truncated,
        "cost_usd": round(namer.cost_usd, 5),
        "leaf_cap_violations": len(leaf_cap_violations(engine, args.cap)),
        "branch_cap_violations": len(branch_cap_violations(engine)),
        "unnamed_nodes": len(unnamed_nodes(engine)),
    }


def cmd_resync(args: argparse.Namespace) -> dict:
    """Place new series on existing leaves; optionally rebuild what that pushed over."""
    engine = _engine(args.url)
    if args.dry_run:
        from apps.agentic.db.fred_subcategory import unassigned_series

        return {
            "dry_run": True,
            "unassigned_series": len(unassigned_series(engine)),
            "over_cap_leaves": len(leaf_cap_violations(engine, args.cap)),
            "would_rebuild": args.split_over_cap,
        }
    return resync(
        url=args.url, split_over_cap=args.split_over_cap, scope=args.scope,
        workers=args.workers,
    )


def cmd_verify(args: argparse.Namespace) -> dict:
    """Read-only. The invariants alone, with a non-zero exit if any is broken."""
    engine = _engine(args.url)
    leaves_over = leaf_cap_violations(engine, args.cap)
    branches_over = branch_cap_violations(engine)
    unnamed = unnamed_nodes(engine)
    return {
        "leaf_cap_violations": [
            {"subcategory_id": s, "category_id": c, "series": n}
            for s, c, n in leaves_over[:20]
        ],
        "branch_cap_violations": [
            {"subcategory_id": s, "category_id": c, "children": n}
            for s, c, n in branches_over[:20]
        ],
        "unnamed_nodes": [
            {"subcategory_id": s, "category_id": c, "name": name}
            for s, c, name in unnamed[:20]
        ],
        "ok": not (leaves_over or branches_over or unnamed),
    }


COMMANDS = {
    "status": cmd_status,
    "build": cmd_build,
    "resync": cmd_resync,
    "verify": cmd_verify,
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
        "--scope", default="non-regional", choices=sorted(SCOPES),
        help="Which half of the catalogue to build. Defaults to the half the cost and "
             "quality were measured on; 'regional' spends real money on a scheme that "
             "does not fit it (see section 4.4 of the procedure).",
    )
    parser.add_argument(
        "--limit", type=int, default=None,
        help="Build at most this many categories, cheapest first.",
    )
    parser.add_argument(
        "--category", type=int, action="append", default=[],
        help="build only: rebuild exactly these category ids, pending or not. Repeatable."
             " This is the repair path for the categories `verify` reports.",
    )
    parser.add_argument(
        "--max-series", type=int, default=None,
        help="Skip categories larger than this, for proving a run before committing to "
             "the whole scope.",
    )
    parser.add_argument(
        "--cap", type=int, default=LEAF_CAP,
        help=f"Maximum series per leaf. Default {LEAF_CAP}.",
    )
    parser.add_argument(
        "--workers", type=int, default=NAMING_CONCURRENCY,
        help=f"Naming calls in flight within one level of one tree. Default "
             f"{NAMING_CONCURRENCY}; 1 is the sequential behaviour.",
    )
    parser.add_argument(
        "--split-over-cap", action="store_true",
        help="resync only: rebuild categories whose leaves the assignment pushed past "
             "the cap. Costs model calls, so it is off by default and the debt is "
             "reported instead.",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Report what would be done, and what it would cost, without a model call "
             "or a write.",
    )
    args = parser.parse_args()

    result = COMMANDS[args.command](args)
    print(json.dumps(result, indent=2, default=str))
    # `verify` is meant to be usable from a scheduler, so a broken invariant has to be
    # detectable without parsing the output.
    if args.command == "verify" and not result["ok"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
