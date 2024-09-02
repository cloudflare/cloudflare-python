# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict, Required

__all__ = ["MatcherParam"]


class MatcherParam(TypedDict, total=False):
    field: Required[Literal["to"]]
    """Field for type matcher."""

    type: Required[Literal["literal"]]
    """Type of matcher."""

    value: Required[str]
    """Value for matcher."""
