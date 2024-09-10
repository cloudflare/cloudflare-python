# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AvailableRatePlan"]


class AvailableRatePlan(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    can_subscribe: Optional[bool] = None
    """Indicates whether you can subscribe to this plan."""

    currency: Optional[str] = None
    """The monetary unit in which pricing information is displayed."""

    externally_managed: Optional[bool] = None
    """Indicates whether this plan is managed externally."""

    frequency: Optional[Literal["weekly", "monthly", "quarterly", "yearly"]] = None
    """The frequency at which you will be billed for this plan."""

    is_subscribed: Optional[bool] = None
    """Indicates whether you are currently subscribed to this plan."""

    legacy_discount: Optional[bool] = None
    """Indicates whether this plan has a legacy discount applied."""

    legacy_id: Optional[str] = None
    """The legacy identifier for this rate plan, if any."""

    name: Optional[str] = None
    """The plan name."""

    price: Optional[float] = None
    """The amount you will be billed for this plan."""
