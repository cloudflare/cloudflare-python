# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .rate_plan import RatePlan

__all__ = ["Subscription"]


class Subscription(BaseModel):
    id: Optional[str] = None
    """Subscription identifier tag."""

    currency: Optional[str] = None
    """The monetary unit in which pricing information is displayed."""

    current_period_end: Optional[datetime] = None
    """The end of the current period and also when the next billing is due."""

    current_period_start: Optional[datetime] = None
    """When the current billing period started.

    May match initial_period_start if this is the first period.
    """

    frequency: Optional[Literal["weekly", "monthly", "quarterly", "yearly"]] = None
    """How often the subscription is renewed automatically."""

    price: Optional[float] = None
    """The price of the subscription that will be billed, in US dollars."""

    rate_plan: Optional[RatePlan] = None
    """The rate plan applied to the subscription."""

    state: Optional[Literal["Trial", "Provisioned", "Paid", "AwaitingPayment", "Cancelled", "Failed", "Expired"]] = None
    """The state that the subscription is in."""
