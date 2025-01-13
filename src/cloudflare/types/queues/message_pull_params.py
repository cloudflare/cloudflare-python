# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MessagePullParams"]


class MessagePullParams(TypedDict, total=False):
    account_id: Required[str]
    """A Resource identifier."""

    batch_size: float
    """The maximum number of messages to include in a batch."""

    visibility_timeout_ms: float
    """The number of milliseconds that a message is exclusively leased.

    After the timeout, the message becomes available for another attempt.
    """
