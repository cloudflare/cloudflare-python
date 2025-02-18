# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "LockGetResponse",
    "Rule",
    "RuleCondition",
    "RuleConditionR2LockRuleAgeCondition",
    "RuleConditionR2LockRuleDateCondition",
    "RuleConditionR2LockRuleIndefiniteCondition",
]


class RuleConditionR2LockRuleAgeCondition(BaseModel):
    max_age_seconds: int = FieldInfo(alias="maxAgeSeconds")

    type: Literal["Age"]


class RuleConditionR2LockRuleDateCondition(BaseModel):
    date: datetime.date

    type: Literal["Date"]


class RuleConditionR2LockRuleIndefiniteCondition(BaseModel):
    type: Literal["Indefinite"]


RuleCondition: TypeAlias = Union[
    RuleConditionR2LockRuleAgeCondition,
    RuleConditionR2LockRuleDateCondition,
    RuleConditionR2LockRuleIndefiniteCondition,
]


class Rule(BaseModel):
    id: str
    """Unique identifier for this rule"""

    condition: RuleCondition
    """Condition to apply a lock rule to an object for how long in seconds"""

    enabled: bool
    """Whether or not this rule is in effect"""

    prefix: Optional[str] = None
    """
    Rule will only apply to objects/uploads in the bucket that start with the given
    prefix, an empty prefix can be provided to scope rule to all objects/uploads
    """


class LockGetResponse(BaseModel):
    rules: Optional[List[Rule]] = None
