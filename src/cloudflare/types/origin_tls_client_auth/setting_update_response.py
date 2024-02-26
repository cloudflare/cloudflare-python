# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SettingUpdateResponse"]


class SettingUpdateResponse(BaseModel):
    enabled: Optional[bool] = None
    """Indicates whether zone-level authenticated origin pulls is enabled."""
