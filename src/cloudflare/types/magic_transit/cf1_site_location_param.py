# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["Cf1SiteLocationParam"]


class Cf1SiteLocationParam(TypedDict, total=False):
    lat: float
    """Latitude of the CF1 Site."""

    long: float
    """Longitude of the CF1 Site."""

    name: str
    """Name of nearest town, city, or village."""
