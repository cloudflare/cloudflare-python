# File generated from our OpenAPI spec by Stainless.

from .api_shield_messages import APIShieldMessages

from typing import Union, Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["APIShieldAPIResponseSingle"]


class APIShieldAPIResponseSingle(BaseModel):
    errors: APIShieldMessages

    messages: APIShieldMessages

    result: Union[Optional[object], Optional[str]]

    success: bool
    """Whether the API call was successful"""
