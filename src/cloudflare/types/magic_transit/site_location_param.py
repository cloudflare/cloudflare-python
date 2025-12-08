# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SiteLocationParam"]


class SiteLocationParam(TypedDict, total=False):
    """Location of site in latitude and longitude."""

    lat: str
    """Latitude"""

    lon: str
    """Longitude"""
