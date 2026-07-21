# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["IndicatorListParams", "Search", "TagSearch"]


class IndicatorListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    cache: Literal["from-graph"]
    """Cache strategy.

    'from-graph' serves results from the graph-node KV cache when all requested
    UUIDs are cached; falls back to normal path on partial/zero hit.
    """

    created_after: Annotated[Union[str, datetime], PropertyInfo(alias="createdAfter", format="iso8601")]
    """Filter indicators created on or after this date.

    Must use ISO 8601 format (e.g., '2024-01-15T00:00:00Z').
    """

    created_before: Annotated[Union[str, datetime], PropertyInfo(alias="createdBefore", format="iso8601")]
    """Filter indicators created on or before this date.

    Must use ISO 8601 format (e.g., '2024-12-31T23:59:59Z').
    """

    dataset_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="datasetIds")]
    """
    Dataset IDs to query indicators from (array of UUIDs), or special value 'all' or
    '\\**' to query all datasets. If not provided, uses the default dataset.
    """

    format: Literal["json", "stix2", "taxii"]
    """Output format for indicator data.

    'json' returns the default format, 'stix2' returns STIX 2.1 Indicator SDOs,
    'taxii' returns a TAXII 2.1 Envelope with Content-Type
    application/taxii+json;version=2.1.
    """

    include_tags: Annotated[bool, PropertyInfo(alias="includeTags")]
    """Whether to include full tag details for each indicator. Defaults to true."""

    include_total_count: Annotated[bool, PropertyInfo(alias="includeTotalCount")]
    """Whether to compute accurate total count via COUNT(\\**).

    Defaults to false for performance. When false, total_count is an approximation.
    """

    indicator_type: Annotated[str, PropertyInfo(alias="indicatorType")]

    name: str
    """Filter indicators by value using substring match (LIKE).

    Legacy alternative to structured search.
    """

    page: float

    page_size: Annotated[float, PropertyInfo(alias="pageSize")]

    related_events: Annotated[SequenceNotStr[str], PropertyInfo(alias="relatedEvents")]
    """Filter by related event IDs"""

    related_events_limit: Annotated[float, PropertyInfo(alias="relatedEventsLimit")]
    """Limit the number of related events returned per indicator.

    Default: 2. Set to 0 for none, -1 for all events.
    """

    search: Iterable[Search]
    """Structured search as a JSON array of {field, op, value} objects.

    Searchable fields: value, indicatorType, uuid. Supports operators: equals, not,
    contains, startsWith, endsWith, gt, lt, gte, lte, like, in, find. Use the 'in'
    operator with an array value to bulk-check up to 100 indicators in a single
    request, e.g.
    search=[{"field":"value","op":"in","value":["evil.com","bad.org"]}]. Multiple
    conditions are AND'd together. Max 10 conditions per request.
    """

    source: Literal["do", "r2catalog"]
    """Read backend.

    'do' (default) reads Durable Object storage. 'r2catalog' reads R2 Data Catalog
    (admin-only, experimental; supports a subset of search fields).
    """

    tags: SequenceNotStr[str]
    """Filter by tag values or UUIDs.

    Indicators must have at least one of the specified tags (OR logic). Supports
    both tag UUID and tag value.
    """

    tag_search: Annotated[Iterable[TagSearch], PropertyInfo(alias="tagSearch")]
    """Structured tag-metadata filter as a JSON array of {field, op, value} objects.

    Operates against the per-dataset IndicatorTag mirror so you can find indicators
    by tag attributes (origin country, motive, sophistication, priority, etc.)
    without a separate Tags lookup. Common dashboard usage: drill from a country
    into indicators, e.g.
    tagSearch=[{"field":"originCountryISO","op":"in","value":["IR","CN"]}]. Country
    values may be passed as alpha-2, alpha-3, name, or alias (e.g. "iran").
    Operators: equals, not, gt/gte/lt/lte (numeric only),
    contains/like/find/startsWith/endsWith (string only), in. AND-joined across
    entries; combined with `tags`, a matching tag must satisfy both. Max 10 entries
    per request, max 100 values per 'in'. Performance notes: `originCountryISO` uses
    its B-tree index for equals/not/in. `priority` uses its B-tree index for numeric
    comparisons. Other string columns (`actorCategory`, `motive`, etc.) are
    case-insensitive and unindexed; current catalog size makes this a non-issue.
    `endsWith` and `aliasGroupNames` contains/like are leading-wildcard scans and
    slow on large result sets. `aliasGroupNames` matches on the JSON-encoded text,
    so substrings can cross alias boundaries ("apt28" also matches "apt280" when
    both appear in the same tag's alias list).
    """


class Search(TypedDict, total=False):
    field: Required[Literal["value", "indicatorType", "uuid"]]
    """The indicator field to search on. Allowed: value, indicatorType, uuid."""

    op: Required[
        Literal["equals", "not", "gt", "gte", "lt", "lte", "like", "contains", "startsWith", "endsWith", "in", "find"]
    ]
    """Search operator.

    Use 'in' for bulk lookup of up to 100 values at once, e.g. {field:'value',
    op:'in', value:['evil.com','bad.org']}.
    """

    value: Required[Union[str, SequenceNotStr[str]]]
    """Search value.

    String for most operators. Array of strings for 'in' operator (max 100 items).
    """


class TagSearch(TypedDict, total=False):
    field: Required[
        Literal[
            "value",
            "categoryId",
            "actorCategory",
            "aliasGroupNames",
            "attributionConfidence",
            "attributionOrganization",
            "motive",
            "opsecLevel",
            "originCountryISO",
            "sophisticationLevel",
            "priority",
            "analyticPriority",
        ]
    ]
    """Tag mirror field to filter on.

    Allowed: value, categoryId, actorCategory, aliasGroupNames,
    attributionConfidence, attributionOrganization, motive, opsecLevel,
    originCountryISO, sophisticationLevel, priority, analyticPriority. Filters
    operate against the per-dataset IndicatorTag mirror (which is kept in sync with
    the Tags SoT by the tag-propagation workflow).
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
    values may be passed as alpha-2, alpha-3, name, or common alias (e.g. "iran",
    "IR", "IRN") and are normalized to alpha-2 server-side.
    """
