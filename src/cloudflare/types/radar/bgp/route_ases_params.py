# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RouteAsesParams"]


class RouteAsesParams(TypedDict, total=False):
    format: Literal["JSON", "CSV"]
    """Format results are returned in."""

    limit: int
    """Limit the number of objects in the response."""

    location: str
    """Location Alpha2 code."""

    sort_by: Annotated[
        Literal["cone", "pfxs", "ipv4", "ipv6", "rpki_valid", "rpki_invalid", "rpki_unknown"],
        PropertyInfo(alias="sortBy"),
    ]
    """Return order results by given type"""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Sort by value ascending or descending"""
