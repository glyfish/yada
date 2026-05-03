from __future__ import annotations

import json
from dataclasses import dataclass


@dataclass
class SeriesRef:
    source: str
    native_id: str
    cache_id: str


    def to_json(self) -> str:
        return json.dumps({
            "source": self.source,
            "native_id": self.native_id,
            "cache_id": self.cache_id,
        })


    @classmethod
    def from_json(cls, s: str) -> SeriesRef:
        d = json.loads(s)
        return cls(
            source=d["source"],
            native_id=d["native_id"],
            cache_id=d["cache_id"],
        )
