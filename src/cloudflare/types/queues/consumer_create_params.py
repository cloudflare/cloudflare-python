# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ConsumerCreateParams",
    "MqWorkerConsumer",
    "MqWorkerConsumerSettings",
    "MqHTTPConsumer",
    "MqHTTPConsumerSettings",
]


class MqWorkerConsumer(TypedDict, total=False):
    account_id: Required[str]
    """A Resource identifier."""

    dead_letter_queue: str

    script_name: str
    """Name of a Worker"""

    settings: MqWorkerConsumerSettings

    type: Literal["worker"]


class MqWorkerConsumerSettings(TypedDict, total=False):
    batch_size: float
    """The maximum number of messages to include in a batch."""

    max_concurrency: float
    """Maximum number of concurrent consumers that may consume from this Queue.

    Set to `null` to automatically opt in to the platform's maximum (recommended).
    """

    max_retries: float
    """The maximum number of retries"""

    max_wait_time_ms: float
    """
    The number of milliseconds to wait for a batch to fill up before attempting to
    deliver it
    """

    retry_delay: float
    """
    The number of seconds to delay before making the message available for another
    attempt.
    """


class MqHTTPConsumer(TypedDict, total=False):
    account_id: Required[str]
    """A Resource identifier."""

    dead_letter_queue: str

    settings: MqHTTPConsumerSettings

    type: Literal["http_pull"]


class MqHTTPConsumerSettings(TypedDict, total=False):
    batch_size: float
    """The maximum number of messages to include in a batch."""

    max_retries: float
    """The maximum number of retries"""

    retry_delay: float
    """
    The number of seconds to delay before making the message available for another
    attempt.
    """

    visibility_timeout_ms: float
    """The number of milliseconds that a message is exclusively leased.

    After the timeout, the message becomes available for another attempt.
    """


ConsumerCreateParams: TypeAlias = Union[MqWorkerConsumer, MqHTTPConsumer]
