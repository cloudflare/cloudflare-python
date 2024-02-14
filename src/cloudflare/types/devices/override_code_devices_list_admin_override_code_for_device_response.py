# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OverrideCodeDevicesListAdminOverrideCodeForDeviceResponse", "DisableForTime"]


class DisableForTime(BaseModel):
    _1: Optional[object] = FieldInfo(alias="1", default=None)
    """Override code that is valid for 1 hour."""

    _12: Optional[object] = FieldInfo(alias="12", default=None)
    """Override code that is valid for 12 hour2."""

    _24: Optional[object] = FieldInfo(alias="24", default=None)
    """Override code that is valid for 24 hour.2."""

    _3: Optional[object] = FieldInfo(alias="3", default=None)
    """Override code that is valid for 3 hours."""

    _6: Optional[object] = FieldInfo(alias="6", default=None)
    """Override code that is valid for 6 hours."""


class OverrideCodeDevicesListAdminOverrideCodeForDeviceResponse(BaseModel):
    disable_for_time: Optional[DisableForTime] = None
