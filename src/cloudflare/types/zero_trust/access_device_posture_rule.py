# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["AccessDevicePostureRule", "DevicePosture"]


class DevicePosture(BaseModel):
    integration_uid: str
    """The ID of a device posture integration."""


class AccessDevicePostureRule(BaseModel):
    device_posture: DevicePosture
