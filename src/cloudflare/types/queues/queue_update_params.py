# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["QueueUpdateParams", "Settings"]


class QueueUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """A Resource identifier."""

    queue_name: str

    settings: Settings


class Settings(TypedDict, total=False):
    delivery_delay: float
    """Number of seconds to delay delivery of all messages to consumers."""

    message_retention_period: float
    """Number of seconds after which an unconsumed message will be delayed."""
