# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DeviceListParams"]


class DeviceListParams(TypedDict, total=False):
    account_id: Required[str]

    page: Required[float]
    """Page number of paginated results"""

    per_page: Required[float]
    """Number of items per page"""

    time_end: Required[str]
    """Timestamp in ISO format"""

    time_start: Required[str]
    """Timestamp in ISO format"""

    colo: str
    """Cloudflare colo"""

    device_id: str
    """Device-specific ID, given as UUID v4"""

    mode: str
    """The mode under which the WARP client is run"""

    platform: str
    """Operating system"""

    sort_by: Literal["colo", "device_id", "mode", "platform", "status", "timestamp", "version"]
    """Dimension to sort results by"""

    status: str
    """Network status"""

    version: str
    """WARP client version"""
