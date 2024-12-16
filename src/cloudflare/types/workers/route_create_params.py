# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RouteCreateParams"]


class RouteCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    pattern: Required[str]

    script: str
    """Name of the script, used in URLs and route configuration."""
