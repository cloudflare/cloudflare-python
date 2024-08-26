# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..filters.firewall_filter import FirewallFilter

from .deleted_filter import DeletedFilter

from typing_extensions import TypeAlias

from ..._models import BaseModel

from typing import Optional, List

from ..rate_limits.action import Action

from .product import Product

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["FirewallRule", "Filter"]

Filter: TypeAlias = Union[FirewallFilter, DeletedFilter]

class FirewallRule(BaseModel):
    id: Optional[str] = None
    """The unique identifier of the firewall rule."""

    action: Optional[Action] = None
    """The action to apply to a matched request.

    The `log` action is only available on an Enterprise plan.
    """

    description: Optional[str] = None
    """An informative summary of the firewall rule."""

    filter: Optional[Filter] = None

    paused: Optional[bool] = None
    """When true, indicates that the firewall rule is currently paused."""

    priority: Optional[float] = None
    """The priority of the rule.

    Optional value used to define the processing order. A lower number indicates a
    higher priority. If not provided, rules with a defined priority will be
    processed before rules without a priority.
    """

    products: Optional[List[Product]] = None

    ref: Optional[str] = None
    """A short reference tag. Allows you to select related firewall rules."""