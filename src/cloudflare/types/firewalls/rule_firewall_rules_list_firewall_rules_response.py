# File generated from our OpenAPI spec by Stainless.

from typing import List, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "RuleFirewallRulesListFirewallRulesResponse",
    "RuleFirewallRulesListFirewallRulesResponseItem",
    "RuleFirewallRulesListFirewallRulesResponseItemFilter",
    "RuleFirewallRulesListFirewallRulesResponseItemFilterLegacyJhsFilter",
    "RuleFirewallRulesListFirewallRulesResponseItemFilterLegacyJhsDeletedFilter",
]


class RuleFirewallRulesListFirewallRulesResponseItemFilterLegacyJhsFilter(BaseModel):
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


class RuleFirewallRulesListFirewallRulesResponseItemFilterLegacyJhsDeletedFilter(BaseModel):
    id: str
    """The unique identifier of the filter."""

    deleted: bool
    """When true, indicates that the firewall rule was deleted."""


RuleFirewallRulesListFirewallRulesResponseItemFilter = Union[
    RuleFirewallRulesListFirewallRulesResponseItemFilterLegacyJhsFilter,
    RuleFirewallRulesListFirewallRulesResponseItemFilterLegacyJhsDeletedFilter,
]


class RuleFirewallRulesListFirewallRulesResponseItem(BaseModel):
    id: str
    """The unique identifier of the firewall rule."""

    action: Literal["block", "challenge", "js_challenge", "managed_challenge", "allow", "log", "bypass"]
    """The action to apply to a matched request.

    The `log` action is only available on an Enterprise plan.
    """

    filter: RuleFirewallRulesListFirewallRulesResponseItemFilter

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


RuleFirewallRulesListFirewallRulesResponse = List[RuleFirewallRulesListFirewallRulesResponseItem]
