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

    Searchable fields: uuid, value, categoryName, description, dateOfDiscovery, tlp,
    confidence, actorCategory, motive, attributionOrganization, originCountryISO,
    aliases, externalReferences, opsecLevel, sophisticationLevel, activeDuration,
    priority, lastSeen, aliasGroupNames. Operators: equals, not, contains,
    startsWith, endsWith, gt, lt, gte, lte, like, in, find. Use 'in' for bulk OR
    within a single field, e.g.
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
    """Free-text substring match on tag value AND custom-field properties.

    Searches case-insensitively inside both `Tag.value` and the serialized
    `Tag.properties` JSON blob (keys, values, and annotation metadata like
    confidence/tlp are all searchable). Same serialized-text tradeoff as
    `aliasGroupNames` — substrings can cross JSON boundaries.
    """


class Filter(TypedDict, total=False):
    field: Required[str]
    """Tag field to search on.

    Allowed first-class fields: uuid, value, categoryName, description,
    dateOfDiscovery, tlp, confidence, actorCategory, motive,
    attributionOrganization, originCountryISO, aliases, externalReferences,
    opsecLevel, sophisticationLevel, activeDuration, priority, lastSeen,
    aliasGroupNames. Also supports properties.<key> to filter on custom field values
    (matches both raw values and annotated {value,confidence,tlp} shapes via
    COALESCE), and properties.<key>.tlp / properties.<key>.confidence to filter
    directly on annotation sub-fields.
    """

    op: Required[
        Literal["equals", "not", "gt", "gte", "lt", "lte", "like", "contains", "startsWith", "endsWith", "in", "find"]
    ]
    """Search operator. Use 'in' for bulk OR within a single field."""

    value: Union[str, float, SequenceNotStr[Union[str, float]]]
    """Search value.

    String or number for most operators. Array for 'in' (max 100 items).
    """
