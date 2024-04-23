# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .image import Image
from ..._models import BaseModel
from ..shared.response_info import ResponseInfo

__all__ = ["V1ListResponse", "Result"]


class Result(BaseModel):
    images: Optional[List[Image]] = None


class V1ListResponse(BaseModel):
    errors: List[ResponseInfo]

    messages: List[ResponseInfo]

    result: Result

    success: Literal[True]
    """Whether the API call was successful"""
