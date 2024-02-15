# File generated from our OpenAPI spec by Stainless.

from typing import Union, Optional

from ..._models import BaseModel
from .api_shield_messages import APIShieldMessages

__all__ = ["APIShieldAPIResponseSingle"]


class APIShieldAPIResponseSingle(BaseModel):
    errors: APIShieldMessages

    messages: APIShieldMessages

    result: Union[Optional[object], Optional[str]]

    success: bool
    """Whether the API call was successful"""
