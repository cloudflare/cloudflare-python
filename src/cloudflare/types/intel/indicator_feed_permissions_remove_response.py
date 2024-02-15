# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["IndicatorFeedPermissionsRemoveResponse"]


class IndicatorFeedPermissionsRemoveResponse(BaseModel):
    success: Optional[bool] = None
    """Whether the update succeeded or not"""
