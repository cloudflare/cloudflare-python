# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from . import filter
from ..action import Action
from ..._models import BaseModel
from .products_item import ProductsItem
from .deleted_filter import DeletedFilter

__all__ = ["Rule", "Filter"]

Filter = Union[filter.Filter, DeletedFilter]


class Rule(BaseModel):
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

    products: Optional[List[ProductsItem]] = None

    ref: Optional[str] = None
    """A short reference tag. Allows you to select related firewall rules."""
