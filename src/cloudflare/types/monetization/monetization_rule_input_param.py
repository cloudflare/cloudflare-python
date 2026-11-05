# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .monetization_rule_input_fixed_price_param import MonetizationRuleInputFixedPriceParam
from .monetization_rule_input_origin_controlled_param import MonetizationRuleInputOriginControlledParam

__all__ = ["MonetizationRuleInputParam"]

MonetizationRuleInputParam: TypeAlias = Union[
    MonetizationRuleInputFixedPriceParam, MonetizationRuleInputOriginControlledParam
]
