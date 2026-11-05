# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .monetization_rule_input_fixed_price import MonetizationRuleInputFixedPrice
from .monetization_rule_input_origin_controlled import MonetizationRuleInputOriginControlled

__all__ = [
    "MonetizationRule",
    "MonetizationRulesMonetizationRuleInputFixedPrice",
    "MonetizationRulesMonetizationRuleInputOriginControlled",
]


class MonetizationRulesMonetizationRuleInputFixedPrice(MonetizationRuleInputFixedPrice):
    """Payment rule with a fixed price set at configuration time."""

    id: str  # type: ignore
    """The server-assigned unique ID of the payment rule.

    Stable across full-ruleset replacements.
    """


class MonetizationRulesMonetizationRuleInputOriginControlled(MonetizationRuleInputOriginControlled):
    """Payment rule whose price the origin server sets dynamically.

    The rule carries no price and the price field must be omitted — any provided value, including "0", is rejected because it would not be enforced.
    """

    id: str  # type: ignore
    """The server-assigned unique ID of the payment rule.

    Stable across full-ruleset replacements.
    """


MonetizationRule: TypeAlias = Union[
    MonetizationRulesMonetizationRuleInputFixedPrice, MonetizationRulesMonetizationRuleInputOriginControlled
]
