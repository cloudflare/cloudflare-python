# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["UsagePaygoInfoResponse", "Subscription"]


class Subscription(BaseModel):
    id: str
    """The identifier for the Cloudflare subscription."""

    billing_cycle_anchor_timestamp: datetime
    """The subscription billing cycle anchor timestamp."""

    start_timestamp: datetime
    """The subscription start timestamp."""

    end_timestamp: Optional[datetime] = None
    """The subscription end timestamp.

    Omitted for active subscriptions; present only when the subscription has been
    cancelled.
    """


class UsagePaygoInfoResponse(BaseModel):
    """Contains the paygo usage info."""

    covered: bool
    """Indicates whether the account is covered."""

    subscriptions: List[Subscription]
    """List of subscriptions for the account."""
