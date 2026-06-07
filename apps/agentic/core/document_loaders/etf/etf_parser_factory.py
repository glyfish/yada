from __future__ import annotations

from apps.agentic.core.document_loaders.etf.etf_parser import ETFParser
from apps.agentic.core.document_loaders.etf.parsers.vaneck_parser import VanEckParser
from apps.agentic.core.document_loaders.etf.parsers.wisdomtree_parser import WisdomTreeParser
from apps.agentic.core.document_loaders.etf.parsers.statestreet_parser import StateStreetParser
from apps.agentic.core.document_loaders.etf.parsers.vanguard_parser import VanguardParser
from apps.agentic.core.document_loaders.etf.parsers.proshares_parser import ProSharesParser
from apps.agentic.core.document_loaders.etf.parsers.ishares_parser import ISharesParser

_REGISTRY: dict[str, ETFParser] = {
    "vaneck": VanEckParser(),
    "wisdomtree": WisdomTreeParser(),
    "statestreet": StateStreetParser(),
    "vanguard": VanguardParser(),
    "proshares": ProSharesParser(),
    "ishares": ISharesParser(),
}


class ETFParserFactory:

    @staticmethod
    def get(source: str) -> ETFParser:
        parser = _REGISTRY.get(source.lower())
        if parser is None:
            available = ", ".join(_REGISTRY.keys())
            raise ValueError(
                f"No ETF parser registered for source '{source}'. Available: {available}"
            )
        return parser

    @staticmethod
    def sources() -> list[str]:
        return list(_REGISTRY.keys())
