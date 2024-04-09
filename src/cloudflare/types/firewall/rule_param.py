# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, TypedDict

from .products_item import ProductsItem
from .deleted_filter import DeletedFilter

__all__ = ["RuleParam", "Filter", "FilterFirewallFilter"]


class FilterFirewallFilter(TypedDict, total=False):
    description: str
    """An informative summary of the filter."""

    expression: str
    """The filter expression.

    For more information, refer to
    [Expressions](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/).
    """

    paused: bool
    """When true, indicates that the filter is currently paused."""

    ref: str
    """A short reference tag. Allows you to select related filters."""


Filter = Union[FilterFirewallFilter, DeletedFilter]


class RuleParam(TypedDict, total=False):
    action: Literal["block", "challenge", "js_challenge", "managed_challenge", "allow", "log", "bypass"]
    """The action to apply to a matched request.

    The `log` action is only available on an Enterprise plan.
    """

    description: str
    """An informative summary of the firewall rule."""

    filter: Filter

    paused: bool
    """When true, indicates that the firewall rule is currently paused."""

    priority: float
    """The priority of the rule.

    Optional value used to define the processing order. A lower number indicates a
    higher priority. If not provided, rules with a defined priority will be
    processed before rules without a priority.
    """

    products: List[ProductsItem]

    ref: str
    """A short reference tag. Allows you to select related firewall rules."""
