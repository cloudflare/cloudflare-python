# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FilterListParams"]


class FilterListParams(TypedDict, total=False):
    description: str
    """A case-insensitive string to find in the description."""

    expression: str
    """A case-insensitive string to find in the expression."""

    page: float
    """Page number of paginated results."""

    paused: bool
    """When true, indicates that the filter is currently paused."""

    per_page: float
    """Number of filters per page."""

    ref: str
    """The filter ref (a short reference tag) to search for. Must be an exact match."""
