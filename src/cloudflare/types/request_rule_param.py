# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union

from .rulesets import LogRuleParam, SkipRuleParam, BlockRuleParam, ExecuteRuleParam

__all__ = ["RequestRuleParamItem"]

RequestRuleParamItem = Union[BlockRuleParam, ExecuteRuleParam, LogRuleParam, SkipRuleParam]

RequestRuleParam = List[RequestRuleParamItem]
