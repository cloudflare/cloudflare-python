# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["DeviceListResponse", "Device"]


class Device(BaseModel):
    device_id: Optional[str] = FieldInfo(alias="deviceId", default=None)
    """Device identifier (UUID v4)"""

    device_name: Optional[str] = FieldInfo(alias="deviceName", default=None)
    """Device identifier (human readable)"""

    eligible: Optional[bool] = None
    """Whether the device is eligible for remote captures"""

    ineligible_reason: Optional[str] = FieldInfo(alias="ineligibleReason", default=None)
    """If the device is not eligible, the reason why."""

    person_email: Optional[str] = FieldInfo(alias="personEmail", default=None)
    """User contact email address"""

    platform: Optional[str] = None
    """Operating system"""

    status: Optional[str] = None
    """Network status"""

    timestamp: Optional[str] = None
    """Timestamp in ISO format"""

    version: Optional[str] = None
    """WARP client version"""


class DeviceListResponse(BaseModel):
    devices: Optional[List[Device]] = None
    """List of eligible devices"""
