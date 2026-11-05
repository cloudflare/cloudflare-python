# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .monetization_rule import MonetizationRule

__all__ = ["MonetizationRuleCollection"]


class MonetizationRuleCollection(BaseModel):
    """The zone's payment rules.

    Mirrors the shape of the ruleset submitted to the deploy endpoint, so the response can be read back as the desired state.
    """

    rules: List[MonetizationRule]
    """The zone's payment rules, in the order they are evaluated.

    Empty when the zone has no payment rules.
    """
