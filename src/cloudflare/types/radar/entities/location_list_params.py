# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["LocationListParams"]


class LocationListParams(TypedDict, total=False):
    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    limit: int
    """Limits the number of objects returned in the response."""

    location: str
    """Filters results by location.

    Specify a comma-separated list of alpha-2 location codes.
    """

    offset: int
    """Skips the specified number of objects before fetching the results."""
