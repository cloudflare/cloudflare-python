# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "ThreatEventListParams",
    "Search",
    "SearchUnionMember0",
    "SearchUnionMember1",
    "SearchUnionMember2",
    "SearchUnionMember3",
    "SearchUnionMember4",
    "SearchUnionMember5",
    "SearchBranch",
    "SearchBranchUnionMember0",
    "SearchBranchUnionMember1",
    "SearchBranchUnionMember2",
    "SearchBranchUnionMember3",
    "SearchBranchUnionMember4",
    "SearchBranchUnionMember5",
]


class ThreatEventListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    cache: Literal["from-graph"]
    """Cache strategy.

    'from-graph' serves results from the graph-node KV cache when all requested
    UUIDs are cached; falls back to normal path on partial/zero hit.
    """

    cursor: str
    """Cursor for pagination.

    When provided, filters are embedded in the cursor so you only need to pass
    cursor and pageSize. Returned in the previous response's result_info.cursor
    field. Use cursor-based pagination for deep pagination (beyond 100,000 records)
    or for optimal performance.
    """

    dataset_id: Annotated[SequenceNotStr[str], PropertyInfo(alias="datasetId")]
    """
    Dataset UUIDs to query, or one standalone scope value: 'all'/'\\**' or
    'operational' for readable intelligence datasets (isAnalytics=false), or
    'analytics' for readable analytics datasets (isAnalytics=true). Scope values
    query at most 50 datasets. If not provided, uses the default dataset.
    """

    force_refresh: Annotated[bool, PropertyInfo(alias="forceRefresh")]

    format: Literal["json", "stix2", "taxii"]

    order: Literal["asc", "desc"]

    order_by: Annotated[str, PropertyInfo(alias="orderBy")]

    page: float
    """Page number (1-indexed) for offset-based pagination.

    Limited to offset of 100,000 records. For deep pagination, use cursor-based
    pagination instead.
    """

    page_size: Annotated[float, PropertyInfo(alias="pageSize")]
    """Number of results per page. Maximum 25,000."""

    search: Iterable[Search]

    search_branches: Annotated[Iterable[Iterable[SearchBranch]], PropertyInfo(alias="searchBranches")]
    """JSON-encoded.

    OR branches of structured search filters. Filters within a branch are AND'd,
    branches are OR'd, and the result is AND'd with `search`:
    `AND(search) AND OR(AND(branch 1), ...)`. Max 8 branches of 1-10 conditions
    each. Not supported for analytics datasets, and `indicator` filters are not yet
    supported inside branches. Cursor pages carry the original branches, so do not
    resend them with `cursor`.
    """


class SearchUnionMember0(TypedDict, total=False):
    field: Required[
        Literal[
            "attacker",
            "attackerCountry",
            "category",
            "createdAt",
            "date",
            "event",
            "indicator",
            "indicatorType",
            "mitreAttack",
            "mitreCapec",
            "tags",
            "targetCountry",
            "targetIndustry",
            "tlp",
            "uuid",
        ]
    ]

    op: Required[
        Literal["equals", "not", "gt", "gte", "lt", "lte", "like", "contains", "startsWith", "endsWith", "find"]
    ]

    value: Required[str]


class SearchUnionMember1(TypedDict, total=False):
    field: Required[
        Literal[
            "attacker",
            "attackerCountry",
            "category",
            "createdAt",
            "date",
            "event",
            "indicator",
            "indicatorType",
            "mitreAttack",
            "mitreCapec",
            "tags",
            "targetCountry",
            "targetIndustry",
            "tlp",
            "uuid",
        ]
    ]

    op: Required[Literal["in"]]

    value: Required[SequenceNotStr[str]]


class SearchUnionMember2(TypedDict, total=False):
    field: Required[Literal["killChain"]]

    op: Required[Literal["equals", "not", "gt", "gte", "lt", "lte"]]

    value: Required[Union[float, str]]


class SearchUnionMember3(TypedDict, total=False):
    field: Required[Literal["killChain"]]

    op: Required[Literal["in"]]

    value: Required[SequenceNotStr[Union[float, str]]]


class SearchUnionMember4(TypedDict, total=False):
    field: Required[Literal["hasChildren"]]

    op: Required[Literal["equals", "not", "gt", "gte", "lt", "lte"]]

    value: Required[Union[bool, object]]


class SearchUnionMember5(TypedDict, total=False):
    field: Required[Literal["hasChildren"]]

    op: Required[Literal["in"]]

    value: Required[Iterable[Union[bool, object]]]


Search: TypeAlias = Union[
    SearchUnionMember0,
    SearchUnionMember1,
    SearchUnionMember2,
    SearchUnionMember3,
    SearchUnionMember4,
    SearchUnionMember5,
]


class SearchBranchUnionMember0(TypedDict, total=False):
    field: Required[
        Literal[
            "attacker",
            "attackerCountry",
            "category",
            "createdAt",
            "date",
            "event",
            "indicator",
            "indicatorType",
            "mitreAttack",
            "mitreCapec",
            "tags",
            "targetCountry",
            "targetIndustry",
            "tlp",
            "uuid",
        ]
    ]

    op: Required[
        Literal["equals", "not", "gt", "gte", "lt", "lte", "like", "contains", "startsWith", "endsWith", "find"]
    ]

    value: Required[str]


class SearchBranchUnionMember1(TypedDict, total=False):
    field: Required[
        Literal[
            "attacker",
            "attackerCountry",
            "category",
            "createdAt",
            "date",
            "event",
            "indicator",
            "indicatorType",
            "mitreAttack",
            "mitreCapec",
            "tags",
            "targetCountry",
            "targetIndustry",
            "tlp",
            "uuid",
        ]
    ]

    op: Required[Literal["in"]]

    value: Required[SequenceNotStr[str]]


class SearchBranchUnionMember2(TypedDict, total=False):
    field: Required[Literal["killChain"]]

    op: Required[Literal["equals", "not", "gt", "gte", "lt", "lte"]]

    value: Required[Union[float, str]]


class SearchBranchUnionMember3(TypedDict, total=False):
    field: Required[Literal["killChain"]]

    op: Required[Literal["in"]]

    value: Required[SequenceNotStr[Union[float, str]]]


class SearchBranchUnionMember4(TypedDict, total=False):
    field: Required[Literal["hasChildren"]]

    op: Required[Literal["equals", "not", "gt", "gte", "lt", "lte"]]

    value: Required[Union[bool, object]]


class SearchBranchUnionMember5(TypedDict, total=False):
    field: Required[Literal["hasChildren"]]

    op: Required[Literal["in"]]

    value: Required[Iterable[Union[bool, object]]]


SearchBranch: TypeAlias = Union[
    SearchBranchUnionMember0,
    SearchBranchUnionMember1,
    SearchBranchUnionMember2,
    SearchBranchUnionMember3,
    SearchBranchUnionMember4,
    SearchBranchUnionMember5,
]
