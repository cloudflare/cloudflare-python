# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["UniqueDevices"]


class UniqueDevices(BaseModel):
    unique_devices_total: int = FieldInfo(alias="uniqueDevicesTotal")
    """total number of unique devices"""
