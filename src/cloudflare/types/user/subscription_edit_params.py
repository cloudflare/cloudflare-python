# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import Iterable

from .subscription_component_param import SubscriptionComponentParam

from .rate_plan_param import RatePlanParam

from .subscription_zone_param import SubscriptionZoneParam

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["SubscriptionEditParams", "App"]

class SubscriptionEditParams(TypedDict, total=False):
    app: App

    component_values: Iterable[SubscriptionComponentParam]
    """The list of add-ons subscribed to."""

    frequency: Literal["weekly", "monthly", "quarterly", "yearly"]
    """How often the subscription is renewed automatically."""

    rate_plan: RatePlanParam
    """The rate plan applied to the subscription."""

    zone: SubscriptionZoneParam
    """A simple zone object. May have null properties if not a zone subscription."""

class App(TypedDict, total=False):
    install_id: str
    """app install id."""