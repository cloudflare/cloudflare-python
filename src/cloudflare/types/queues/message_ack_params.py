# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["MessageAckParams", "Ack", "Retry"]


class MessageAckParams(TypedDict, total=False):
    account_id: Required[str]
    """A Resource identifier."""

    acks: Iterable[Ack]

    retries: Iterable[Retry]


class Ack(TypedDict, total=False):
    lease_id: str
    """An ID that represents an "in-flight" message that has been pulled from a Queue.

    You must hold on to this ID and use it to acknowledge this message.
    """


class Retry(TypedDict, total=False):
    delay_seconds: float
    """
    The number of seconds to delay before making the message available for another
    attempt.
    """

    lease_id: str
    """An ID that represents an "in-flight" message that has been pulled from a Queue.

    You must hold on to this ID and use it to acknowledge this message.
    """
