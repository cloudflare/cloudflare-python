# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SettingGetResponse"]


class SettingGetResponse(BaseModel):
    enabled: Optional[bool] = None
    """Indicates whether zone-level authenticated origin pulls is enabled."""
