# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["MessageAckParams", "Ack", "Retry"]


class MessageAckParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    acks: Iterable[Ack]

    retries: Iterable[Retry]


class Ack(TypedDict, total=False):
    lease_id: str
    """Lease ID for a message to acknowledge."""


class Retry(TypedDict, total=False):
    delay_seconds: float
    """
    The number of seconds to delay before making the message available for another
    attempt.
    """

    lease_id: str
    """Lease ID for a message to retry."""
