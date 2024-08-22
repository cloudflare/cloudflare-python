# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .live_stat import LiveStat
from ...._models import BaseModel

__all__ = ["FleetStatusLiveResponse", "DeviceStats"]


class DeviceStats(BaseModel):
    by_colo: Optional[List[LiveStat]] = FieldInfo(alias="byColo", default=None)

    by_mode: Optional[List[LiveStat]] = FieldInfo(alias="byMode", default=None)

    by_platform: Optional[List[LiveStat]] = FieldInfo(alias="byPlatform", default=None)

    by_status: Optional[List[LiveStat]] = FieldInfo(alias="byStatus", default=None)

    by_version: Optional[List[LiveStat]] = FieldInfo(alias="byVersion", default=None)

    unique_devices_total: Optional[float] = FieldInfo(alias="uniqueDevicesTotal", default=None)
    """Number of unique devices"""


class FleetStatusLiveResponse(BaseModel):
    device_stats: Optional[DeviceStats] = FieldInfo(alias="deviceStats", default=None)
