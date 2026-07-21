# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["TokenDeleteResponse", "Error", "Message"]


class Error(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None


class Message(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None


class TokenDeleteResponse(BaseModel):
    errors: List[Error]

    messages: List[Message]

    success: bool
