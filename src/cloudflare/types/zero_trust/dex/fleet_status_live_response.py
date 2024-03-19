# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "FleetStatusLiveResponse",
    "DeviceStats",
    "DeviceStatsByColo",
    "DeviceStatsByMode",
    "DeviceStatsByPlatform",
    "DeviceStatsByStatus",
    "DeviceStatsByVersion",
]


class DeviceStatsByColo(BaseModel):
    unique_devices_total: Optional[float] = FieldInfo(alias="uniqueDevicesTotal", default=None)
    """Number of unique devices"""

    value: Optional[str] = None


class DeviceStatsByMode(BaseModel):
    unique_devices_total: Optional[float] = FieldInfo(alias="uniqueDevicesTotal", default=None)
    """Number of unique devices"""

    value: Optional[str] = None


class DeviceStatsByPlatform(BaseModel):
    unique_devices_total: Optional[float] = FieldInfo(alias="uniqueDevicesTotal", default=None)
    """Number of unique devices"""

    value: Optional[str] = None


class DeviceStatsByStatus(BaseModel):
    unique_devices_total: Optional[float] = FieldInfo(alias="uniqueDevicesTotal", default=None)
    """Number of unique devices"""

    value: Optional[str] = None


class DeviceStatsByVersion(BaseModel):
    unique_devices_total: Optional[float] = FieldInfo(alias="uniqueDevicesTotal", default=None)
    """Number of unique devices"""

    value: Optional[str] = None


class DeviceStats(BaseModel):
    by_colo: Optional[List[DeviceStatsByColo]] = FieldInfo(alias="byColo", default=None)

    by_mode: Optional[List[DeviceStatsByMode]] = FieldInfo(alias="byMode", default=None)

    by_platform: Optional[List[DeviceStatsByPlatform]] = FieldInfo(alias="byPlatform", default=None)

    by_status: Optional[List[DeviceStatsByStatus]] = FieldInfo(alias="byStatus", default=None)

    by_version: Optional[List[DeviceStatsByVersion]] = FieldInfo(alias="byVersion", default=None)

    unique_devices_total: Optional[float] = FieldInfo(alias="uniqueDevicesTotal", default=None)
    """Number of unique devices"""


class FleetStatusLiveResponse(BaseModel):
    device_stats: Optional[DeviceStats] = FieldInfo(alias="deviceStats", default=None)
