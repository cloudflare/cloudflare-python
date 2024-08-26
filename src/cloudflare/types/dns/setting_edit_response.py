# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from .dns_setting import DNSSetting

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["SettingEditResponse"]

class SettingEditResponse(BaseModel):
    zone_defaults: Optional[DNSSetting] = None