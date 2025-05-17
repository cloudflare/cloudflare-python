# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TelemetryKeysParams", "Filter", "KeyNeedle", "Needle", "Timeframe"]


class TelemetryKeysParams(TypedDict, total=False):
    account_id: Required[str]

    datasets: List[str]

    filters: Iterable[Filter]

    key_needle: Annotated[KeyNeedle, PropertyInfo(alias="keyNeedle")]
    """Search for a specific substring in the keys."""

    limit: float

    needle: Needle
    """Search for a specific substring in the event."""

    timeframe: Timeframe


class Filter(TypedDict, total=False):
    key: Required[str]

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

    value: Union[str, float, bool]


class KeyNeedle(TypedDict, total=False):
    value: Required[Union[str, float, bool]]

    is_regex: Annotated[bool, PropertyInfo(alias="isRegex")]

    match_case: Annotated[bool, PropertyInfo(alias="matchCase")]


class Needle(TypedDict, total=False):
    value: Required[Union[str, float, bool]]

    is_regex: Annotated[bool, PropertyInfo(alias="isRegex")]

    match_case: Annotated[bool, PropertyInfo(alias="matchCase")]


_TimeframeReservedKeywords = TypedDict(
    "_TimeframeReservedKeywords",
    {
        "from": float,
    },
    total=False,
)


class Timeframe(_TimeframeReservedKeywords, total=False):
    to: Required[float]
