# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union

from .rulesets import LogRule, SkipRule, BlockRule, ExecuteRule

__all__ = ["ResponeRule", "ResponeRuleItem"]

ResponeRuleItem = Union[BlockRule, ExecuteRule, LogRule, SkipRule]

ResponeRule = List[ResponeRuleItem]
