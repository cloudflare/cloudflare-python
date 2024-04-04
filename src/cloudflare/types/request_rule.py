# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union

from .log_rule import LogRule
from .skip_rule import SkipRule
from .block_rule import BlockRule
from .execute_rule import ExecuteRule

__all__ = ["RequestRule"]

RequestRule = Union[BlockRule, ExecuteRule, LogRule, SkipRule]
