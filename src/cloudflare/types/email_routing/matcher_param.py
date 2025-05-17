# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MatcherParam"]


class MatcherParam(TypedDict, total=False):
    type: Required[Literal["all", "literal"]]
    """Type of matcher."""

    field: Literal["to"]
    """Field for type matcher."""

    value: str
    """Value for matcher."""
