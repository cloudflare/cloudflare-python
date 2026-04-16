# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["MessagePullResponse", "Message", "Metadata", "MetadataMetrics"]


class Message(BaseModel):
    id: Optional[str] = None

    attempts: Optional[float] = None

    body: Optional[str] = None

    lease_id: Optional[str] = None
    """An ID that represents an "in-flight" message that has been pulled from a Queue.

    You must hold on to this ID and use it to acknowledge this message.
    """

    metadata: Optional[object] = None

    timestamp_ms: Optional[float] = None


class MetadataMetrics(BaseModel):
    """Best-effort metrics for the queue.

    Values may be approximate due to the distributed nature of queues.
    """

    backlog_bytes: float
    """The size in bytes of unacknowledged messages in the queue."""

    backlog_count: float
    """The number of unacknowledged messages in the queue."""

    oldest_message_timestamp_ms: float
    """Unix timestamp in milliseconds of the oldest unacknowledged message in the
    queue.

    Returns 0 if unknown.
    """


class Metadata(BaseModel):
    metrics: Optional[MetadataMetrics] = None
    """Best-effort metrics for the queue.

    Values may be approximate due to the distributed nature of queues.
    """


class MessagePullResponse(BaseModel):
    message_backlog_count: Optional[float] = None
    """The number of unacknowledged messages in the queue."""

    messages: Optional[List[Message]] = None

    metadata: Optional[Metadata] = None
