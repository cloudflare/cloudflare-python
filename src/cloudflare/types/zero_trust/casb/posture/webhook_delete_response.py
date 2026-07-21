# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["WebhookDeleteResponse", "Error", "ErrorSource", "Message", "MessageSource"]


class ErrorSource(BaseModel):
    pointer: Optional[str] = None
    """JSON pointer to the source of the error."""


class Error(BaseModel):
    code: int
    """Error or message code."""

    message: str
    """Human-readable message."""

    documentation_url: Optional[str] = None
    """Link to relevant documentation."""

    source: Optional[ErrorSource] = None


class MessageSource(BaseModel):
    pointer: Optional[str] = None
    """JSON pointer to the source of the error."""


class Message(BaseModel):
    code: int
    """Error or message code."""

    message: str
    """Human-readable message."""

    documentation_url: Optional[str] = None
    """Link to relevant documentation."""

    source: Optional[MessageSource] = None


class WebhookDeleteResponse(BaseModel):
    """Common response structure for all API endpoints."""

    errors: List[Error]

    messages: List[Message]

    success: bool
    """Whether the API call was successful."""
