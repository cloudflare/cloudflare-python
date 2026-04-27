# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = [
    "TelemetryKeysParams",
    "Filter",
    "FilterUnionMember0",
    "FilterUnionMember0Filter",
    "FilterUnionMember0FilterUnionMember0",
    "FilterUnionMember0FilterWorkersObservabilityFilterLeaf",
    "FilterWorkersObservabilityFilterLeaf",
    "KeyNeedle",
    "Needle",
]


class TelemetryKeysParams(TypedDict, total=False):
    account_id: Required[str]

    datasets: SequenceNotStr[str]
    """Leave this empty to use the default datasets"""

    filters: Iterable[Filter]
    """Apply filters to narrow key discovery.

    Supports nested groups via kind: 'group'. Maximum nesting depth is 4.
    """

    from_: Annotated[float, PropertyInfo(alias="from")]

    key_needle: Annotated[KeyNeedle, PropertyInfo(alias="keyNeedle")]
    """If the user suggests a key, use this to narrow down the list of keys returned.

    Make sure matchCase is false to avoid case sensitivity issues.
    """

    limit: float
    """
    Advanced usage: set limit=1000+ to retrieve comprehensive key options without
    needing additional filtering.
    """

    needle: Needle
    """Search for a specific substring in any of the events"""

    to: float


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
        ]
    ]
    """Comparison operator.

    String operators: includes, not_includes, starts_with, regex. Existence: exists,
    is_null. Set membership: in, not_in (comma-separated values). Numeric: eq, neq,
    gt, gte, lt, lte.
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
        ]
    ]
    """Comparison operator.

    String operators: includes, not_includes, starts_with, regex. Existence: exists,
    is_null. Set membership: in, not_in (comma-separated values). Numeric: eq, neq,
    gt, gte, lt, lte.
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


class KeyNeedle(TypedDict, total=False):
    """If the user suggests a key, use this to narrow down the list of keys returned.

    Make sure matchCase is false to avoid case sensitivity issues.
    """

    value: Required[Union[str, float, bool]]
    """The text or pattern to search for."""

    is_regex: Annotated[bool, PropertyInfo(alias="isRegex")]
    """When true, treats the value as a regular expression (RE2 syntax)."""

    match_case: Annotated[bool, PropertyInfo(alias="matchCase")]
    """When true, performs a case-sensitive search. Defaults to case-insensitive."""


class Needle(TypedDict, total=False):
    """Search for a specific substring in any of the events"""

    value: Required[Union[str, float, bool]]
    """The text or pattern to search for."""

    is_regex: Annotated[bool, PropertyInfo(alias="isRegex")]
    """When true, treats the value as a regular expression (RE2 syntax)."""

    match_case: Annotated[bool, PropertyInfo(alias="matchCase")]
    """When true, performs a case-sensitive search. Defaults to case-insensitive."""
