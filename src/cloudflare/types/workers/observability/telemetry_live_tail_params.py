# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "TelemetryLiveTailParams",
    "Filter",
    "FilterUnionMember0",
    "FilterUnionMember0Filter",
    "FilterUnionMember0FilterUnionMember0",
    "FilterUnionMember0FilterWorkersObservabilityFilterLeaf",
    "FilterWorkersObservabilityFilterLeaf",
]


class TelemetryLiveTailParams(TypedDict, total=False):
    account_id: Required[str]

    filter_combination: Annotated[Literal["and", "or", "AND", "OR"], PropertyInfo(alias="filterCombination")]
    """Set a flag to describe how to combine the filters on the query."""

    filters: Iterable[Filter]
    """Apply filters to the query. Supports nested groups via kind: 'group'."""

    script_id: Annotated[str, PropertyInfo(alias="scriptId")]


class FilterUnionMember0FilterUnionMember0(TypedDict, total=False):
    filter_combination: Required[Annotated[Literal["and", "or", "AND", "OR"], PropertyInfo(alias="filterCombination")]]

    filters: Required[Iterable[object]]

    kind: Required[Literal["group"]]


class FilterUnionMember0FilterWorkersObservabilityFilterLeaf(TypedDict, total=False):
    """A filter condition applied to query results.

    Use the keys and values endpoints to discover available fields and their values before constructing filters.
    """

    key: Required[str]
    """Filter field name.

    Use verified keys from previous query results or the keys endpoint. Common keys
    include $metadata.service, $metadata.origin, $metadata.trigger,
    $metadata.message, and $metadata.error.
    """

    operation: Required[
        Literal[
            "includes",
            "not_includes",
            "starts_with",
            "ends_with",
            "regex",
            "exists",
            "is_null",
            "in",
            "not_in",
            "eq",
            "neq",
            "gt",
            "gte",
            "lt",
            "lte",
            "=",
            "!=",
            ">",
            ">=",
            "<",
            "<=",
            "INCLUDES",
            "DOES_NOT_INCLUDE",
            "MATCH_REGEX",
            "EXISTS",
            "DOES_NOT_EXIST",
            "IN",
            "NOT_IN",
            "STARTS_WITH",
            "ENDS_WITH",
        ]
    ]
    """Comparison operator.

    String operators: includes, not_includes, starts_with, ends_with, regex.
    Existence: exists, is_null. Set membership: in, not_in (comma-separated values).
    Numeric: eq, neq, gt, gte, lt, lte.
    """

    type: Required[Literal["string", "number", "boolean"]]
    """Data type of the filter field.

    Must match the actual type of the key being filtered.
    """

    kind: Literal["filter"]
    """Discriminator for leaf filter nodes.

    Always 'filter' when present; may be omitted.
    """

    value: Union[str, float, bool]
    """Comparison value.

    Must match actual values in your data — verify with the values endpoint. Ensure
    the value type (string/number/boolean) matches the field type. String
    comparisons are case-sensitive. Regex uses RE2 syntax (no
    lookaheads/lookbehinds).
    """


FilterUnionMember0Filter: TypeAlias = Union[
    FilterUnionMember0FilterUnionMember0, FilterUnionMember0FilterWorkersObservabilityFilterLeaf
]


class FilterUnionMember0(TypedDict, total=False):
    filter_combination: Required[Annotated[Literal["and", "or", "AND", "OR"], PropertyInfo(alias="filterCombination")]]

    filters: Required[Iterable[FilterUnionMember0Filter]]

    kind: Required[Literal["group"]]


class FilterWorkersObservabilityFilterLeaf(TypedDict, total=False):
    """A filter condition applied to query results.

    Use the keys and values endpoints to discover available fields and their values before constructing filters.
    """

    key: Required[str]
    """Filter field name.

    Use verified keys from previous query results or the keys endpoint. Common keys
    include $metadata.service, $metadata.origin, $metadata.trigger,
    $metadata.message, and $metadata.error.
    """

    operation: Required[
        Literal[
            "includes",
            "not_includes",
            "starts_with",
            "ends_with",
            "regex",
            "exists",
            "is_null",
            "in",
            "not_in",
            "eq",
            "neq",
            "gt",
            "gte",
            "lt",
            "lte",
            "=",
            "!=",
            ">",
            ">=",
            "<",
            "<=",
            "INCLUDES",
            "DOES_NOT_INCLUDE",
            "MATCH_REGEX",
            "EXISTS",
            "DOES_NOT_EXIST",
            "IN",
            "NOT_IN",
            "STARTS_WITH",
            "ENDS_WITH",
        ]
    ]
    """Comparison operator.

    String operators: includes, not_includes, starts_with, ends_with, regex.
    Existence: exists, is_null. Set membership: in, not_in (comma-separated values).
    Numeric: eq, neq, gt, gte, lt, lte.
    """

    type: Required[Literal["string", "number", "boolean"]]
    """Data type of the filter field.

    Must match the actual type of the key being filtered.
    """

    kind: Literal["filter"]
    """Discriminator for leaf filter nodes.

    Always 'filter' when present; may be omitted.
    """

    value: Union[str, float, bool]
    """Comparison value.

    Must match actual values in your data — verify with the values endpoint. Ensure
    the value type (string/number/boolean) matches the field type. String
    comparisons are case-sensitive. Regex uses RE2 syntax (no
    lookaheads/lookbehinds).
    """


Filter: TypeAlias = Union[FilterUnionMember0, FilterWorkersObservabilityFilterLeaf]
