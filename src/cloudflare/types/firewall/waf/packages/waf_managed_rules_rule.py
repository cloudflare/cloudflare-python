# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = [
    "WAFManagedRulesRule",
    "WAFManagedRulesAnomalyRule",
    "WAFManagedRulesAnomalyRuleGroup",
    "WAFManagedRulesTraditionalDenyRule",
    "WAFManagedRulesTraditionalDenyRuleGroup",
    "WAFManagedRulesTraditionalAllowRule",
    "WAFManagedRulesTraditionalAllowRuleGroup",
]


class WAFManagedRulesAnomalyRuleGroup(BaseModel):
    id: Optional[str] = None
    """The unique identifier of the rule group."""

    name: Optional[str] = None
    """The name of the rule group."""


class WAFManagedRulesAnomalyRule(BaseModel):
    id: str
    """The unique identifier of the WAF rule."""

    allowed_modes: List[Literal["on", "off"]]
    """Defines the available modes for the current WAF rule.

    Applies to anomaly detection WAF rules.
    """

    description: str
    """The public description of the WAF rule."""

    group: WAFManagedRulesAnomalyRuleGroup
    """The rule group to which the current WAF rule belongs."""

    mode: Literal["on", "off"]
    """When set to `on`, the current WAF rule will be used when evaluating the request.

    Applies to anomaly detection WAF rules.
    """

    package_id: str
    """The unique identifier of a WAF package."""

    priority: str
    """The order in which the individual WAF rule is executed within its rule group."""


class WAFManagedRulesTraditionalDenyRuleGroup(BaseModel):
    id: Optional[str] = None
    """The unique identifier of the rule group."""

    name: Optional[str] = None
    """The name of the rule group."""


class WAFManagedRulesTraditionalDenyRule(BaseModel):
    id: str
    """The unique identifier of the WAF rule."""

    allowed_modes: List[Literal["default", "disable", "simulate", "block", "challenge"]]
    """The list of possible actions of the WAF rule when it is triggered."""

    default_mode: Literal["disable", "simulate", "block", "challenge"]
    """The default action/mode of a rule."""

    description: str
    """The public description of the WAF rule."""

    group: WAFManagedRulesTraditionalDenyRuleGroup
    """The rule group to which the current WAF rule belongs."""

    mode: Literal["default", "disable", "simulate", "block", "challenge"]
    """The action that the current WAF rule will perform when triggered.

    Applies to traditional (deny) WAF rules.
    """

    package_id: str
    """The unique identifier of a WAF package."""

    priority: str
    """The order in which the individual WAF rule is executed within its rule group."""


class WAFManagedRulesTraditionalAllowRuleGroup(BaseModel):
    id: Optional[str] = None
    """The unique identifier of the rule group."""

    name: Optional[str] = None
    """The name of the rule group."""


class WAFManagedRulesTraditionalAllowRule(BaseModel):
    id: str
    """The unique identifier of the WAF rule."""

    allowed_modes: List[Literal["on", "off"]]
    """Defines the available modes for the current WAF rule."""

    description: str
    """The public description of the WAF rule."""

    group: WAFManagedRulesTraditionalAllowRuleGroup
    """The rule group to which the current WAF rule belongs."""

    mode: Literal["on", "off"]
    """When set to `on`, the current rule will be used when evaluating the request.

    Applies to traditional (allow) WAF rules.
    """

    package_id: str
    """The unique identifier of a WAF package."""

    priority: str
    """The order in which the individual WAF rule is executed within its rule group."""


WAFManagedRulesRule = Union[
    WAFManagedRulesAnomalyRule, WAFManagedRulesTraditionalDenyRule, WAFManagedRulesTraditionalAllowRule
]
