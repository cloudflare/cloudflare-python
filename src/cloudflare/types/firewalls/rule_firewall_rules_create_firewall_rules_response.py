# File generated from our OpenAPI spec by Stainless.

from typing import List, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "RuleFirewallRulesCreateFirewallRulesResponse",
    "RuleFirewallRulesCreateFirewallRulesResponseItem",
    "RuleFirewallRulesCreateFirewallRulesResponseItemFilter",
    "RuleFirewallRulesCreateFirewallRulesResponseItemFilterLegacyJhsFilter",
    "RuleFirewallRulesCreateFirewallRulesResponseItemFilterLegacyJhsDeletedFilter",
]


class RuleFirewallRulesCreateFirewallRulesResponseItemFilterLegacyJhsFilter(BaseModel):
    id: Optional[str] = None
    """The unique identifier of the filter."""

    description: Optional[str] = None
    """An informative summary of the filter."""

    expression: Optional[str] = None
    """The filter expression.

    For more information, refer to
    [Expressions](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/).
    """

    paused: Optional[bool] = None
    """When true, indicates that the filter is currently paused."""

    ref: Optional[str] = None
    """A short reference tag. Allows you to select related filters."""


class RuleFirewallRulesCreateFirewallRulesResponseItemFilterLegacyJhsDeletedFilter(BaseModel):
    id: str
    """The unique identifier of the filter."""

    deleted: bool
    """When true, indicates that the firewall rule was deleted."""


RuleFirewallRulesCreateFirewallRulesResponseItemFilter = Union[
    RuleFirewallRulesCreateFirewallRulesResponseItemFilterLegacyJhsFilter,
    RuleFirewallRulesCreateFirewallRulesResponseItemFilterLegacyJhsDeletedFilter,
]


class RuleFirewallRulesCreateFirewallRulesResponseItem(BaseModel):
    id: str
    """The unique identifier of the firewall rule."""

    action: Literal["block", "challenge", "js_challenge", "managed_challenge", "allow", "log", "bypass"]
    """The action to apply to a matched request.

    The `log` action is only available on an Enterprise plan.
    """

    filter: RuleFirewallRulesCreateFirewallRulesResponseItemFilter

    paused: bool
    """When true, indicates that the firewall rule is currently paused."""

    description: Optional[str] = None
    """An informative summary of the firewall rule."""

    priority: Optional[float] = None
    """The priority of the rule.

    Optional value used to define the processing order. A lower number indicates a
    higher priority. If not provided, rules with a defined priority will be
    processed before rules without a priority.
    """

    products: Optional[
        List[Literal["zoneLockdown", "uaBlock", "bic", "hot", "securityLevel", "rateLimit", "waf"]]
    ] = None

    ref: Optional[str] = None
    """A short reference tag. Allows you to select related firewall rules."""


RuleFirewallRulesCreateFirewallRulesResponse = List[RuleFirewallRulesCreateFirewallRulesResponseItem]
