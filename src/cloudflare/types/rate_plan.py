# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .component import Component

__all__ = ["RatePlan"]


class RatePlan(BaseModel):
    id: Optional[str] = None
    """Plan identifier tag."""

    components: Optional[List[Component]] = None
    """Array of available components values for the plan."""

    currency: Optional[str] = None
    """The monetary unit in which pricing information is displayed."""

    duration: Optional[float] = None
    """The duration of the plan subscription."""

    frequency: Optional[Literal["weekly", "monthly", "quarterly", "yearly"]] = None
    """The frequency at which you will be billed for this plan."""

    name: Optional[str] = None
    """The plan name."""
