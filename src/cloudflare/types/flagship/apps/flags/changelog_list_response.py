# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "ChangelogListResponse",
    "UnionMember0",
    "UnionMember0After",
    "UnionMember0AfterRule",
    "UnionMember0AfterRuleCondition",
    "UnionMember0AfterRuleConditionUnionMember0",
    "UnionMember0AfterRuleConditionUnionMember1",
    "UnionMember0AfterRuleConditionUnionMember1Clause",
    "UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember0",
    "UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1",
    "UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1Clause",
    "UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember0",
    "UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1",
    "UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1Clause",
    "UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0",
    "UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1",
    "UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause",
    "UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0",
    "UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1",
    "UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause",
    "UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0",
    "UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1",
    "UnionMember0AfterRuleRollout",
    "UnionMember1",
    "UnionMember1After",
    "UnionMember1AfterRule",
    "UnionMember1AfterRuleCondition",
    "UnionMember1AfterRuleConditionUnionMember0",
    "UnionMember1AfterRuleConditionUnionMember1",
    "UnionMember1AfterRuleConditionUnionMember1Clause",
    "UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember0",
    "UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1",
    "UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1Clause",
    "UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember0",
    "UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1",
    "UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1Clause",
    "UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0",
    "UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1",
    "UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause",
    "UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0",
    "UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1",
    "UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause",
    "UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0",
    "UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1",
    "UnionMember1AfterRuleRollout",
    "UnionMember2",
    "UnionMember2After",
    "UnionMember2AfterRule",
    "UnionMember2AfterRuleCondition",
    "UnionMember2AfterRuleConditionUnionMember0",
    "UnionMember2AfterRuleConditionUnionMember1",
    "UnionMember2AfterRuleConditionUnionMember1Clause",
    "UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember0",
    "UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1",
    "UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1Clause",
    "UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember0",
    "UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1",
    "UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1Clause",
    "UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0",
    "UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1",
    "UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause",
    "UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0",
    "UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1",
    "UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause",
    "UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0",
    "UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1",
    "UnionMember2AfterRuleRollout",
    "UnionMember2Diff",
]


class UnionMember0AfterRuleConditionUnionMember0(BaseModel):
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


class UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember0(BaseModel):
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


class UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember0(BaseModel):
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


class UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0(BaseModel):
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


class UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0(
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


class UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0(
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


class UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1(
    BaseModel
):
    clauses: List[Union[Optional[str], float, bool, Dict[str, object], List[object]]]

    logical_operator: Literal["AND", "OR"]


UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause: TypeAlias = Union[
    UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0,
    UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1,
]


class UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1(
    BaseModel
):
    clauses: List[
        UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause
    ]

    logical_operator: Literal["AND", "OR"]


UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause: TypeAlias = Union[
    UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0,
    UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1,
]


class UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1(BaseModel):
    clauses: List[
        UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause
    ]

    logical_operator: Literal["AND", "OR"]


UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1Clause: TypeAlias = Union[
    UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0,
    UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1,
]


class UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1(BaseModel):
    clauses: List[UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1Clause]

    logical_operator: Literal["AND", "OR"]


UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1Clause: TypeAlias = Union[
    UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember0,
    UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1,
]


class UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1(BaseModel):
    clauses: List[UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1Clause]

    logical_operator: Literal["AND", "OR"]


UnionMember0AfterRuleConditionUnionMember1Clause: TypeAlias = Union[
    UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember0,
    UnionMember0AfterRuleConditionUnionMember1ClauseUnionMember1,
]


class UnionMember0AfterRuleConditionUnionMember1(BaseModel):
    clauses: List[UnionMember0AfterRuleConditionUnionMember1Clause]

    logical_operator: Literal["AND", "OR"]


UnionMember0AfterRuleCondition: TypeAlias = Union[
    UnionMember0AfterRuleConditionUnionMember0, UnionMember0AfterRuleConditionUnionMember1
]


class UnionMember0AfterRuleRollout(BaseModel):
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


class UnionMember0AfterRule(BaseModel):
    conditions: List[UnionMember0AfterRuleCondition]
    """Conditions the context must satisfy for this rule to match.

    An empty array matches all contexts.
    """

    priority: int
    """Evaluation order; lower numbers are evaluated first.

    Must be unique across the flag's rules.
    """

    serve_variation: str
    """Variation served when this rule matches. Must be a key in `variations`."""

    rollout: Optional[UnionMember0AfterRuleRollout] = None


class UnionMember0After(BaseModel):
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

    rules: List[UnionMember0AfterRule]
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


class UnionMember0(BaseModel):
    after: UnionMember0After

    event: Literal["create"]

    flag_key: str


class UnionMember1AfterRuleConditionUnionMember0(BaseModel):
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


class UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember0(BaseModel):
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


class UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember0(BaseModel):
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


class UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0(BaseModel):
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


class UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0(
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


class UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0(
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


class UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1(
    BaseModel
):
    clauses: List[Union[Optional[str], float, bool, Dict[str, object], List[object]]]

    logical_operator: Literal["AND", "OR"]


UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause: TypeAlias = Union[
    UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0,
    UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1,
]


class UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1(
    BaseModel
):
    clauses: List[
        UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause
    ]

    logical_operator: Literal["AND", "OR"]


UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause: TypeAlias = Union[
    UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0,
    UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1,
]


class UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1(BaseModel):
    clauses: List[
        UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause
    ]

    logical_operator: Literal["AND", "OR"]


UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1Clause: TypeAlias = Union[
    UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0,
    UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1,
]


class UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1(BaseModel):
    clauses: List[UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1Clause]

    logical_operator: Literal["AND", "OR"]


UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1Clause: TypeAlias = Union[
    UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember0,
    UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1,
]


class UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1(BaseModel):
    clauses: List[UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1Clause]

    logical_operator: Literal["AND", "OR"]


UnionMember1AfterRuleConditionUnionMember1Clause: TypeAlias = Union[
    UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember0,
    UnionMember1AfterRuleConditionUnionMember1ClauseUnionMember1,
]


class UnionMember1AfterRuleConditionUnionMember1(BaseModel):
    clauses: List[UnionMember1AfterRuleConditionUnionMember1Clause]

    logical_operator: Literal["AND", "OR"]


UnionMember1AfterRuleCondition: TypeAlias = Union[
    UnionMember1AfterRuleConditionUnionMember0, UnionMember1AfterRuleConditionUnionMember1
]


class UnionMember1AfterRuleRollout(BaseModel):
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


class UnionMember1AfterRule(BaseModel):
    conditions: List[UnionMember1AfterRuleCondition]
    """Conditions the context must satisfy for this rule to match.

    An empty array matches all contexts.
    """

    priority: int
    """Evaluation order; lower numbers are evaluated first.

    Must be unique across the flag's rules.
    """

    serve_variation: str
    """Variation served when this rule matches. Must be a key in `variations`."""

    rollout: Optional[UnionMember1AfterRuleRollout] = None


class UnionMember1After(BaseModel):
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

    rules: List[UnionMember1AfterRule]
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


class UnionMember1(BaseModel):
    after: UnionMember1After

    event: Literal["delete"]

    flag_key: str


class UnionMember2AfterRuleConditionUnionMember0(BaseModel):
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


class UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember0(BaseModel):
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


class UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember0(BaseModel):
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


class UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0(BaseModel):
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


class UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0(
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


class UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0(
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


class UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1(
    BaseModel
):
    clauses: List[Union[Optional[str], float, bool, Dict[str, object], List[object]]]

    logical_operator: Literal["AND", "OR"]


UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause: TypeAlias = Union[
    UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0,
    UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1,
]


class UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1(
    BaseModel
):
    clauses: List[
        UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause
    ]

    logical_operator: Literal["AND", "OR"]


UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause: TypeAlias = Union[
    UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0,
    UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1,
]


class UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1(BaseModel):
    clauses: List[
        UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause
    ]

    logical_operator: Literal["AND", "OR"]


UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1Clause: TypeAlias = Union[
    UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0,
    UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1,
]


class UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1(BaseModel):
    clauses: List[UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1Clause]

    logical_operator: Literal["AND", "OR"]


UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1Clause: TypeAlias = Union[
    UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember0,
    UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1,
]


class UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1(BaseModel):
    clauses: List[UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1Clause]

    logical_operator: Literal["AND", "OR"]


UnionMember2AfterRuleConditionUnionMember1Clause: TypeAlias = Union[
    UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember0,
    UnionMember2AfterRuleConditionUnionMember1ClauseUnionMember1,
]


class UnionMember2AfterRuleConditionUnionMember1(BaseModel):
    clauses: List[UnionMember2AfterRuleConditionUnionMember1Clause]

    logical_operator: Literal["AND", "OR"]


UnionMember2AfterRuleCondition: TypeAlias = Union[
    UnionMember2AfterRuleConditionUnionMember0, UnionMember2AfterRuleConditionUnionMember1
]


class UnionMember2AfterRuleRollout(BaseModel):
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


class UnionMember2AfterRule(BaseModel):
    conditions: List[UnionMember2AfterRuleCondition]
    """Conditions the context must satisfy for this rule to match.

    An empty array matches all contexts.
    """

    priority: int
    """Evaluation order; lower numbers are evaluated first.

    Must be unique across the flag's rules.
    """

    serve_variation: str
    """Variation served when this rule matches. Must be a key in `variations`."""

    rollout: Optional[UnionMember2AfterRuleRollout] = None


class UnionMember2After(BaseModel):
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

    rules: List[UnionMember2AfterRule]
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


class UnionMember2Diff(BaseModel):
    from_: Union[Optional[str], float, bool, Dict[str, object], List[object], None] = FieldInfo(
        alias="from", default=None
    )

    to: Union[Optional[str], float, bool, Dict[str, object], List[object], None] = None


class UnionMember2(BaseModel):
    after: UnionMember2After

    diff: Dict[str, UnionMember2Diff]

    event: Literal["update"]

    flag_key: str


ChangelogListResponse: TypeAlias = Union[UnionMember0, UnionMember1, UnionMember2]
