# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RouteUpdateParams"]


class RouteUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    pattern: Required[str]
    """Pattern to match incoming requests against.

    [Learn more](https://developers.cloudflare.com/workers/configuration/routing/routes/#matching-behavior).
    """

    script: str
    """Name of the script to run if the route matches."""
