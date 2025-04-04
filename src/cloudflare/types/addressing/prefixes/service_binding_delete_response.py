# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ServiceBindingDeleteResponse", "Error", "Message"]


class Error(BaseModel):
    code: int

    message: str


class Message(BaseModel):
    code: int

    message: str


class ServiceBindingDeleteResponse(BaseModel):
    errors: List[Error]

    messages: List[Message]

    success: Literal[True]
    """Whether the API call was successful"""
