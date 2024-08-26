# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["RatePlan", "Component"]

class Component(BaseModel):
    default: Optional[float] = None
    """The default amount allocated."""

    name: Optional[Literal["zones", "page_rules", "dedicated_certificates", "dedicated_certificates_custom"]] = None
    """The unique component."""

    unit_price: Optional[float] = None
    """The unit price of the addon."""

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