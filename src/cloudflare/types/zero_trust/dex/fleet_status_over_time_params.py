# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FleetStatusOverTimeParams"]


class FleetStatusOverTimeParams(TypedDict, total=False):
    account_id: Required[str]

    time_end: Required[str]
    """Timestamp in ISO format"""

    time_start: Required[str]
    """Timestamp in ISO format"""

    colo: str
    """Cloudflare colo"""

    device_id: str
    """Device-specific ID, given as UUID v4"""
