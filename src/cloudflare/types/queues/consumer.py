# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["Consumer", "MqWorkerConsumer", "MqWorkerConsumerSettings", "MqHTTPConsumer", "MqHTTPConsumerSettings"]


class MqWorkerConsumerSettings(BaseModel):
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


class MqWorkerConsumer(BaseModel):
    consumer_id: Optional[str] = None
    """A Resource identifier."""

    created_on: Optional[str] = None

    queue_id: Optional[str] = None
    """A Resource identifier."""

    script: Optional[str] = None
    """Name of a Worker"""

    settings: Optional[MqWorkerConsumerSettings] = None

    type: Optional[Literal["worker"]] = None


class MqHTTPConsumerSettings(BaseModel):
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


class MqHTTPConsumer(BaseModel):
    consumer_id: Optional[str] = None
    """A Resource identifier."""

    created_on: Optional[str] = None

    queue_id: Optional[str] = None
    """A Resource identifier."""

    settings: Optional[MqHTTPConsumerSettings] = None

    type: Optional[Literal["http_pull"]] = None


Consumer: TypeAlias = Union[MqWorkerConsumer, MqHTTPConsumer]
