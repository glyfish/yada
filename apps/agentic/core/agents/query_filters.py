"""
query_filters.py

Parse inline qualifiers from a user query into a Chroma 'where' filter and a cleaned query string.

Supported qualifiers (case-insensitive):

  # GitHub-style
  account:<name>    | owner:<name> | org:<name> | user:<name>
  repo:<name>       | repo:<owner/name>
  ext:<ext>         # normalized to leading dot (e.g., '.rb', '.md')

  # Time -- GITHUB ONLY. These filter on metadata 'ts_unix', which is present on
  # 100% of github chunks and on 0% of research_library, fred and etf (verified
  # 2026-10-17). Used against those three they match nothing and silently zero
  # the result set.
  after:YYYY-MM-DD
  before:YYYY-MM-DD

  # Research Notes
  # NOTE: every qualifier below builds an EXACT equality condition. Nothing here
  # matches substrings, and matching is case-sensitive.
  notes:            # BROKEN -- adds {"source":"research_notes"}, but the research
                    # library store has no 'source' key at all, so this forces any
                    # query using it to zero results.
  title:"..."       | title:<word>   # one of 64 titles, matched in full
  authors:"..."     | authors:<word>
                    # EXACT match on the whole stored string. Multi-author documents
                    # store one comma-joined value ("Troy Stribling, W. H. Matthaeus"),
                    # so a single contributor's name matches none of them.
  topic:<word>      # ACCEPTED AND IGNORED. `topic` is an info field, not a search
                    # filter: present on 99% of chunks, but its values are whole
                    # prose sentences, so equality never matches. It is stripped
                    # from the query so it cannot pollute the embedding, and no
                    # condition is built. Topic is surfaced by the info agents,
                    # which project metadata rows and show no content.
  shelf:<word>      # exactly one of: notes, posts, publications, jaynes, reading_list
  section:<n>
  section:<lo>-<hi>

  # FRED (Federal Reserve Economic Data)
  category_id:<n>                   # exact category ID match
  category_name:"..."               | category_name:<word>
  series_id:"..."                   | series_id:<word>
  popularity:<n>                    # exact match
  popularity:>n | >=n | <n | <=n    # comparison operators
  last_updated:YYYY-MM-DD           # exact date
  last_updated:after YYYY-MM-DD     | last_updated:before YYYY-MM-DD

Returns:
    clean_q: str              # the natural-language remainder to search with
    where: dict | None        # a Chroma filter object, or None if no qualifiers
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Tuple, Dict, Any, Optional

# ---------- Qualifier regexes ----------

QUAL_ACCOUNT = re.compile(r"\b(?:account|owner|org|user):\s*([\w.-]+)\b", re.I)
QUAL_REPO    = re.compile(r"\brepo:\s*([\w.-]+(?:/[\w.-]+)?)\b", re.I)
# Accept ext with or without leading dot
QUAL_EXT     = re.compile(r"\bext:\s*\.?([A-Za-z0-9_+-]+)\b", re.I)

QUAL_AFTER   = re.compile(r"\bafter:\s*(\d{4}-\d{2}-\d{2})\b", re.I)
QUAL_BEFORE  = re.compile(r"\bbefore:\s*(\d{4}-\d{2}-\d{2})\b", re.I)

# Research notes
QUAL_NOTES   = re.compile(r"\bnotes:\s*(?:true|yes|1)?\b", re.I)

# Quoted or single-token capture for multiword fields
QUAL_TITLE   = re.compile(r'\btitle:\s*(?:"([^"]+)"|([^\s]+))', re.I)
QUAL_AUTHORS = re.compile(r'\bauthors:\s*(?:"([^"]+)"|([^\s]+))', re.I)
QUAL_TOPIC   = re.compile(r'\btopic:\s*(?:"([^"]+)"|([^\s]+))', re.I)
QUAL_SHELF   = re.compile(r'\bshelf:\s*(?:"([^"]+)"|([^\s]+))', re.I)

QUAL_PAGE    = re.compile(r"\bpage:\s*(\d+)\b", re.I)
QUAL_PAGES   = re.compile(r"\bpages?:\s*(\d+)\s*-\s*(\d+)\b", re.I)

# FRED qualifiers
QUAL_CATEGORY_ID   = re.compile(r"\bcategory_id:\s*(\d+)\b", re.I)
QUAL_CATEGORY_NAME = re.compile(r'\bcategory_name:\s*(?:"([^"]+)"|([^\s]+))', re.I)
QUAL_SERIES_ID     = re.compile(r'\bseries_id:\s*(?:"([^"]+)"|([^\s]+))', re.I)
QUAL_POPULARITY    = re.compile(r"\bpopularity:\s*([<>]=?)?\s*(\d+)\b", re.I)
QUAL_LAST_UPDATED  = re.compile(r"\blast_updated:\s*(after|before)?\s*(\d{4}-\d{2}-\d{2})\b", re.I)

# ETF qualifiers
QUAL_FAMILY         = re.compile(r'\bfamily:\s*(?:"([^"]+)"|([^\s]+))', re.I)
QUAL_CATEGORY_GROUP = re.compile(r'\bcategory_group:\s*(?:"([^"]+)"|([^\s]+))', re.I)
QUAL_ETF_CATEGORY   = re.compile(r'\bcategory:\s*(?:"([^"]+)"|([^\s]+))', re.I)
QUAL_EXCHANGE       = re.compile(r'\bexchange:\s*(?:"([^"]+)"|([^\s]+))', re.I)


# ---------- Helpers ----------

def _to_epoch(datestr: str) -> int:
    """
    Convert 'YYYY-MM-DD' (or ISO8601 date/time) to seconds since epoch (UTC).
    """
    dt = datetime.fromisoformat(datestr)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    else:
        dt = dt.astimezone(timezone.utc)
    return int(dt.timestamp())


def _pick(m: re.Match) -> str:
    """
    Choose the quoted (group 1) or fallback single-token (group 2) capture.
    """
    return (m.group(1) or m.group(2)).strip()


# ---------- Main parser ----------

def build_filter_and_query(q: str) -> Tuple[str, Optional[Dict[str, Any]]]:
    """
    Parse qualifiers out of 'q', returning (clean_q, where_filter).

    - 'clean_q' is the residual NL prompt after removing qualifiers.
    - 'where_filter' is a Chroma 'where' dict, or None if no qualifiers were found.

    Time filters ALWAYS map to 'ts_unix' so they apply across both GitHub and Research Notes.
    """
    conditions: list[Dict[str, Any]] = []

    # --- GitHub-style qualifiers ---
    m = QUAL_ACCOUNT.search(q)
    if m:
        conditions.append({"account": m.group(1)})
        q = QUAL_ACCOUNT.sub("", q).strip()

    m = QUAL_REPO.search(q)
    if m:
        token = m.group(1)
        q = QUAL_REPO.sub("", q).strip()
        if "/" in token:
            acct, repo = token.split("/", 1)
            conditions.append({"account": acct})
            conditions.append({"repo": repo})
        else:
            conditions.append({"repo": token})

    m = QUAL_EXT.search(q)
    if m:
        ext = m.group(1).lower()
        if not ext.startswith("."):
            ext = f".{ext}"
        conditions.append({"ext": ext})
        q = QUAL_EXT.sub("", q).strip()

    # --- Unified time filters (across all sources) ---
    m = QUAL_AFTER.search(q)
    if m:
        conditions.append({"ts_unix": {"$gte": _to_epoch(m.group(1))}})
        q = QUAL_AFTER.sub("", q).strip()

    m = QUAL_BEFORE.search(q)
    if m:
        conditions.append({"ts_unix": {"$lte": _to_epoch(m.group(1))}})
        q = QUAL_BEFORE.sub("", q).strip()

    # --- Research Notes qualifiers ---
    if QUAL_NOTES.search(q):
        # If routing by collection, you can ignore this; keeping it helps when using a single collection.
        conditions.append({"source": "research_notes"})
        q = QUAL_NOTES.sub("", q).strip()

    m = QUAL_TITLE.search(q)
    if m:
        conditions.append({"title": _pick(m)})
        q = QUAL_TITLE.sub("", q).strip()

    m = QUAL_AUTHORS.search(q)
    if m:
        conditions.append({"authors": _pick(m)})
        q = QUAL_AUTHORS.sub("", q).strip()

    # `topic` is an INFO field, not a search filter. Its values are whole prose
    # sentences ("Fundamentals of fractional Brownian motion."), so the equality
    # match this used to build could never hit -- it only ever zeroed the result
    # set. Where topic belongs is the info agents, which project metadata rows and
    # show no content at all. The qualifier is still stripped here so a stray
    # "topic:..." does not end up embedded in the semantic query.
    m = QUAL_TOPIC.search(q)
    if m:
        q = QUAL_TOPIC.sub("", q).strip()

    m = QUAL_SHELF.search(q)
    if m:
        conditions.append({"shelf": _pick(m)})
        q = QUAL_SHELF.sub("", q).strip()

    m = QUAL_PAGE.search(q)
    if m:
        try:
            conditions.append({"section": int(m.group(1))})
        except Exception:
            pass
        q = QUAL_PAGE.sub("", q).strip()

    m = QUAL_PAGES.search(q)
    if m:
        try:
            lo, hi = int(m.group(1)), int(m.group(2))
            if lo > hi:
                lo, hi = hi, lo
            conditions.append({"section": {"$gte": lo}})
            conditions.append({"section": {"$lte": hi}})
        except Exception:
            pass
        q = QUAL_PAGES.sub("", q).strip()

    # --- FRED qualifiers ---
    m = QUAL_CATEGORY_ID.search(q)
    if m:
        conditions.append({"category_id": int(m.group(1))})
        q = QUAL_CATEGORY_ID.sub("", q).strip()

    m = QUAL_CATEGORY_NAME.search(q)
    if m:
        conditions.append({"category_name": _pick(m)})
        q = QUAL_CATEGORY_NAME.sub("", q).strip()

    m = QUAL_SERIES_ID.search(q)
    if m:
        conditions.append({"series_id": _pick(m)})
        q = QUAL_SERIES_ID.sub("", q).strip()

    m = QUAL_POPULARITY.search(q)
    if m:
        op = m.group(1) or ""
        val = int(m.group(2))
        if op == ">":
            conditions.append({"popularity": {"$gt": val}})
        elif op == ">=":
            conditions.append({"popularity": {"$gte": val}})
        elif op == "<":
            conditions.append({"popularity": {"$lt": val}})
        elif op == "<=":
            conditions.append({"popularity": {"$lte": val}})
        else:
            conditions.append({"popularity": val})
        q = QUAL_POPULARITY.sub("", q).strip()

    m = QUAL_LAST_UPDATED.search(q)
    if m:
        direction = (m.group(1) or "").lower()
        date_val = m.group(2)
        if direction == "after":
            conditions.append({"last_updated": {"$gte": date_val}})
        elif direction == "before":
            conditions.append({"last_updated": {"$lte": date_val}})
        else:
            conditions.append({"last_updated": date_val})
        q = QUAL_LAST_UPDATED.sub("", q).strip()

    # --- ETF qualifiers ---
    m = QUAL_FAMILY.search(q)
    if m:
        conditions.append({"family": _pick(m)})
        q = QUAL_FAMILY.sub("", q).strip()

    m = QUAL_CATEGORY_GROUP.search(q)
    if m:
        conditions.append({"category_group": _pick(m)})
        q = QUAL_CATEGORY_GROUP.sub("", q).strip()

    m = QUAL_ETF_CATEGORY.search(q)
    if m:
        conditions.append({"category": _pick(m)})
        q = QUAL_ETF_CATEGORY.sub("", q).strip()

    m = QUAL_EXCHANGE.search(q)
    if m:
        conditions.append({"exchange": _pick(m)})
        q = QUAL_EXCHANGE.sub("", q).strip()

    if not conditions:
        where = None
    elif len(conditions) == 1:
        where = conditions[0]           # <-- no $and wrapper
    else:
        where = {"$and": conditions} 

    clean_q = q.strip() or "*"
    
    return clean_q, where
