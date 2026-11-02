"""
Tests for the derived FRED subcategory layer.

Everything here runs without a database, a network or an API key. The clustering is
driven through the injectable `cluster` hook, and the model boundary is exercised with
stub reply objects -- which is where the real bugs were: a ThinkingBlock at `content[0]`,
and a reply truncated at `max_tokens` that still parses into a confident half-name.
"""

import math

import numpy as np
import pytest

from apps.agentic.db import fred_subcategory as sub
from apps.agentic.db.fred_subcategory import (
    BRANCH_CAP,
    INTERIOR_SYSTEM_PROMPT,
    LEAF_CAP,
    LEAF_SYSTEM_PROMPT,
    NAMING_MAX_TOKENS,
    PROMPT_VERSION,
    Namer,
    centroid_of,
    extract_text,
    interior_user_prompt,
    leaf_user_prompt,
    parse_naming_reply,
    recursive_split,
    split_sizes,
)


def flat(prompt: str) -> str:
    """Collapse the prompt's line wrapping, so assertions test wording not layout."""
    return " ".join(prompt.split())


class Block:
    def __init__(self, type_, text=""):
        self.type = type_
        self.text = text


class Usage:
    def __init__(self, input_tokens=100, output_tokens=50):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens


class Reply:
    def __init__(self, blocks, stop_reason="end_turn", usage=None):
        self.content = blocks
        self.stop_reason = stop_reason
        self.usage = usage or Usage()


class StubAnthropic:
    """Returns queued replies, recording the max_tokens each call asked for."""

    def __init__(self, replies):
        self._replies = list(replies)
        self.budgets: list[int] = []
        self.messages = self

    def create(self, **kwargs):
        self.budgets.append(kwargs["max_tokens"])
        return self._replies.pop(0)


# ------------------------------------------------------------------- the leaf ceiling


def test_the_cap_is_twenty_five():
    assert LEAF_CAP == 25


def test_a_category_at_the_cap_needs_no_levels():
    assert split_sizes(25) == 0


def test_one_over_the_cap_needs_one_level():
    assert split_sizes(26) == 1


def test_a_thousand_series_needs_two_levels():
    assert split_sizes(1000) == 2


def test_the_largest_real_category_needs_three_levels():
    """53,187 series is the largest fetchable category in the live catalogue."""
    assert split_sizes(53187) == 3


# ----------------------------------------------------------------- recursive_split


def _even_cluster(vectors, k):
    """Deterministic round-robin split, so structure is tested without k-means."""
    return np.array([i % k for i in range(len(vectors))])


def _degenerate_cluster(vectors, k):
    """Puts everything in one cluster -- the case that makes naive recursion hang."""
    return np.zeros(len(vectors), dtype=int)


def _leaves(node):
    if not node["children"]:
        return [node]
    return [leaf for child in node["children"] for leaf in _leaves(child)]


def test_a_small_group_is_already_a_leaf():
    vectors = np.zeros((10, 4), dtype="float32")
    tree = recursive_split(range(10), vectors, cluster=_even_cluster)
    assert tree["children"] == []
    assert tree["members"] == list(range(10))


def test_every_leaf_respects_the_cap():
    vectors = np.zeros((500, 4), dtype="float32")
    tree = recursive_split(range(500), vectors, cluster=_even_cluster)
    assert all(len(leaf["members"]) <= LEAF_CAP for leaf in _leaves(tree))


def test_no_member_is_lost_or_duplicated():
    vectors = np.zeros((437, 4), dtype="float32")
    tree = recursive_split(range(437), vectors, cluster=_even_cluster)
    members = [i for leaf in _leaves(tree) for i in leaf["members"]]
    assert sorted(members) == list(range(437))


def test_a_degenerate_clusterer_still_terminates():
    """
    k-means can return a single cluster. Without the forced halving this recurses until
    the stack dies -- and a hang in a long build is indistinguishable from slow progress.
    """
    vectors = np.zeros((120, 4), dtype="float32")
    tree = recursive_split(range(120), vectors, cluster=_degenerate_cluster)
    assert all(len(leaf["members"]) <= LEAF_CAP for leaf in _leaves(tree))


def test_depth_grows_once_the_branch_cap_binds():
    """
    With even clustering a single level suffices up to BRANCH_CAP**2 members, because
    k = ceil(n/cap) still fits under the branching ceiling. Past that the cap binds and
    a third level appears -- which is why three real categories now need depth 3.
    """
    small = np.zeros((BRANCH_CAP * BRANCH_CAP, 4), dtype="float32")
    large = np.zeros((20000, 4), dtype="float32")
    shallow = recursive_split(range(len(small)), small, cluster=_even_cluster)
    deep = recursive_split(range(len(large)), large, cluster=_even_cluster)
    assert max(leaf["depth"] for leaf in _leaves(shallow)) == 2
    assert max(leaf["depth"] for leaf in _leaves(deep)) > 2
    assert all(len(leaf["members"]) <= LEAF_CAP for leaf in _leaves(deep))


def test_a_mean_of_the_cap_is_not_a_maximum_of_the_cap():
    """
    The measured reason recursion is needed at all: one k-means at k = n/cap leaves many
    clusters over it. Here an uneven clusterer makes the point deterministically.
    """
    def lopsided(vectors, k):
        labels = np.zeros(len(vectors), dtype=int)
        labels[: len(vectors) // 2] = 0
        labels[len(vectors) // 2 :] = np.arange(1, len(vectors) - len(vectors) // 2 + 1) % max(k, 2)
        return labels

    vectors = np.zeros((300, 4), dtype="float32")
    tree = recursive_split(range(300), vectors, cluster=lopsided)
    assert all(len(leaf["members"]) <= LEAF_CAP for leaf in _leaves(tree))


# ----------------------------------------------------------------------- centroids


def test_a_centroid_is_unit_length():
    vectors = np.random.default_rng(0).normal(size=(10, 8)).astype("float32")
    assert math.isclose(np.linalg.norm(centroid_of(vectors, range(10))), 1.0, rel_tol=1e-5)


def test_a_centroid_of_identical_vectors_is_that_direction():
    vectors = np.tile(np.array([1.0, 0.0, 0.0, 0.0], dtype="float32"), (5, 1))
    assert centroid_of(vectors, range(5)) == pytest.approx([1.0, 0.0, 0.0, 0.0])


def test_opposing_vectors_do_not_divide_by_zero():
    """A mean of zero must not produce NaNs, or every later comparison silently fails."""
    vectors = np.array([[1.0, 0.0], [-1.0, 0.0]], dtype="float32")
    assert not any(math.isnan(x) for x in centroid_of(vectors, range(2)))


# ------------------------------------------------------------------ reply handling


def test_the_first_text_block_is_used_not_the_first_block():
    """
    haiku-5-5 uses adaptive thinking, so `content[0]` is a ThinkingBlock with no `.text`.
    Indexing block zero raised AttributeError and cost a run.
    """
    reply = Reply([Block("thinking", ""), Block("text", '{"name": "X"}')])
    assert extract_text(reply) == '{"name": "X"}'


def test_a_reply_with_no_text_block_yields_empty_string():
    assert extract_text(Reply([Block("thinking", "")])) == ""


def test_plain_json_parses():
    out = parse_naming_reply('{"name": "Coke oven capacity", "concepts": "steel, coal"}')
    assert out == {"name": "Coke oven capacity", "concepts": "steel, coal"}


def test_fenced_json_parses():
    out = parse_naming_reply('```json\n{"name": "A", "concepts": "b"}\n```')
    assert out["name"] == "A"


def test_truncated_json_is_a_failure_not_a_partial_name():
    """
    The dangerous case. A cut-off object must not yield a name that reads fine with its
    concepts silently missing.
    """
    out = parse_naming_reply('{"name": "Historical industrial output", "concepts": "manufact')
    assert out["name"].startswith("UNNAMED")


def test_prose_instead_of_json_is_a_failure():
    assert parse_naming_reply("Here is the group name you asked for.")["name"].startswith(
        "UNNAMED"
    )


def test_an_empty_reply_is_a_failure():
    assert parse_naming_reply("")["name"].startswith("UNNAMED")


def test_a_name_missing_from_the_json_is_a_failure():
    assert parse_naming_reply('{"concepts": "a, b"}')["name"].startswith("UNNAMED")


# ------------------------------------------------------------------ the retry path


def test_a_truncated_reply_is_retried_with_a_bigger_budget():
    stub = StubAnthropic([
        Reply([Block("thinking"), Block("text", '{"name": "cut off')], stop_reason="max_tokens"),
        Reply([Block("thinking"), Block("text", '{"name": "Good name", "concepts": "a, b"}')]),
    ])
    namer = Namer(client=stub)
    assert namer.name_leaf(["a title"])["name"] == "Good name"
    assert stub.budgets == [NAMING_MAX_TOKENS, NAMING_MAX_TOKENS * 2]
    assert namer.truncated == 1
    assert namer.failures == 0


def test_a_truncated_reply_is_never_parsed():
    """Counting it as truncated rather than parsing it is the whole point."""
    stub = StubAnthropic([
        Reply([Block("text", '{"name": "Plausible but cut')], stop_reason="max_tokens"),
        Reply([Block("text", '{"name": "Plausible but cut')], stop_reason="max_tokens"),
    ])
    namer = Namer(client=stub)
    assert namer.name_leaf(["t"])["name"] == "UNNAMED (reply truncated)"
    assert namer.truncated == 2
    assert namer.failures == 1


def test_tokens_are_counted_across_retries():
    stub = StubAnthropic([
        Reply([Block("text", "x")], stop_reason="max_tokens", usage=Usage(10, 20)),
        Reply([Block("text", '{"name": "N", "concepts": "c"}')], usage=Usage(30, 40)),
    ])
    namer = Namer(client=stub)
    namer.name_leaf(["t"])
    assert (namer.input_tokens, namer.output_tokens) == (40, 60)
    assert namer.calls == 2


def test_cost_uses_the_published_rates():
    namer = Namer(client=object())
    namer.input_tokens, namer.output_tokens = 1_000_000, 1_000_000
    assert namer.cost_usd == pytest.approx(
        sub.NAMING_INPUT_RATE + sub.NAMING_OUTPUT_RATE
    )


# ------------------------------------------------------------------- the prompt itself


def test_the_prompt_is_versioned():
    assert PROMPT_VERSION and PROMPT_VERSION[0].isdigit()


def test_the_leaf_prompt_demands_terms_absent_from_the_titles():
    """
    The vocabulary bridge is the reason this layer works. Without this instruction the
    model echoes the titles' own words back and the concepts field earns nothing.
    """
    assert "do NOT appear in the titles shown" in flat(LEAF_SYSTEM_PROMPT)


def test_the_leaf_prompt_forbids_invented_specifics():
    """Guards the failure mode of a confident label that is wrong for most members."""
    assert "you are shown a sample" in flat(LEAF_SYSTEM_PROMPT)
    assert "date range or units" in flat(LEAF_SYSTEM_PROMPT)


def test_both_prompts_demand_json_only():
    for prompt in (LEAF_SYSTEM_PROMPT, INTERIOR_SYSTEM_PROMPT):
        assert "Reply with JSON only" in flat(prompt)


def test_the_interior_prompt_must_cover_all_children():
    assert "cover ALL the child groups" in flat(INTERIOR_SYSTEM_PROMPT)
    assert "name the group after one child" in flat(INTERIOR_SYSTEM_PROMPT)


def test_the_naming_sample_is_bounded():
    titles = [f"Title {i}" for i in range(500)]
    assert leaf_user_prompt(titles[: sub.NAMING_SAMPLE]).count("\n- ") == sub.NAMING_SAMPLE


def test_the_user_prompts_list_their_inputs():
    assert "- Series A" in leaf_user_prompt(["Series A"])
    assert "- Child A" in interior_user_prompt(["Child A"])


def test_the_branch_cap_matches_the_leaf_cap():
    """A node with 243 children is no more evaluable than a leaf with 1,000 series."""
    assert BRANCH_CAP == LEAF_CAP
