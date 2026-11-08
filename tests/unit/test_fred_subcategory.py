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
    SCOPES,
    SPLIT_VERSION,
    Namer,
    balanced_clusters,
    centroid_of,
    modelled_nodes,
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


# --------------------------------------------------------------- balanced clustering


def _plain_kmeans(vectors, k):
    """The clusterer this module used before `balanced_clusters`."""
    from sklearn.cluster import KMeans

    return KMeans(n_clusters=k, n_init=3, random_state=0).fit_predict(vectors)


def _skewed(n: int, dims: int = 8, seed: int = 0):
    """
    One dense blob and a thin spread, which is the shape real title embeddings have.

    Plain k-means puts most of the blob in one cluster; that cluster then recurses, which
    is where the depth came from.
    """
    rng = np.random.default_rng(seed)
    dense = rng.normal(scale=0.02, size=(int(n * 0.8), dims))
    spread = rng.normal(scale=1.0, size=(n - int(n * 0.8), dims))
    points = np.vstack([dense, spread]).astype("float32")
    return points / np.linalg.norm(points, axis=1, keepdims=True)


def test_balanced_clusters_sizes_differ_by_at_most_one():
    """The whole point: `k` groups of `ceil(n / k)`, not whatever k-means felt like."""
    vectors = _skewed(300)
    labels = balanced_clusters(vectors, 12)
    sizes = np.bincount(labels, minlength=12)
    assert sizes.sum() == 300
    assert sizes.max() - sizes.min() <= 1


def test_balanced_clusters_places_every_point():
    vectors = _skewed(137)
    labels = balanced_clusters(vectors, 7)
    assert (labels >= 0).all(), "a point left unassigned would vanish from the tree"


def test_balanced_clusters_is_deterministic():
    """A rebuild has to reproduce the tree, or `split_version` means nothing."""
    vectors = _skewed(200)
    assert (balanced_clusters(vectors, 9) == balanced_clusters(vectors, 9)).all()


def test_balancing_is_what_keeps_the_tree_shallow():
    """
    The measured reason `balanced_clusters` exists. On real data a 9,932-series category
    reached depth 8 with 1,105 nodes under plain k-means and depth 3 with 426 under
    balancing. Reproduced here on synthetic skew so it is checkable without a network.
    """
    vectors = _skewed(1200)
    plain = recursive_split(range(1200), vectors, cluster=_plain_kmeans)
    balanced = recursive_split(range(1200), vectors)

    plain_depth = max(leaf["depth"] for leaf in _leaves(plain))
    balanced_depth = max(leaf["depth"] for leaf in _leaves(balanced))
    assert balanced_depth < plain_depth
    # Cheaper as well as shallower: every node is a naming call.
    assert len(_leaves(balanced)) < len(_leaves(plain))


def test_balancing_does_not_produce_singleton_leaves():
    """
    Plain k-means stranded 9 series in leaves of their own on a real category. A
    "browsable group" holding one item is noise with a name attached.
    """
    vectors = _skewed(1200)
    sizes = [len(leaf["members"]) for leaf in _leaves(recursive_split(range(1200), vectors))]
    assert min(sizes) > 1


def test_the_branch_cap_is_enforced_not_just_documented():
    """
    It was documented and unenforced: the k ceiling read `branch ** 2`, so a node could
    take 625 children. 130 of the 723 non-regional categories were over the threshold
    that triggers it.
    """
    vectors = _skewed(5000)
    tree = recursive_split(range(5000), vectors)
    nodes, over = [tree], []
    while nodes:
        node = nodes.pop()
        if len(node["children"]) > BRANCH_CAP:
            over.append(len(node["children"]))
        nodes.extend(node["children"])
    assert over == []


def test_the_leaf_cap_still_holds_under_balancing():
    vectors = _skewed(5000)
    tree = recursive_split(range(5000), vectors)
    assert all(len(leaf["members"]) <= LEAF_CAP for leaf in _leaves(tree))


def test_balancing_loses_no_members():
    vectors = _skewed(911)
    tree = recursive_split(range(911), vectors)
    members = [i for leaf in _leaves(tree) for i in leaf["members"]]
    assert sorted(members) == list(range(911))


# ------------------------------------------------------------------- naming the tree


class CountingNamer:
    """Records the order names were requested in, and from how many threads."""

    def __init__(self):
        self.leaf_calls = []
        self.interior_calls = []
        self.threads = set()

    def _note(self):
        import threading

        self.threads.add(threading.get_ident())

    def name_leaf(self, titles):
        self._note()
        self.leaf_calls.append(tuple(titles))
        return {"name": "leaf:" + "|".join(titles), "concepts": "c"}

    def name_interior(self, child_names):
        self._note()
        self.interior_calls.append(tuple(child_names))
        return {"name": "interior:" + "|".join(child_names), "concepts": "c"}


def _name_with(workers):
    vectors = _skewed(300)
    tree = recursive_split(range(300), vectors)
    titles = [f"title {i}" for i in range(300)]
    namer = CountingNamer()
    sub._name_tree(tree, titles, namer, workers=workers)
    return tree, namer


def _names(node):
    return [node["name"]] + [n for child in node["children"] for n in _names(child)]


def test_concurrent_naming_produces_the_same_tree_as_sequential():
    """
    Names do not depend on the order within a level -- a node is named from its own
    members or its own children's names, never from a sibling. If that stopped being
    true, concurrency would silently stop being reproducible.
    """
    sequential, _ = _name_with(workers=1)
    concurrent, _ = _name_with(workers=8)
    assert _names(sequential) == _names(concurrent)


def test_concurrent_naming_actually_uses_threads():
    _, namer = _name_with(workers=8)
    assert len(namer.threads) > 1, "the pool collapsed to one worker"


def test_every_node_is_named_exactly_once():
    tree, namer = _name_with(workers=8)
    total = len(_names(tree))
    assert len(namer.leaf_calls) + len(namer.interior_calls) == total


def test_an_interior_node_is_named_from_its_children_not_its_series():
    """
    Naming a node two levels up from a sample of its series describes the sample and
    reads as describing the subtree -- confidently, and wrongly.
    """
    tree, _ = _name_with(workers=8)
    assert tree["name"].startswith("interior:")
    for child in tree["children"]:
        assert child["name"] in tree["name"]


def test_a_naming_failure_in_the_pool_is_raised_not_swallowed():
    """
    A tree written with an unnamed branch in it is worse than a category recorded as
    `error`, because nothing downstream can tell it from a complete one.
    """
    vectors = _skewed(200)
    tree = recursive_split(range(200), vectors)

    class Exploding(CountingNamer):
        def name_leaf(self, titles):
            raise RuntimeError("overloaded")

    with pytest.raises(RuntimeError):
        sub._name_tree(tree, [f"t{i}" for i in range(200)], Exploding(), workers=4)


def test_namer_counters_survive_concurrent_calls():
    """
    Unguarded `+=` under a thread pool under-reports, and the spend is the one number
    this build has to get right.
    """
    from concurrent.futures import ThreadPoolExecutor

    reply = '{"name": "n", "concepts": "c"}'
    namer = Namer(
        client=StubAnthropic([Reply([Block("text", reply)]) for _ in range(200)])
    )
    with ThreadPoolExecutor(max_workers=8) as pool:
        list(pool.map(lambda _: namer.name_leaf(["t"]), range(200)))
    assert namer.calls == 200
    assert namer.input_tokens == 200 * 100
    assert namer.output_tokens == 200 * 50
    assert namer.failures == 0


# ------------------------------------------------------------------------- versioning


def test_the_split_is_versioned_like_the_prompt():
    """
    The names are not the only derived thing here; the shape is too. A tree half-built
    under two splitters is no more comparable than one half-built under two prompts.
    """
    assert SPLIT_VERSION
    assert SPLIT_VERSION != PROMPT_VERSION


# ----------------------------------------------------------------------------- scopes


def test_the_scopes_partition_the_catalogue():
    """`non-regional` and `regional` must not overlap, or a build pays twice."""
    assert SCOPES["all"] == ""
    assert "NOT LIKE" in SCOPES["non-regional"]
    assert "NOT LIKE" not in SCOPES["regional"]
    assert "LIKE" in SCOPES["regional"]
    prefix = "U.S. Regional Data%"
    assert prefix in SCOPES["non-regional"] and prefix in SCOPES["regional"]


def test_there_is_no_implicit_whole_catalogue_default():
    """
    `pending_builds` used to return every over-cap category, so `build()` with no
    argument would have spent the regional budget by accident.
    """
    import inspect

    default = inspect.signature(sub.pending_builds).parameters["scope"].default
    assert default == "non-regional"
    assert inspect.signature(sub.build).parameters["scope"].default == "non-regional"


# ------------------------------------------------------------------------ cost model


@pytest.mark.parametrize("size", [26, 100, 454, 2790, 9932, 20000])
def test_the_cost_model_matches_the_splitter(size):
    """
    The dry-run quotes a dollar figure from `modelled_nodes`. If the two drift, a plan
    gets approved against a number the run cannot reproduce -- which is how the $4.29
    estimate in the procedure came to be low.
    """
    vectors = _skewed(size, seed=size)
    tree = recursive_split(range(size), vectors)
    actual = len(_names_of_shape(tree))
    assert actual == modelled_nodes(size), (
        f"{size} series: splitter made {actual} nodes, model said {modelled_nodes(size)}"
    )


def _names_of_shape(node):
    return [node] + [n for child in node["children"] for n in _names_of_shape(child)]


def test_the_model_counts_a_category_under_the_cap_as_one_node():
    assert modelled_nodes(LEAF_CAP) == 1
    assert modelled_nodes(1) == 1


def test_the_model_never_returns_fewer_nodes_than_leaves_are_needed():
    """A sanity floor: you cannot cover n series with fewer than ceil(n / cap) leaves."""
    for size in (26, 500, 5000, 53187):
        assert modelled_nodes(size) >= math.ceil(size / LEAF_CAP)
