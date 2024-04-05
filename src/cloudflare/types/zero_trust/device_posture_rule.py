# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["DevicePostureRule", "DevicePosture"]


class DevicePosture(BaseModel):
    integration_uid: str
    """The ID of a device posture integration."""


class DevicePostureRule(BaseModel):
    device_posture: DevicePosture
