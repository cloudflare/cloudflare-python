# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "LockUpdateParams",
    "Rule",
    "RuleCondition",
    "RuleConditionR2LockRuleAgeCondition",
    "RuleConditionR2LockRuleDateCondition",
    "RuleConditionR2LockRuleIndefiniteCondition",
]


class LockUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID"""

    rules: Iterable[Rule]

    jurisdiction: Annotated[Literal["default", "eu", "fedramp"], PropertyInfo(alias="cf-r2-jurisdiction")]
    """The bucket jurisdiction"""


class RuleConditionR2LockRuleAgeCondition(TypedDict, total=False):
    max_age_seconds: Required[Annotated[int, PropertyInfo(alias="maxAgeSeconds")]]

    type: Required[Literal["Age"]]


class RuleConditionR2LockRuleDateCondition(TypedDict, total=False):
    date: Required[Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]]

    type: Required[Literal["Date"]]


class RuleConditionR2LockRuleIndefiniteCondition(TypedDict, total=False):
    type: Required[Literal["Indefinite"]]


RuleCondition: TypeAlias = Union[
    RuleConditionR2LockRuleAgeCondition,
    RuleConditionR2LockRuleDateCondition,
    RuleConditionR2LockRuleIndefiniteCondition,
]


class Rule(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for this rule"""

    condition: Required[RuleCondition]
    """Condition to apply a lock rule to an object for how long in seconds"""

    enabled: Required[bool]
    """Whether or not this rule is in effect"""

    prefix: str
    """
    Rule will only apply to objects/uploads in the bucket that start with the given
    prefix, an empty prefix can be provided to scope rule to all objects/uploads
    """
