# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MessagePeekParams"]


class MessagePeekParams(TypedDict, total=False):
    account_id: Required[str]
    """A Resource identifier."""

    batch_size: float
    """The maximum number of messages to include in a batch."""
