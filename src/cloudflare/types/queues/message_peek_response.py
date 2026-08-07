# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["MessagePeekResponse", "Message"]


class Message(BaseModel):
    id: Optional[str] = None

    attempts: Optional[float] = None

    body: Optional[str] = None

    metadata: Optional[object] = None

    ref: Optional[str] = None
    """An opaque reference to a peeked message.

    You must hold on to this value and use it to purge the message.
    """

    timestamp_ms: Optional[float] = None


class MessagePeekResponse(BaseModel):
    messages: Optional[List[Message]] = None
