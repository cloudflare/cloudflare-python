# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SubscriptionUpdateParams", "Destination"]


class SubscriptionUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """A Resource identifier."""

    destination: Destination
    """Destination configuration for the subscription"""

    enabled: bool
    """Whether the subscription is active"""

    events: List[str]
    """List of event types this subscription handles"""

    name: str
    """Name of the subscription"""


class Destination(TypedDict, total=False):
    queue_id: Required[str]
    """ID of the target queue"""

    type: Required[Literal["queues.queue"]]
    """Type of destination"""
