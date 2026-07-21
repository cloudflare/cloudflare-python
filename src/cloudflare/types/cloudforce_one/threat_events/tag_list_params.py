# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["TagListParams", "Filter"]


class TagListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    cache: Literal["from-graph"]
    """Cache strategy.

    'from-graph' serves results from the graph-node KV cache when all requested
    UUIDs are cached; falls back to normal path on partial/zero hit.
    """

    category_uuid: Annotated[str, PropertyInfo(alias="categoryUuid")]

    filters: Iterable[Filter]
    """Structured filters as a JSON array of {field, op, value} objects.

    Searchable fields: uuid, value, actorCategory, actorCategoryConfidence,
    aliasGroupNames, attributionConfidence, attributionConfidenceScore,
    attributionOrganization, categoryName, motive, motiveConfidence, opsecLevel,
    originCountryISO, originCountryConfidence, sophisticationLevel, priority,
    analyticPriority. Operators: equals, not, contains, startsWith, endsWith, gt,
    lt, gte, lte, like, in, find. Use 'in' for bulk OR within a single field, e.g.
    filters=[{"field":"originCountryISO","op":"in","value":["IR","CN"]}]. Multiple
    entries are AND-joined. Max 10 entries per request, max 100 values per 'in'.
    Per-field notes: `uuid` accepts only 'equals' and 'in' (other operators throw
    ValidationError) — matched against the canonical lowercase storage but callers
    may pass either case (the server lowercases before comparison); index-backed by
    the column's UNIQUE constraint and intended for batched UUID → tag resolution.
    `originCountryISO` uses its B-tree index for equals/not/in. `priority` uses its
    B-tree index for numeric comparisons. Other string columns (`actorCategory`,
    `motive`, etc.) are case-insensitive and unindexed; current catalog size makes
    this a non-issue. `endsWith` and `aliasGroupNames` contains/like are
    leading-wildcard scans and slow on large result sets. `aliasGroupNames` matches
    on the JSON-encoded text, so substrings can cross alias boundaries (a search for
    "apt28" will also match "apt280" if both appear in the same tag's alias list).
    """

    page: float

    page_size: Annotated[float, PropertyInfo(alias="pageSize")]

    search: str
    """Legacy free-text substring match on tag value."""


class Filter(TypedDict, total=False):
    field: Required[
        Literal[
            "uuid",
            "value",
            "actorCategory",
            "actorCategoryConfidence",
            "aliasGroupNames",
            "attributionConfidence",
            "attributionConfidenceScore",
            "attributionOrganization",
            "categoryName",
            "motive",
            "motiveConfidence",
            "opsecLevel",
            "originCountryISO",
            "originCountryConfidence",
            "sophisticationLevel",
            "priority",
            "analyticPriority",
        ]
    ]
    """Tag field to search on.

    Allowed: uuid, value, actorCategory, actorCategoryConfidence, aliasGroupNames,
    attributionConfidence, attributionConfidenceScore, attributionOrganization,
    categoryName, motive, motiveConfidence, opsecLevel, originCountryISO,
    originCountryConfidence, sophisticationLevel, priority, analyticPriority.
    """

    op: Required[
        Literal["equals", "not", "gt", "gte", "lt", "lte", "like", "contains", "startsWith", "endsWith", "in", "find"]
    ]
    """Search operator.

    Use 'in' for bulk OR within a single field, e.g. {field:"originCountryISO",
    op:"in", value:["IR","CN"]}.
    """

    value: Union[str, float, SequenceNotStr[Union[str, float]]]
    """Search value.

    String or number for most operators. Array for 'in' (max 100 items). Country
    values may be passed as alpha-2, alpha-3, name, or common alias (e.g. 'iran',
    'IR', 'IRN') and are normalized to alpha-2 server-side.
    """
