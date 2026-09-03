# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["AccessDevicePostureRule", "DevicePosture"]


class DevicePosture(BaseModel):
    integration_uid: str
    """The ID of a device posture integration."""

    account_id: Optional[str] = None
    """The ID of the account that owns the device posture integration."""


class AccessDevicePostureRule(BaseModel):
    """Enforces a device posture rule has run successfully"""

    device_posture: DevicePosture
