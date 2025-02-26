# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RouteStatsParams"]


class RouteStatsParams(TypedDict, total=False):
    asn: int
    """Single Autonomous System Number (ASN) as integer."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    location: str
    """Location alpha-2 code."""
