# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "RuleParam",
    "WAFManagedRulesAnomalyRule",
    "WAFManagedRulesTraditionalDenyRule",
    "WAFManagedRulesTraditionalAllowRule",
]


class WAFManagedRulesAnomalyRule(TypedDict, total=False):
    mode: Required[Literal["on", "off"]]
    """When set to `on`, the current WAF rule will be used when evaluating the request.

    Applies to anomaly detection WAF rules.
    """


class WAFManagedRulesTraditionalDenyRule(TypedDict, total=False):
    mode: Required[Literal["default", "disable", "simulate", "block", "challenge"]]
    """The action that the current WAF rule will perform when triggered.

    Applies to traditional (deny) WAF rules.
    """


class WAFManagedRulesTraditionalAllowRule(TypedDict, total=False):
    default_mode: Required[object]

    mode: Required[Literal["on", "off"]]
    """When set to `on`, the current rule will be used when evaluating the request.

    Applies to traditional (allow) WAF rules.
    """


RuleParam = Union[WAFManagedRulesAnomalyRule, WAFManagedRulesTraditionalDenyRule, WAFManagedRulesTraditionalAllowRule]
