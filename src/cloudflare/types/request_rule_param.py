# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

from .log_rule_param import LogRuleParam
from .skip_rule_param import SkipRuleParam
from .block_rule_param import BlockRuleParam
from .execute_rule_param import ExecuteRuleParam

__all__ = ["RequestRuleParam"]

RequestRuleParam = Union[BlockRuleParam, ExecuteRuleParam, LogRuleParam, SkipRuleParam]
