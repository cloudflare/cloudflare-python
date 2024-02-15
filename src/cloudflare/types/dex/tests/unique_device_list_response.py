# File generated from our OpenAPI spec by Stainless.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["UniqueDeviceListResponse"]


class UniqueDeviceListResponse(BaseModel):
    unique_devices_total: int = FieldInfo(alias="uniqueDevicesTotal")
    """total number of unique devices"""
