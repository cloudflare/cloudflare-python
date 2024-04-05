# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SiteLocationParam"]


class SiteLocationParam(TypedDict, total=False):
    lat: str
    """Latitude"""

    lon: str
    """Longitude"""
