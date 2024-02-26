# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AccountSettingGetResponse"]


class AccountSettingGetResponse(BaseModel):
    default_usage_model: Optional[object] = None

    green_compute: Optional[object] = None
