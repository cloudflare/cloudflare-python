# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .dns_setting import DNSSetting

__all__ = ["SettingGetResponse"]


class SettingGetResponse(BaseModel):
    zone_defaults: Optional[DNSSetting] = None
