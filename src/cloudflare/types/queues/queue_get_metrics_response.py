# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["QueueGetMetricsResponse"]


class QueueGetMetricsResponse(BaseModel):
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
