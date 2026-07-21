# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RobotGetParams"]


class RobotGetParams(TypedDict, total=False):
    zone_id: Required[str]

    subdomain: str
    """Optional subdomain to fetch robots.txt for.

    If omitted, fetches robots.txt for the zone apex domain.
    """
