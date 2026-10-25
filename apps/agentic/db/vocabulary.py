"""
The distinct metadata values each Chroma document store holds, and resolution of a
proposed filter value against them.

Why this exists
---------------
Chroma's ``where`` is exact equality on metadata. There is no substring, no regex, and
no LIKE -- and ``$contains``, which the grammar accepts, returns zero rows for every
needle against a string field, including the exact stored value. So a caller who names
an author as "Matthaeus" against a store holding "Troy Stribling, William H. Matthaeus"
matches nothing, with no error to say why. That was the original reported failure.

Resolution is therefore the only mechanism, not an optimisation: a proposed value is
expanded to the exact stored values before any query is built.

Chroma also cannot answer "what values does this field have?" without a full scan --
33.5 s over github's 415,006 chunks. The values are four orders of magnitude smaller
than the chunks (101 repositories, 190 extensions, 27 authors), so they are held in
Postgres and read in microseconds.

See sefer/planning/yada-document-mcp-design.md §4 and §5.
"""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Iterable, Literal, Mapping, Sequence

from sqlalchemy import MetaData, Table, create_engine, delete, select, text
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.engine import Engine

from apps.agentic.core.constants import LANGUAGE_EXTENSIONS
from apps.core.environment import db_url as environment_db_url
from lib.logger import get_logger

logger = get_logger("YADA")

#: Stored as the empty string by ``os.path.splitext`` for a file with no extension --
#: LICENSE, Makefile, Rakefile: 1,995 chunks across 372 files. A caller cannot type an
#: empty string and mean it, so it is given a name. Parentheses cannot occur in a real
#: extension, so the token cannot collide with one. The name says what it SELECTS, not
#: what is absent: omitting ``ext`` searches every extension, passing this searches only
#: the files that have none.
NO_EXTENSION = "(no extension)"

#: The field whose values are whole author lists, so a surname resolves against them.
_SURNAME_FIELD = "authors"
#: The field an account name stands in for: `repo="glyfish"` names an account.
_ACCOUNT_OF = "repo"

ResolutionKind = Literal["exact", "language", "alias", "substring", "empty", "none"]


@dataclass(frozen=True)
class Resolution:
    """What a proposed filter value resolved to, and how."""

    field: str
    proposed: str
    #: The stored values this reaches, for reporting. For an account alias these are the
    #: repositories it holds -- which is what an enumerating tool's refusal has to list.
    values: tuple[str, ...]
    kind: ResolutionKind
    #: Which kind of alias matched, when ``kind == "alias"``. Carried because resolution
    #: is per-operation: ``repo="glyfish"`` resolving to an account's 2,052 files is the
    #: right answer for a search and the wrong one for an enumeration, against a median
    #: repository of 41 files. The tool layer decides; the resolver reports.
    alias_kind: str | None = None
    #: Set when resolution moves to a different field. An account name is not a repo
    #: value, so ``repo="glyfish"`` queries ``{"account": "glyfish"}`` -- one equality
    #: rather than a 22-value ``$in`` over the repositories it covers.
    applied_field: str | None = None
    applied_values: tuple[str, ...] = ()
    #: Distinct values the field holds, so a widening can report its breadth.
    field_total: int = 0

    @property
    def matched(self) -> bool:
        return bool(self.values)

    def where(self) -> dict[str, Any] | None:
        """The Chroma ``where`` fragment, or None when nothing matched."""
        field = self.applied_field or self.field
        values = self.applied_values or self.values
        if not values:
            return None
        if len(values) == 1:
            return {field: values[0]}
        return {field: {"$in": list(values)}}

    def describe(self) -> str:
        """One line for the result's ``filters_resolved``, so a caller sees the decision."""
        if self.kind == "exact":
            return "exact"
        if self.kind == "empty":
            return "files with no extension"
        if self.kind == "language":
            return f"language {self.proposed!r} -> {', '.join(self.values)}"
        if self.kind == "none":
            return "no match"
        if self.alias_kind == "account":
            return f"account '{self.proposed}' -> {len(self.values)} repositories"
        return f"{self.kind}, {len(self.values)} of {self.field_total}"


@dataclass(frozen=True)
class ResolvedFilters:
    """
    A whole filter set resolved at once, shaped for the result contract.

    The three ``filters_*`` views are what a caller needs to see the difference between
    what it asked for and what ran -- the distinction whose absence let a filter match
    nothing and the search quietly return someone else's documents.
    """

    resolutions: tuple[Resolution, ...]
    where: dict[str, Any] | None

    @property
    def unresolvable(self) -> tuple[Resolution, ...]:
        """Values that match nothing. Any of these means: answer now, do not search."""
        return tuple(r for r in self.resolutions if not r.matched)

    @property
    def requested(self) -> dict[str, str]:
        return {r.field: r.proposed for r in self.resolutions}

    @property
    def applied(self) -> dict[str, Any]:
        out: dict[str, Any] = {}
        for r in self.resolutions:
            fragment = r.where()
            if fragment:
                out.update(fragment)
        return out

    @property
    def resolved(self) -> dict[str, str]:
        return {r.field: r.describe() for r in self.resolutions}


def surname(name: str) -> str:
    """
    The last whitespace-separated token of a personal name.

    A surname unifies the spelling variants a store accumulates -- 'W. H. Matthaeus'
    and 'William H. Matthaeus' both yield 'Matthaeus' -- which is what makes naming an
    author by last name exact rather than approximate. Measured on the live library:
    27 full names reduce to 22 surnames, and every surname covering more than one full
    name is the same person written differently, with no genuine collisions.
    """
    parts = [p for p in name.replace(".", ". ").split() if p]
    return parts[-1] if parts else name


def split_authors(value: str) -> list[str]:
    """
    Split a stored author string into individual names.

    The field holds the whole author list as one value -- "Troy Stribling, S. Oughton,
    W. H. Matthaeus" -- which is why a single contributor's name matches nothing by
    equality. Handles the trailing "and" the corpus uses in one entry.
    """
    collapsed = re.sub(r",?\s+and\s+", ", ", value)
    return [p.strip() for p in collapsed.split(",") if p.strip()]


class Vocabulary:
    """
    Reads the vocabulary and resolves proposed filter values against it.

    Initialized once at startup via ``Vocabulary.initialize()``. One table is read --
    the per-combination rows, at most 961 for a store -- and the marginals, the aliases
    and the coverage figures are all derived from it and memoised. They used to be
    tables of their own, which meant two write paths producing counts that had to agree;
    deriving them means there is nothing to keep in step.
    """

    _engine: Engine | None = None
    _scan: Table | None = None
    _combination: Table | None = None
    #: The one table read; everything else is derived from it and memoised below.
    _rows_cache: dict[str, list[tuple[dict, int, int]]] = {}
    _cache: dict[tuple[str, str], dict[str, int]] = {}
    _alias_cache: dict[tuple[str, str], dict[str, tuple[tuple[str, ...], str]]] = {}

    # ---------------------------------------------------------------- lifecycle

    @classmethod
    def initialize(cls, url: str | None = None) -> None:
        resolved = url or environment_db_url()
        cls._engine = create_engine(resolved, pool_pre_ping=True)
        metadata = MetaData()
        metadata.reflect(bind=cls._engine, only=[
            "document_vocabulary_scan", "document_vocabulary_combination"])
        cls._scan = metadata.tables["document_vocabulary_scan"]
        cls._combination = metadata.tables["document_vocabulary_combination"]
        cls._rows_cache.clear()
        cls._cache.clear()
        cls._alias_cache.clear()
        logger.info(f"Vocabulary initialized against {resolved}")

    @classmethod
    def _engine_or_raise(cls) -> Engine:
        if cls._engine is None:
            raise RuntimeError("Vocabulary.initialize() has not been called")
        return cls._engine

    # ------------------------------------------------------------------- reads

    @classmethod
    def rows(cls, store: str) -> list[tuple[dict, int, int]]:
        """
        Every combination row for a store, read once per process.

        One read serves resolution, the generated descriptions and every describe call:
        a store is at most 961 rows, so holding them beats a query per question. This is
        the single source the other reads derive from -- the marginals and aliases used
        to be tables, which meant two write paths producing counts that had to agree.
        """
        if store not in cls._rows_cache:
            k = cls._combination
            assert k is not None
            with cls._engine_or_raise().connect() as conn:
                fetched = conn.execute(
                    select(k.c.field_values, k.c.chunks, k.c.documents).where(k.c.store == store)
                ).fetchall()
            cls._rows_cache[store] = [(v, int(c), int(d)) for v, c, d in fetched]
        return cls._rows_cache[store]

    @classmethod
    def values(cls, store: str, field: str) -> dict[str, int]:
        """{value: chunk count} for one field, summed over the combinations holding it."""
        key = (store, field)
        if key not in cls._cache:
            counts: Counter[str] = Counter()
            for field_values, chunks, _ in cls.rows(store):
                if field in field_values:
                    counts[field_values[field]] += chunks
            cls._cache[key] = dict(counts)
        return cls._cache[key]

    @classmethod
    def aliases(cls, store: str, field: str) -> dict[str, tuple[tuple[str, ...], str]]:
        """
        {alias: ((values it reaches), kind)} -- the names a caller uses that are not
        themselves stored values.

        Derived rather than stored, from the same two rules that used to populate the
        alias table. Both are pure functions of the combinations, so there is nothing to
        keep in sync; ``kind`` is implicit in which rule produced the entry, where it was
        previously a column with a CHECK constraint.
        """
        key = (store, field)
        if key not in cls._alias_cache:
            out: dict[str, tuple[set[str], str]] = {}

            # A surname is not a stored value -- the stored value is the whole author
            # list -- and it unifies that person's spellings. Token-exact, so it beats
            # the substring fallback, under which 'Ng' would match 'Young'.
            if field == _SURNAME_FIELD:
                for value in cls.values(store, field):
                    for name in split_authors(value):
                        out.setdefault(surname(name), (set(), "surname"))[0].add(value)

            # An account shares no characters with most of its repositories, so substring
            # cannot reach them. Both keys are on every github row, so the mapping is
            # just a projection of the combinations.
            if field == _ACCOUNT_OF:
                for field_values, _, _ in cls.rows(store):
                    account, repo = field_values.get("account"), field_values.get(field)
                    if account and repo:
                        out.setdefault(account, (set(), "account"))[0].add(repo)

            cls._alias_cache[key] = {a: (tuple(sorted(v)), kind) for a, (v, kind) in out.items()}
        return cls._alias_cache[key]

    @classmethod
    def coverage(cls, store: str, field: str) -> tuple[int, int]:
        """(chunks carrying this field, chunks in the store).

        A field below the store total is partial, and a filter on it silently excludes
        the chunks that lack it -- so a generated description has to say so.
        """
        rows = cls.rows(store)
        return (sum(c for fv, c, _ in rows if field in fv), sum(c for _, c, _ in rows))

    @classmethod
    def scan_info(cls, store: str) -> tuple[str, int, datetime] | None:
        """(collection, chunks, built_at) for the staleness check, or None if never built."""
        s = cls._scan
        assert s is not None
        with cls._engine_or_raise().connect() as conn:
            row = conn.execute(
                select(s.c.collection, s.c.chunks, s.c.built_at).where(s.c.store == store)
            ).first()
        return (row[0], int(row[1]), row[2]) if row else None

    # -------------------------------------------------------------- resolution

    @classmethod
    def resolve(cls, store: str, field: str, proposed: str) -> Resolution:
        """
        Expand a proposed filter value to the exact stored values it should match.

            exact      the value is stored as given
            empty      ``ext`` only: "" or the (no extension) token
            alias      a surname, or an account name standing for its repositories
            substring  a fragment of one or more stored values
            none       nothing matches -- answer without searching, and say what exists

        Resolution is deliberately not fuzzy beyond substring. A near-miss that resolves
        to the wrong value is worse than one that resolves to nothing, because the first
        is silent and the second is reportable.
        """
        values = cls.values(store, field)
        total = len(values)

        if field == "ext" and proposed in ("", NO_EXTENSION):
            return Resolution(field, proposed, ("",) if "" in values else (), "empty",
                              field_total=total)

        if proposed in values:
            return Resolution(field, proposed, (proposed,), "exact", field_total=total)

        if field == "ext":
            folded = proposed.casefold()

            # A language name, which is what a request actually contains -- nobody asks
            # for ".rb" code, they ask for Ruby. Only the mappings the codebase already
            # specifies, so this stays a lookup and never a guess, and intersected with
            # what is stored so it cannot propose an extension the store lacks.
            #
            # Only without a leading dot. The dot says the caller means an extension
            # literally, and the two readings differ where a language shares its name
            # with one of its extensions: `.c` is .c alone, `c` is C and takes .h too.
            if not folded.startswith("."):
                mapped = LANGUAGE_EXTENSIONS.get(folded)
                if mapped:
                    present = tuple(e for e in mapped if e in values)
                    if present:
                        return Resolution(field, proposed, present, "language",
                                          field_total=total)

            # Otherwise the dot and the case are spelling, not meaning: "py" and "PY"
            # each name one extension, and letting either fall through to substring
            # widens it to .ipynb, .py, .pyi and .pyx -- three wrong values outweighing
            # the intended one. Normalise before widening.
            dotted = folded if folded.startswith(".") else f".{folded}"
            matches = tuple(sorted(v for v in values if v.casefold() == dotted))
            if matches:
                return Resolution(field, proposed, matches, "exact", field_total=total)

        aliased = cls.aliases(store, field).get(proposed)
        if aliased:
            reached, alias_kind = aliased
            # An account is a field of its own, so query it directly rather than listing
            # the repositories under it. The repositories stay in `values` because a
            # refusal has to name them.
            applied = ("account", (proposed,)) if alias_kind == "account" else (None, ())
            return Resolution(field, proposed, reached, "alias", alias_kind,
                              applied[0], applied[1], total)

        needle = proposed.casefold()
        hits = tuple(sorted(v for v in values if needle in v.casefold()))
        if hits:
            return Resolution(field, proposed, hits, "substring", field_total=total)

        return Resolution(field, proposed, (), "none", field_total=total)

    @classmethod
    def resolve_filters(cls, store: str, proposed: Mapping[str, str | None]) -> ResolvedFilters:
        """
        Resolve a whole filter set. ``None`` values are omissions and are skipped.

        When any value resolves to nothing the conjunction is left unbuilt: a filter that
        matches no stored value makes the whole result empty, so the honest answer is to
        say which value is unknown rather than to run a search that cannot succeed. That
        costs microseconds against the 3.0 s the search would have taken to return the
        wrong thing.
        """
        resolutions = tuple(
            cls.resolve(store, field, value)
            for field, value in proposed.items()
            if value is not None
        )
        if any(not r.matched for r in resolutions):
            return ResolvedFilters(resolutions, None)

        fragments = [f for f in (r.where() for r in resolutions) if f]
        if not fragments:
            where = None
        elif len(fragments) == 1:
            where = fragments[0]
        else:
            where = {"$and": fragments}
        return ResolvedFilters(resolutions, where)

    @classmethod
    def available(cls, store: str, field: str, limit: int = 40) -> list[str]:
        """What a field's values actually are, for an unresolvable_filter result."""
        values = cls.values(store, field)
        ordered = sorted(values, key=lambda v: (-values[v], v))
        return [NO_EXTENSION if v == "" else v for v in ordered[:limit]]

    # ------------------------------------------------- the filtered subset (0003)

    @classmethod
    def combinations(cls, store: str,
                     resolutions: Sequence[Resolution] = ()) -> list[tuple[dict, int, int]]:
        """
        The (values, chunks, documents) rows matching a resolved filter set.

        Filtered in memory from the one cached read. A store is at most 961 rows, so a
        scan costs microseconds and a describe does no database work at all after the
        first call -- against 3.8 s to ask Chroma the same question.
        """
        rows = cls.rows(store)
        for r in resolutions:
            field = r.applied_field or r.field
            values = set(r.applied_values or r.values)
            if not values:
                continue
            rows = [row for row in rows if row[0].get(field) in values]
        return rows

    @classmethod
    def facets(cls, store: str, resolutions: Sequence[Resolution] = (),
               fields: Sequence[str] | None = None) -> dict[str, dict[str, int]]:
        """
        {field: {value: chunks}} over the filtered subset.

        This is the whole reason the combination table exists. Built from the marginal
        counts instead, ``describe_code(repo="zgomot")`` would return the store-wide
        extension histogram -- right shape, right counts, wrong question, and plausible
        enough to be cited.
        """
        out: dict[str, Counter[str]] = defaultdict(Counter)
        for values, chunks, _ in cls.combinations(store, resolutions):
            for field, value in values.items():
                if fields is not None and field not in fields:
                    continue
                out[field][NO_EXTENSION if field == "ext" and value == "" else value] += chunks
        return {f: dict(sorted(c.items(), key=lambda kv: (-kv[1], kv[0]))) for f, c in out.items()}

    @classmethod
    def counts(cls, store: str, resolutions: Sequence[Resolution] = ()) -> tuple[int, int]:
        """
        (documents, chunks) over the filtered subset.

        Summing ``documents`` across rows does not double-count: every chunk of a file
        carries the same repo, ext and account, so a file belongs to exactly one
        combination -- as does a library document, whose shelf, authors and title are
        fixed while only its section varies.
        """
        rows = cls.combinations(store, resolutions)
        return sum(d for _, _, d in rows), sum(c for _, c, _ in rows)

    @classmethod
    def prompt_block(cls, store: str, fields: Sequence[str], max_values: int = 120) -> str:
        """
        The real stored values, for an extraction prompt.

        This is the most direct lever there is on extraction accuracy. A model choosing
        a filter blind produces a plausible spelling -- observed: ``{'authors':
        'Matthaeus'}`` against a store where that matches nothing. Shown the values, it
        emits one that exists; shown the counts, it can tell which reading of an
        ambiguous request is plausible, since ``Stribling 3455`` against ``Bates 11``
        says which is likelier meant.

        Ordered by size so a truncated field keeps the values worth naming.
        """
        lines = []
        for field in fields:
            values = cls.values(store, field)
            if not values:
                continue
            ordered = sorted(values.items(), key=lambda kv: (-kv[1], kv[0]))
            shown = ordered[:max_values]
            rendered = ", ".join(
                f"{NO_EXTENSION if v == '' else v} ({n:,})" for v, n in shown)
            more = f", and {len(ordered) - len(shown)} more" if len(ordered) > len(shown) else ""
            lines.append(f"{field} -- {len(ordered)} stored values: {rendered}{more}")

            # Surnames earn their place here: the stored values are whole author lists,
            # so the name a user says is never one of them. Without this the model has
            # to infer that naming one contributor is allowed, from values that all
            # show several. Accounts are left out -- they are listed as a field already.
            surnames = sorted(a for a, (_, kind) in cls.aliases(store, field).items()
                              if kind == "surname")
            if surnames:
                lines.append(
                    f"{field} -- a surname alone also works, and reaches every spelling "
                    f"and every co-authored document: {', '.join(surnames)}")
        return "\n".join(lines)

    # ------------------------------------------------------------------ writes

    @classmethod
    def replace_store(
        cls,
        store: str,
        collection: str,
        chunks: int,
        combinations: Iterable[tuple[dict[str, str], int, int]] = (),
    ) -> None:
        """
        Replace one store's vocabulary in a single transaction.

        Called by the loader, never by hand. Atomic because a half-written vocabulary
        would resolve some values and not others, which is the silent-partial-failure
        this design exists to remove.
        """
        s, k = cls._scan, cls._combination
        assert s is not None and k is not None
        with cls._engine_or_raise().begin() as conn:
            conn.execute(delete(k).where(k.c.store == store))
            rows = [
                {"store": store, "field_values": field_values, "chunks": n, "documents": docs}
                for field_values, n, docs in combinations if n > 0 and docs > 0
            ]
            if rows:
                conn.execute(k.insert(), rows)
            conn.execute(
                insert(s)
                .values(store=store, collection=collection, chunks=chunks,
                        built_at=text("now()"))
                .on_conflict_do_update(
                    index_elements=[s.c.store],
                    set_={"collection": collection, "chunks": chunks, "built_at": text("now()")},
                )
            )
        cls._rows_cache.pop(store, None)
        cls._cache = {key: v for key, v in cls._cache.items() if key[0] != store}
        cls._alias_cache = {key: v for key, v in cls._alias_cache.items() if key[0] != store}
        logger.info(f"Vocabulary for {store}: {len(rows)} combinations, {chunks:,} chunks")
