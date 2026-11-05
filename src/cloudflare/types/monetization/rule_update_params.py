# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .monetization_rule_input_param import MonetizationRuleInputParam

__all__ = ["RuleUpdateParams"]


class RuleUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """The unique ID of the zone."""

    rules: Required[Iterable[MonetizationRuleInputParam]]
    """Full desired Payment Required ruleset.

    An empty array clears all payment rules. The ruleset may contain at most 40
    unique wallet addresses; address comparison is case-insensitive. Every address
    must pass wallet screening before deployment.
    """
