# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["FleetStatusOverTimeResponse", "DeviceStats", "DeviceStatsByMode", "DeviceStatsByStatus"]


class DeviceStatsByMode(BaseModel):
    timestamp: Optional[str] = None
    """Timestamp in ISO format"""

    unique_devices_total: Optional[float] = FieldInfo(alias="uniqueDevicesTotal", default=None)
    """Number of unique devices"""

    value: Optional[str] = None


class DeviceStatsByStatus(BaseModel):
    timestamp: Optional[str] = None
    """Timestamp in ISO format"""

    unique_devices_total: Optional[float] = FieldInfo(alias="uniqueDevicesTotal", default=None)
    """Number of unique devices"""

    value: Optional[str] = None


class DeviceStats(BaseModel):
    by_mode: Optional[List[DeviceStatsByMode]] = FieldInfo(alias="byMode", default=None)

    by_status: Optional[List[DeviceStatsByStatus]] = FieldInfo(alias="byStatus", default=None)

    unique_devices_total: Optional[float] = FieldInfo(alias="uniqueDevicesTotal", default=None)
    """Number of unique devices"""


class FleetStatusOverTimeResponse(BaseModel):
    device_stats: Optional[DeviceStats] = FieldInfo(alias="deviceStats", default=None)
