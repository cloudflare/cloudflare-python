# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SilenceDeleteResponse", "Error", "Message"]


class Error(BaseModel):
    message: str

    code: Optional[int] = None


class Message(BaseModel):
    message: str

    code: Optional[int] = None


class SilenceDeleteResponse(BaseModel):
    errors: List[Error]

    messages: List[Message]

    success: Literal[True]
    """Whether the API call was successful"""
