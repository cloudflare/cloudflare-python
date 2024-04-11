# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union

from .rulesets import LogRule, SkipRule, BlockRule, ExecuteRule

__all__ = ["ResponseRule", "ResponseRuleItem"]

ResponseRuleItem = Union[BlockRule, ExecuteRule, LogRule, SkipRule]

ResponseRule = List[ResponseRuleItem]
