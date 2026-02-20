# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "Queue",
    "Consumer",
    "ConsumerMqWorkerConsumerResponse",
    "ConsumerMqWorkerConsumerResponseSettings",
    "ConsumerMqHTTPConsumerResponse",
    "ConsumerMqHTTPConsumerResponseSettings",
    "Producer",
    "ProducerMqWorkerProducer",
    "ProducerMqR2Producer",
    "Settings",
]


class ConsumerMqWorkerConsumerResponseSettings(BaseModel):
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


class ConsumerMqWorkerConsumerResponse(BaseModel):
    consumer_id: Optional[str] = None
    """A Resource identifier."""

    created_on: Optional[datetime] = None

    dead_letter_queue: Optional[str] = None
    """Name of the dead letter queue, or empty string if not configured"""

    queue_name: Optional[str] = None

    script_name: Optional[str] = None
    """Name of a Worker"""

    settings: Optional[ConsumerMqWorkerConsumerResponseSettings] = None

    type: Optional[Literal["worker"]] = None


class ConsumerMqHTTPConsumerResponseSettings(BaseModel):
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


class ConsumerMqHTTPConsumerResponse(BaseModel):
    consumer_id: Optional[str] = None
    """A Resource identifier."""

    created_on: Optional[datetime] = None

    dead_letter_queue: Optional[str] = None
    """Name of the dead letter queue, or empty string if not configured"""

    queue_name: Optional[str] = None

    settings: Optional[ConsumerMqHTTPConsumerResponseSettings] = None

    type: Optional[Literal["http_pull"]] = None


Consumer: TypeAlias = Annotated[
    Union[ConsumerMqWorkerConsumerResponse, ConsumerMqHTTPConsumerResponse], PropertyInfo(discriminator="type")
]


class ProducerMqWorkerProducer(BaseModel):
    script: Optional[str] = None

    type: Optional[Literal["worker"]] = None


class ProducerMqR2Producer(BaseModel):
    bucket_name: Optional[str] = None

    type: Optional[Literal["r2_bucket"]] = None


Producer: TypeAlias = Union[ProducerMqWorkerProducer, ProducerMqR2Producer]


class Settings(BaseModel):
    delivery_delay: Optional[float] = None
    """Number of seconds to delay delivery of all messages to consumers."""

    delivery_paused: Optional[bool] = None
    """Indicates if message delivery to consumers is currently paused."""

    message_retention_period: Optional[float] = None
    """Number of seconds after which an unconsumed message will be delayed."""


class Queue(BaseModel):
    consumers: Optional[List[Consumer]] = None

    consumers_total_count: Optional[float] = None

    created_on: Optional[str] = None

    modified_on: Optional[str] = None

    producers: Optional[List[Producer]] = None

    producers_total_count: Optional[float] = None

    queue_id: Optional[str] = None

    queue_name: Optional[str] = None

    settings: Optional[Settings] = None
