# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["GraphListParams"]


class GraphListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    cursor: str
    """Opaque pagination token.

    Only valid when seeds has exactly 1 entry; 400 otherwise.
    """

    dataset_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="datasetIds")]
    """Comma-separated dataset UUIDs to restrict neighbor scope.

    Intersected with ACL grants.
    """

    direction: str
    """
    Edge direction relative to each seed: out (seed→neighbors), in (neighbors→seed),
    both (default).
    """

    expand: SequenceNotStr[str]
    """Comma-separated list of response sections to expand (hydrate).

    Allowed: `nodes`. Omitting `expand` returns identifier-only nodes.
    """

    hydration: str
    """Hydration strategy for neighbor nodes when expand=nodes is set.

    r2_join (default): use R2 JOIN query + DO fallback. do_only: use plain R2
    query + hydrate all neighbors via Durable Objects.
    """

    limit: float
    """Max neighbors per seed (default: 100, max: 1000). Values above 1000 return 400."""

    max_nodes: float
    """Total accumulated node cap across all seeds (default: 500, max: 1000).

    Values above 1000 return 400.
    """

    relationship_types: Annotated[SequenceNotStr[str], PropertyInfo(alias="relationshipTypes")]
    """Comma-separated relationship types to filter by.

    Allowed: tagged_with, appears_in, related_to, caused_by, attributed_to.
    """

    seeds: SequenceNotStr[str]
    """Comma-separated compact seed ids (type:uuid).

    Example: seeds=event:550e8400-...,indicator:661fa920-... Provide 1–50 entries;
    omitting seeds returns 400.
    """
