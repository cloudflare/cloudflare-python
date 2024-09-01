# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..user.rate_plan_param import RatePlanParam

__all__ = ["SubscriptionUpdateParams"]


class SubscriptionUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    frequency: Literal["weekly", "monthly", "quarterly", "yearly"]
    """How often the subscription is renewed automatically."""

    rate_plan: RatePlanParam
    """The rate plan applied to the subscription."""