# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RouteStatsParams"]


class RouteStatsParams(TypedDict, total=False):
    asn: int
    """Single ASN as integer."""

    format: Literal["JSON", "CSV"]
    """Format results are returned in."""

    location: str
    """Location Alpha2 code."""
