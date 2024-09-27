# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from ..shared_params.rate_plan import RatePlan

__all__ = ["SubscriptionCreateParams"]


class SubscriptionCreateParams(TypedDict, total=False):
    frequency: Literal["weekly", "monthly", "quarterly", "yearly"]
    """How often the subscription is renewed automatically."""

    rate_plan: RatePlan
    """The rate plan applied to the subscription."""
