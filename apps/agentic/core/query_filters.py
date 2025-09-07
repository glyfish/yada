import re
from datetime import datetime, timezone

QUAL_REPO  = re.compile(r'\brepo:([\w.-]+(?:/[\w.-]+)?)\b', re.I)
QUAL_EXT   = re.compile(r'\bext:(\w+)\b', re.I)
QUAL_AFTER = re.compile(r'\bafter:(\d{4}-\d{2}-\d{2})\b', re.I)

def build_filter_and_query(q: str):
    where = {}

    m = QUAL_REPO.search(q)
    if m:
        repo_qual = m.group(1)
        if "/" in repo_qual:
            acct, repo = repo_qual.split("/", 1)
            where["account"] = acct
            where["repo"] = repo
        else:
            where["repo"] = repo_qual
        q = QUAL_REPO.sub("", q).strip()

    m = QUAL_EXT.search(q)
    if m:
        where["ext"] = f".{m.group(1).lower()}"
        q = QUAL_EXT.sub("", q).strip()

    m = QUAL_AFTER.search(q)
    if m:
        dt = datetime.fromisoformat(m.group(1)).replace(tzinfo=timezone.utc)
        where["commit_ts"] = {"$gte": dt.isoformat()}
        q = QUAL_AFTER.sub("", q).strip()

    return (q or "*"), (where or None)