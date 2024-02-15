# File generated from our OpenAPI spec by Stainless.

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["UniqueDeviceListResponse"]


class UniqueDeviceListResponse(BaseModel):
    unique_devices_total: int = FieldInfo(alias="uniqueDevicesTotal")
    """total number of unique devices"""
