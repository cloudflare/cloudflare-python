# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["RobotBulkGetParams"]


class RobotBulkGetParams(TypedDict, total=False):
    zone_id: Required[str]

    body: Required[SequenceNotStr[str]]
    """Array of domain hostnames to fetch robots.txt for.

    Each domain must end with the zone name. Maximum 25 domains per request.
    """
