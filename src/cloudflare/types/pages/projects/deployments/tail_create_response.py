# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["TailCreateResponse"]


class TailCreateResponse(BaseModel):
    """A tail session for streaming logs from a Pages deployment."""

    id: str
    """Identifier of the tail session."""

    url: Optional[str] = None
    """
    Optional WebSocket URL to connect to for receiving tail events, when returned by
    the tail service.
    """
