# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union

from .rulesets import LogRule, SkipRule, BlockRule, ExecuteRule

__all__ = ["ResponeRule"]

ResponeRule = Union[BlockRule, ExecuteRule, LogRule, SkipRule]
