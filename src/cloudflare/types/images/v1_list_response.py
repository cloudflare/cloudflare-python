# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .image import Image
from ..._models import BaseModel

__all__ = ["V1ListResponse", "Error", "Message", "Result"]


class Error(BaseModel):
    code: int

    message: str


class Message(BaseModel):
    code: int

    message: str


class Result(BaseModel):
    images: Optional[List[Image]] = None


class V1ListResponse(BaseModel):
    errors: List[Error]

    messages: List[Message]

    result: Result

    success: Literal[True]
    """Whether the API call was successful"""
