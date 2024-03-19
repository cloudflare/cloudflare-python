# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .images_image import ImagesImage

__all__ = ["V1ListResponse", "Error", "Message", "Result"]


class Error(BaseModel):
    code: int

    message: str


class Message(BaseModel):
    code: int

    message: str


class Result(BaseModel):
    images: Optional[List[ImagesImage]] = None


class V1ListResponse(BaseModel):
    errors: List[Error]

    messages: List[Message]

    result: Result

    success: Literal[True]
    """Whether the API call was successful"""
