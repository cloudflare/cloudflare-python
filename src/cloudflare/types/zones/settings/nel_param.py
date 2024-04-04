# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["NELParam", "Value"]


class Value(TypedDict, total=False):
    enabled: bool


class NELParam(TypedDict, total=False):
    id: Required[Literal["nel"]]
    """Zone setting identifier."""

    value: Required[Value]
    """Current value of the zone setting."""
