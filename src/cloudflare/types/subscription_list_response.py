# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "SubscriptionListResponse",
    "SubscriptionListResponseItem",
    "SubscriptionListResponseItemApp",
    "SubscriptionListResponseItemComponentValue",
    "SubscriptionListResponseItemRatePlan",
    "SubscriptionListResponseItemZone",
]


class SubscriptionListResponseItemApp(BaseModel):
    install_id: Optional[str] = None
    """app install id."""


class SubscriptionListResponseItemComponentValue(BaseModel):
    default: Optional[float] = None
    """The default amount assigned."""

    name: Optional[str] = None
    """The name of the component value."""

    price: Optional[float] = None
    """The unit price for the component value."""

    value: Optional[float] = None
    """The amount of the component value assigned."""


class SubscriptionListResponseItemRatePlan(BaseModel):
    id: Optional[object] = None
    """The ID of the rate plan."""

    currency: Optional[str] = None
    """The currency applied to the rate plan subscription."""

    externally_managed: Optional[bool] = None
    """Whether this rate plan is managed externally from Cloudflare."""

    is_contract: Optional[bool] = None
    """Whether a rate plan is enterprise-based (or newly adopted term contract)."""

    public_name: Optional[str] = None
    """The full name of the rate plan."""

    scope: Optional[str] = None
    """The scope that this rate plan applies to."""

    sets: Optional[List[str]] = None
    """The list of sets this rate plan applies to."""


class SubscriptionListResponseItemZone(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    name: Optional[str] = None
    """The domain name"""


class SubscriptionListResponseItem(BaseModel):
    id: Optional[str] = None
    """Subscription identifier tag."""

    app: Optional[SubscriptionListResponseItemApp] = None

    component_values: Optional[List[SubscriptionListResponseItemComponentValue]] = None
    """The list of add-ons subscribed to."""

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

    rate_plan: Optional[SubscriptionListResponseItemRatePlan] = None
    """The rate plan applied to the subscription."""

    state: Optional[Literal["Trial", "Provisioned", "Paid", "AwaitingPayment", "Cancelled", "Failed", "Expired"]] = None
    """The state that the subscription is in."""

    zone: Optional[SubscriptionListResponseItemZone] = None
    """A simple zone object. May have null properties if not a zone subscription."""


SubscriptionListResponse = List[SubscriptionListResponseItem]
