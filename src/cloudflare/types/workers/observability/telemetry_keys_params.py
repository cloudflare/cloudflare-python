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
    "FilterWorkersObservabilityFilterLeaf",
    "KeyNeedle",
    "Needle",
]


class TelemetryKeysParams(TypedDict, total=False):
    account_id: str

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


class FilterUnionMember0(TypedDict, total=False):
    filter_combination: Required[Annotated[Literal["and", "or", "AND", "OR"], PropertyInfo(alias="filterCombination")]]

    filters: Required[Iterable[object]]

    kind: Required[Literal["group"]]


class FilterWorkersObservabilityFilterLeaf(TypedDict, total=False):
    """
    Filtering best practices: use observability_keys and observability_values to confirm available fields and values. If searching for errors, filter for $metadata.error exists.
    """

    key: Required[str]
    """Filter field name.

    IMPORTANT: do not guess keys. Always use verified keys from previous query
    results or the observability_keys response. Preferred keys: $metadata.service,
    $metadata.origin, $metadata.trigger, $metadata.message, $metadata.error.
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

    type: Required[Literal["string", "number", "boolean"]]

    kind: Literal["filter"]

    value: Union[str, float, bool]
    """Filter comparison value.

    IMPORTANT: must match actual values in your logs. Verify using previous query
    results or the /values endpoint. Ensure value type matches the field type.
    String comparisons are case-sensitive unless using specific operations. Regex
    uses ClickHouse RE2 syntax (no lookaheads/lookbehinds); examples: ^5\\dd{2}$ for
    HTTP 5xx, \bERROR\b for word boundary.
    """


Filter: TypeAlias = Union[FilterUnionMember0, FilterWorkersObservabilityFilterLeaf]


class KeyNeedle(TypedDict, total=False):
    """If the user suggests a key, use this to narrow down the list of keys returned.

    Make sure matchCase is false to avoid case sensitivity issues.
    """

    value: Required[Union[str, float, bool]]

    is_regex: Annotated[bool, PropertyInfo(alias="isRegex")]

    match_case: Annotated[bool, PropertyInfo(alias="matchCase")]


class Needle(TypedDict, total=False):
    """Search for a specific substring in any of the events"""

    value: Required[Union[str, float, bool]]

    is_regex: Annotated[bool, PropertyInfo(alias="isRegex")]

    match_case: Annotated[bool, PropertyInfo(alias="matchCase")]
