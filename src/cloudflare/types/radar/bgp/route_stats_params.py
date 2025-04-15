# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RouteStatsParams"]


class RouteStatsParams(TypedDict, total=False):
    asn: int
    """Filters results by Autonomous System.

    Specify a single Autonomous System Number (ASN) as integer.
    """

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    location: str
    """Filters results by location. Specify an alpha-2 location code."""
