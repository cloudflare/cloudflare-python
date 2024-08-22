# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["LiveStat"]


class LiveStat(BaseModel):
    unique_devices_total: Optional[float] = FieldInfo(alias="uniqueDevicesTotal", default=None)
    """Number of unique devices"""

    value: Optional[str] = None
