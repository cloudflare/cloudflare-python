# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional, List

from .live_stat import LiveStat

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

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
