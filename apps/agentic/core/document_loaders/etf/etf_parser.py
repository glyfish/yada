from __future__ import annotations

import re
from typing import Protocol, runtime_checkable


@runtime_checkable
class ETFParser(Protocol):
    def parse(self, path: str, limit: int | None = None) -> list[dict]:
        ...


def normalize_aum(raw: str | None) -> float | None:
    """Convert strings like '$3.1B', '$108.5M', '$450K' to a float (USD)."""
    if not raw:
        return None
    raw = str(raw).strip().replace(",", "")
    match = re.match(r"^\$?([\d.]+)\s*([TtBbMmKk]?)$", raw)
    if not match:
        return None
    value = float(match.group(1))
    suffix = match.group(2).upper()
    multipliers = {"T": 1e12, "B": 1e9, "M": 1e6, "K": 1e3, "": 1.0}
    return value * multipliers.get(suffix, 1.0)


def normalize_date(raw: str | None) -> str | None:
    """Convert MM/DD/YYYY to ISO YYYY-MM-DD. Returns None if unparseable."""
    if not raw:
        return None
    raw = str(raw).strip()
    match = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{4})$", raw)
    if match:
        m, d, y = match.groups()
        return f"{y}-{int(m):02d}-{int(d):02d}"
    return raw
