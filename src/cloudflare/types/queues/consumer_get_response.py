# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "ConsumerGetResponse",
    "MqWorkerConsumerResponse",
    "MqWorkerConsumerResponseSettings",
    "MqHTTPConsumerResponse",
    "MqHTTPConsumerResponseSettings",
]


class MqWorkerConsumerResponseSettings(BaseModel):
    batch_size: Optional[float] = None
    """The maximum number of messages to include in a batch."""

    max_concurrency: Optional[float] = None
    """Maximum number of concurrent consumers that may consume from this Queue.

    Set to `null` to automatically opt in to the platform's maximum (recommended).
    """

    max_retries: Optional[float] = None
    """The maximum number of retries"""

    max_wait_time_ms: Optional[float] = None
    """
    The number of milliseconds to wait for a batch to fill up before attempting to
    deliver it
    """

    retry_delay: Optional[float] = None
    """
    The number of seconds to delay before making the message available for another
    attempt.
    """


class MqWorkerConsumerResponse(BaseModel):
    consumer_id: Optional[str] = None
    """A Resource identifier."""

    created_on: Optional[datetime] = None

    dead_letter_queue: Optional[str] = None
    """Name of the dead letter queue, or empty string if not configured"""

    queue_name: Optional[str] = None

    script_name: Optional[str] = None
    """Name of a Worker"""

    settings: Optional[MqWorkerConsumerResponseSettings] = None

    type: Optional[Literal["worker"]] = None


class MqHTTPConsumerResponseSettings(BaseModel):
    batch_size: Optional[float] = None
    """The maximum number of messages to include in a batch."""

    max_retries: Optional[float] = None
    """The maximum number of retries"""

    retry_delay: Optional[float] = None
    """
    The number of seconds to delay before making the message available for another
    attempt.
    """

    visibility_timeout_ms: Optional[float] = None
    """The number of milliseconds that a message is exclusively leased.

    After the timeout, the message becomes available for another attempt.
    """


class MqHTTPConsumerResponse(BaseModel):
    consumer_id: Optional[str] = None
    """A Resource identifier."""

    created_on: Optional[datetime] = None

    dead_letter_queue: Optional[str] = None
    """Name of the dead letter queue, or empty string if not configured"""

    queue_name: Optional[str] = None

    settings: Optional[MqHTTPConsumerResponseSettings] = None

    type: Optional[Literal["http_pull"]] = None


ConsumerGetResponse: TypeAlias = Annotated[
    Union[MqWorkerConsumerResponse, MqHTTPConsumerResponse], PropertyInfo(discriminator="type")
]
