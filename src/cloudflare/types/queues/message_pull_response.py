# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MessagePullResponse"]


class MessagePullResponse(BaseModel):
    id: Optional[str] = None

    attempts: Optional[float] = None

    body: Optional[str] = None

    lease_id: Optional[str] = None
    """An ID that represents an "in-flight" message that has been pulled from a Queue.

    You must hold on to this ID and use it to acknowledge this message.
    """

    metadata: Optional[object] = None

    timestamp_ms: Optional[float] = None
