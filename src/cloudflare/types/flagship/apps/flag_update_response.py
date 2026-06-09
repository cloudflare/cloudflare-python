# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = [
    "FlagUpdateResponse",
    "Rule",
    "RuleCondition",
    "RuleConditionUnionMember0",
    "RuleConditionUnionMember1",
    "RuleConditionUnionMember1Clause",
    "RuleConditionUnionMember1ClauseUnionMember0",
    "RuleConditionUnionMember1ClauseUnionMember1",
    "RuleConditionUnionMember1ClauseUnionMember1Clause",
    "RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember0",
    "RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1",
    "RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1Clause",
    "RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0",
    "RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1",
    "RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause",
    "RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0",
    "RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1",
    "RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause",
    "RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0",
    "RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1",
    "RuleRollout",
]


class RuleConditionUnionMember0(BaseModel):
    attribute: str

    operator: Literal[
        "equals",
        "not_equals",
        "greater_than",
        "less_than",
        "greater_than_or_equals",
        "less_than_or_equals",
        "contains",
        "starts_with",
        "ends_with",
        "in",
        "not_in",
    ]

    value: object
    """Value to compare against the context attribute.

    Must be an array for `in` and `not_in`; numeric and ISO-8601 datetime strings
    are accepted by the ordering operators.
    """


class RuleConditionUnionMember1ClauseUnionMember0(BaseModel):
    attribute: str

    operator: Literal[
        "equals",
        "not_equals",
        "greater_than",
        "less_than",
        "greater_than_or_equals",
        "less_than_or_equals",
        "contains",
        "starts_with",
        "ends_with",
        "in",
        "not_in",
    ]

    value: object
    """Value to compare against the context attribute.

    Must be an array for `in` and `not_in`; numeric and ISO-8601 datetime strings
    are accepted by the ordering operators.
    """


class RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember0(BaseModel):
    attribute: str

    operator: Literal[
        "equals",
        "not_equals",
        "greater_than",
        "less_than",
        "greater_than_or_equals",
        "less_than_or_equals",
        "contains",
        "starts_with",
        "ends_with",
        "in",
        "not_in",
    ]

    value: object
    """Value to compare against the context attribute.

    Must be an array for `in` and `not_in`; numeric and ISO-8601 datetime strings
    are accepted by the ordering operators.
    """


class RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0(BaseModel):
    attribute: str

    operator: Literal[
        "equals",
        "not_equals",
        "greater_than",
        "less_than",
        "greater_than_or_equals",
        "less_than_or_equals",
        "contains",
        "starts_with",
        "ends_with",
        "in",
        "not_in",
    ]

    value: object
    """Value to compare against the context attribute.

    Must be an array for `in` and `not_in`; numeric and ISO-8601 datetime strings
    are accepted by the ordering operators.
    """


class RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0(BaseModel):
    attribute: str

    operator: Literal[
        "equals",
        "not_equals",
        "greater_than",
        "less_than",
        "greater_than_or_equals",
        "less_than_or_equals",
        "contains",
        "starts_with",
        "ends_with",
        "in",
        "not_in",
    ]

    value: object
    """Value to compare against the context attribute.

    Must be an array for `in` and `not_in`; numeric and ISO-8601 datetime strings
    are accepted by the ordering operators.
    """


class RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0(
    BaseModel
):
    attribute: str

    operator: Literal[
        "equals",
        "not_equals",
        "greater_than",
        "less_than",
        "greater_than_or_equals",
        "less_than_or_equals",
        "contains",
        "starts_with",
        "ends_with",
        "in",
        "not_in",
    ]

    value: object
    """Value to compare against the context attribute.

    Must be an array for `in` and `not_in`; numeric and ISO-8601 datetime strings
    are accepted by the ordering operators.
    """


class RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1(
    BaseModel
):
    clauses: List[Union[Optional[str], float, bool, Dict[str, object], List[object]]]

    logical_operator: Literal["AND", "OR"]


RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause: TypeAlias = Union[
    RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0,
    RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1,
]


class RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1(BaseModel):
    clauses: List[
        RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause
    ]

    logical_operator: Literal["AND", "OR"]


RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause: TypeAlias = Union[
    RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0,
    RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1,
]


class RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1(BaseModel):
    clauses: List[RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause]

    logical_operator: Literal["AND", "OR"]


RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1Clause: TypeAlias = Union[
    RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0,
    RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1,
]


class RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1(BaseModel):
    clauses: List[RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1Clause]

    logical_operator: Literal["AND", "OR"]


RuleConditionUnionMember1ClauseUnionMember1Clause: TypeAlias = Union[
    RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember0,
    RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1,
]


class RuleConditionUnionMember1ClauseUnionMember1(BaseModel):
    clauses: List[RuleConditionUnionMember1ClauseUnionMember1Clause]

    logical_operator: Literal["AND", "OR"]


RuleConditionUnionMember1Clause: TypeAlias = Union[
    RuleConditionUnionMember1ClauseUnionMember0, RuleConditionUnionMember1ClauseUnionMember1
]


class RuleConditionUnionMember1(BaseModel):
    clauses: List[RuleConditionUnionMember1Clause]

    logical_operator: Literal["AND", "OR"]


RuleCondition: TypeAlias = Union[RuleConditionUnionMember0, RuleConditionUnionMember1]


class RuleRollout(BaseModel):
    percentage: float
    """Percentage of matching traffic (0–100) served this variation.

    For multi-way splits, use cumulative upper bounds across rules (e.g. 30, 70,
    100).
    """

    attribute: Optional[str] = None
    """Context attribute used for sticky bucketing.

    Defaults to `targetingKey`. If absent at evaluation time, bucketing is random
    per request.
    """


class Rule(BaseModel):
    conditions: List[RuleCondition]
    """Conditions the context must satisfy for this rule to match.

    An empty array matches all contexts.
    """

    priority: int
    """Evaluation order; lower numbers are evaluated first.

    Must be unique across the flag's rules.
    """

    serve_variation: str
    """Variation served when this rule matches. Must be a key in `variations`."""

    rollout: Optional[RuleRollout] = None


class FlagUpdateResponse(BaseModel):
    default_variation: str
    """Variation served when no rule matches or the flag is disabled.

    Must be a key in `variations`.
    """

    enabled: bool
    """When false, the flag bypasses all rules and always serves `default_variation`."""

    key: str
    """Unique identifier for the flag within an app.

    Used in all evaluation and SDK calls.
    """

    rules: List[Rule]
    """Targeting rules evaluated in ascending `priority`; the first matching rule wins.

    An empty array means the flag always serves `default_variation`.
    """

    variations: Dict[str, Union[Optional[str], float, bool, Dict[str, object], List[object]]]
    """Map of variation name to value.

    All values must be the same type (boolean, string, number, or JSON
    object/array). Each serialized value must be 10KB or smaller.
    """

    description: Optional[str] = None

    type: Optional[Literal["boolean", "string", "number", "json"]] = None
    """Value type of the flag's variations.

    Inferred from the variation values on write, so it may be omitted in requests.
    """

    updated_at: Optional[str] = None

    updated_by: Optional[str] = None
