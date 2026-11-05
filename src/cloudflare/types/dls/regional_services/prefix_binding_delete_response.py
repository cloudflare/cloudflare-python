# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["PrefixBindingDeleteResponse", "Message", "Error"]


class Message(BaseModel):
    code: int

    message: str

    error_chain: Optional[List[object]] = None
    """
    Optional upstream error context for APIv4 errors that wrap downstream service
    failures.
    """


class Error(BaseModel):
    code: int

    message: str

    error_chain: Optional[List[object]] = None
    """
    Optional upstream error context for APIv4 errors that wrap downstream service
    failures.
    """


class PrefixBindingDeleteResponse(BaseModel):
    messages: List[Message]

    success: bool

    errors: Optional[List[Error]] = None
