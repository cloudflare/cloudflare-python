# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["TelemetryKeysParams", "Filter", "KeyNeedle", "Needle"]


class TelemetryKeysParams(TypedDict, total=False):
    account_id: Required[str]

    datasets: SequenceNotStr[str]

    filters: Iterable[Filter]

    from_: Annotated[float, PropertyInfo(alias="from")]

    key_needle: Annotated[KeyNeedle, PropertyInfo(alias="keyNeedle")]
    """Search for a specific substring in the keys."""

    limit: float

    needle: Needle
    """Search for a specific substring in any of the events"""

    to: float


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
    """Search for a specific substring in the keys."""

    value: Required[Union[str, float, bool]]

    is_regex: Annotated[bool, PropertyInfo(alias="isRegex")]

    match_case: Annotated[bool, PropertyInfo(alias="matchCase")]


class Needle(TypedDict, total=False):
    """Search for a specific substring in any of the events"""

    value: Required[Union[str, float, bool]]

    is_regex: Annotated[bool, PropertyInfo(alias="isRegex")]

    match_case: Annotated[bool, PropertyInfo(alias="matchCase")]
