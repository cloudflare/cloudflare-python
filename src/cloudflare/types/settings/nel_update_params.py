# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["NELUpdateParams", "Value", "ValueValue"]


class NELUpdateParams(TypedDict, total=False):
    value: Required[Value]
    """Enable Network Error Logging reporting on your zone. (Beta)"""


class ValueValue(TypedDict, total=False):
    enabled: bool


class Value(TypedDict, total=False):
    id: Required[Literal["nel"]]
    """Zone setting identifier."""

    value: Required[ValueValue]
    """Current value of the zone setting."""
