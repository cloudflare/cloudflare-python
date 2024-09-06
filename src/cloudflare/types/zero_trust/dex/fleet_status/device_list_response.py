# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["DeviceListResponse"]


class DeviceListResponse(BaseModel):
    colo: str
    """Cloudflare colo"""

    device_id: str = FieldInfo(alias="deviceId")
    """Device identifier (UUID v4)"""

    platform: str
    """Operating system"""

    status: str
    """Network status"""

    version: str
    """WARP client version"""

    device_name: Optional[str] = FieldInfo(alias="deviceName", default=None)
    """Device identifier (human readable)"""

    person_email: Optional[str] = FieldInfo(alias="personEmail", default=None)
    """User contact email address"""
