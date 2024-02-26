# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AccountSettingUpdateResponse"]


class AccountSettingUpdateResponse(BaseModel):
    default_usage_model: Optional[object] = None

    green_compute: Optional[object] = None
