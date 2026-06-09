# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RegionalHostnameDeleteResponse", "Error", "ErrorSource", "Message", "MessageSource"]


class ErrorSource(BaseModel):
    pointer: Optional[str] = None


class Error(BaseModel):
    code: int

    message: str

    documentation_url: Optional[str] = None

    source: Optional[ErrorSource] = None


class MessageSource(BaseModel):
    pointer: Optional[str] = None


class Message(BaseModel):
    code: int

    message: str

    documentation_url: Optional[str] = None

    source: Optional[MessageSource] = None


class RegionalHostnameDeleteResponse(BaseModel):
    errors: List[Error]

    messages: List[Message]

    success: Literal[True]
    """Whether the API call was successful."""
