# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["DeviceMatch"]


class DeviceMatch(BaseModel):
    platform: Optional[Literal["windows", "mac", "linux", "android", "ios"]] = None
