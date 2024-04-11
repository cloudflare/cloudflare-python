# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

from .rulesets import LogRuleParam, SkipRuleParam, BlockRuleParam, ExecuteRuleParam

__all__ = ["RequestRuleParam"]

RequestRuleParam = Union[BlockRuleParam, ExecuteRuleParam, LogRuleParam, SkipRuleParam]
