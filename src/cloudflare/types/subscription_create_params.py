# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, TypedDict

__all__ = ["SubscriptionCreateParams", "App", "ComponentValue", "RatePlan", "Zone"]


class SubscriptionCreateParams(TypedDict, total=False):
    app: App

    component_values: Iterable[ComponentValue]
    """The list of add-ons subscribed to."""

    frequency: Literal["weekly", "monthly", "quarterly", "yearly"]
    """How often the subscription is renewed automatically."""

    rate_plan: RatePlan
    """The rate plan applied to the subscription."""

    zone: Zone
    """A simple zone object. May have null properties if not a zone subscription."""


class App(TypedDict, total=False):
    install_id: str
    """app install id."""


class ComponentValue(TypedDict, total=False):
    default: float
    """The default amount assigned."""

    name: str
    """The name of the component value."""

    price: float
    """The unit price for the component value."""

    value: float
    """The amount of the component value assigned."""


class RatePlan(TypedDict, total=False):
    id: str
    """The ID of the rate plan."""

    currency: str
    """The currency applied to the rate plan subscription."""

    externally_managed: bool
    """Whether this rate plan is managed externally from Cloudflare."""

    is_contract: bool
    """Whether a rate plan is enterprise-based (or newly adopted term contract)."""

    public_name: str
    """The full name of the rate plan."""

    scope: str
    """The scope that this rate plan applies to."""

    sets: List[str]
    """The list of sets this rate plan applies to."""


class Zone(TypedDict, total=False):
    pass
