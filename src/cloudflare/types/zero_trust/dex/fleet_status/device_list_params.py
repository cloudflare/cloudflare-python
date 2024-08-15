# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["DeviceListParams"]


class DeviceListParams(TypedDict, total=False):
    account_id: Required[str]

    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Time range beginning in ISO format"""

    page: Required[float]
    """Page number"""

    per_page: Required[float]
    """Number of results per page"""

    to: Required[str]
    """Time range end in ISO format"""

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

    source: Literal["last_seen", "hourly", "raw"]
    """Source:

    - `hourly` - device details aggregated hourly, up to 7 days prior
    - `last_seen` - device details, up to 24 hours prior
    - `raw` - device details, up to 7 days prior
    """

    status: str
    """Network status"""

    version: str
    """WARP client version"""
