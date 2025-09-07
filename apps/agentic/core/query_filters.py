import re
from datetime import datetime, timezone

QUAL_ACCOUNT = re.compile(r'\b(?:account|owner|org|user):\s*([\w.-]+)\b', re.I)
QUAL_REPO    = re.compile(r'\brepo:\s*([\w.-]+(?:/[\w.-]+)?)\b', re.I)
QUAL_EXT     = re.compile(r'\bext:\s*(\w+)\b', re.I)
QUAL_AFTER   = re.compile(r'\bafter:\s*(\d{4}-\d{2}-\d{2})\b', re.I)
QUAL_BEFORE  = re.compile(r'\bbefore:\s*(\d{4}-\d{2}-\d{2})\b', re.I)

def _to_epoch(datestr: str) -> int:
    return int(datetime.fromisoformat(datestr).replace(tzinfo=timezone.utc).timestamp())

def build_filter_and_query(q: str):
    conditions = []
    # account / owner
    m = QUAL_ACCOUNT.search(q)
    if m:
        conditions.append({"account": m.group(1)})
        q = QUAL_ACCOUNT.sub("", q).strip()

    # repo (name or owner/name)
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

    # extension (normalize to ".rb" shape your metadata uses)
    m = QUAL_EXT.search(q)
    if m:
        conditions.append({"ext": f".{m.group(1).lower()}"})
        q = QUAL_EXT.sub("", q).strip()

    # time bounds (use numeric)
    m = QUAL_AFTER.search(q)
    if m:
        conditions.append({"commit_ts_unix": {"$gte": _to_epoch(m.group(1))}})
        q = QUAL_AFTER.sub("", q).strip()

    m = QUAL_BEFORE.search(q)
    if m:
        conditions.append({"commit_ts_unix": {"$lte": _to_epoch(m.group(1))}})
        q = QUAL_BEFORE.sub("", q).strip()

    where = {"$and": conditions} if conditions else None
    clean_q = q or "*"
    return clean_q, where