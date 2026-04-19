# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PurgeStartParams"]


class PurgeStartParams(TypedDict, total=False):
    account_id: str
    """A Resource identifier."""

    delete_messages_permanently: bool
    """Confimation that all messages will be deleted permanently."""
