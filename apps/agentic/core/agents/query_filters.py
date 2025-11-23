"""
query_filters.py

Parse inline qualifiers from a user query into a Chroma 'where' filter and a cleaned query string.

Supported qualifiers (case-insensitive):

  # GitHub-style
  account:<name>    | owner:<name> | org:<name> | user:<name>
  repo:<name>       | repo:<owner/name>
  ext:<ext>         # normalized to leading dot (e.g., '.rb', '.md')

  # Time (applies to ALL sources via unified metadata 'ts_unix')
  after:YYYY-MM-DD
  before:YYYY-MM-DD

  # Research Notes
  notes:            # optional switch; also adds {"source":"research_notes"}
  title:"..."       | title:<word>
  authors:"..."     | authors:<word>, csv list of authors, matches substring
  topic:"..."       | topic:<word>
  tags:<word>       # matches substring in CSV 'tags' field you store
  section:<n>
  section:<lo>-<hi>

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
QUAL_TAGS    = re.compile(r"\btags:\s*([^\s,]+)\b", re.I)

QUAL_PAGE    = re.compile(r"\bpage:\s*(\d+)\b", re.I)
QUAL_PAGES   = re.compile(r"\bpages?:\s*(\d+)\s*-\s*(\d+)\b", re.I)


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

    m = QUAL_TOPIC.search(q)
    if m:
        conditions.append({"topic": _pick(m)})
        q = QUAL_TOPIC.sub("", q).strip()

    m = QUAL_TAGS.search(q)
    if m:
        # 'tags' is expected to be a CSV string (scalar) in metadata
        conditions.append({"tags": m.group(1)})
        q = QUAL_TAGS.sub("", q).strip()

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

    if not conditions:
        where = None
    elif len(conditions) == 1:
        where = conditions[0]           # <-- no $and wrapper
    else:
        where = {"$and": conditions} 

    clean_q = q.strip() or "*"
    
    return clean_q, where