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
    "UnionMember0AfterRuleConditionFlagshipBaseCondition",
    "UnionMember0AfterRuleConditionFlagshipLogicalCondition",
    "UnionMember0AfterRuleConditionFlagshipLogicalConditionClause",
    "UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipBaseCondition",
    "UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1",
    "UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1Clause",
    "UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipBaseCondition",
    "UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2",
    "UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2Clause",
    "UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipBaseCondition",
    "UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3",
    "UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3Clause",
    "UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipBaseCondition",
    "UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4",
    "UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4Clause",
    "UnionMember0AfterRuleRollout",
    "UnionMember1",
    "UnionMember1After",
    "UnionMember1AfterRule",
    "UnionMember1AfterRuleCondition",
    "UnionMember1AfterRuleConditionFlagshipBaseCondition",
    "UnionMember1AfterRuleConditionFlagshipLogicalCondition",
    "UnionMember1AfterRuleConditionFlagshipLogicalConditionClause",
    "UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipBaseCondition",
    "UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1",
    "UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1Clause",
    "UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipBaseCondition",
    "UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2",
    "UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2Clause",
    "UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipBaseCondition",
    "UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3",
    "UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3Clause",
    "UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipBaseCondition",
    "UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4",
    "UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4Clause",
    "UnionMember1AfterRuleRollout",
    "UnionMember2",
    "UnionMember2After",
    "UnionMember2AfterRule",
    "UnionMember2AfterRuleCondition",
    "UnionMember2AfterRuleConditionFlagshipBaseCondition",
    "UnionMember2AfterRuleConditionFlagshipLogicalCondition",
    "UnionMember2AfterRuleConditionFlagshipLogicalConditionClause",
    "UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipBaseCondition",
    "UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1",
    "UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1Clause",
    "UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipBaseCondition",
    "UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2",
    "UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2Clause",
    "UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipBaseCondition",
    "UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3",
    "UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3Clause",
    "UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipBaseCondition",
    "UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4",
    "UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4Clause",
    "UnionMember2AfterRuleRollout",
    "UnionMember2Diff",
]


class UnionMember0AfterRuleConditionFlagshipBaseCondition(BaseModel):
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
        "has",
        "not_has",
    ]

    value: Union[Optional[str], float, bool, Dict[str, object], List[object]]


class UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipBaseCondition(BaseModel):
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
        "has",
        "not_has",
    ]

    value: Union[Optional[str], float, bool, Dict[str, object], List[object]]


class UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipBaseCondition(
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
        "has",
        "not_has",
    ]

    value: Union[Optional[str], float, bool, Dict[str, object], List[object]]


class UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipBaseCondition(
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
        "has",
        "not_has",
    ]

    value: Union[Optional[str], float, bool, Dict[str, object], List[object]]


class UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipBaseCondition(
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
        "has",
        "not_has",
    ]

    value: Union[Optional[str], float, bool, Dict[str, object], List[object]]


class UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4Clause(
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
        "has",
        "not_has",
    ]

    value: Union[Optional[str], float, bool, Dict[str, object], List[object]]


class UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4(
    BaseModel
):
    clauses: List[
        UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4Clause
    ]

    logical_operator: Literal["AND", "OR"]


UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3Clause: TypeAlias = Union[
    UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipBaseCondition,
    UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4,
]


class UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3(
    BaseModel
):
    clauses: List[
        UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3Clause
    ]

    logical_operator: Literal["AND", "OR"]


UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2Clause: TypeAlias = Union[
    UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipBaseCondition,
    UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3,
]


class UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2(
    BaseModel
):
    clauses: List[
        UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2Clause
    ]

    logical_operator: Literal["AND", "OR"]


UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1Clause: TypeAlias = Union[
    UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipBaseCondition,
    UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2,
]


class UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1(BaseModel):
    clauses: List[UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1Clause]

    logical_operator: Literal["AND", "OR"]


UnionMember0AfterRuleConditionFlagshipLogicalConditionClause: TypeAlias = Union[
    UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipBaseCondition,
    UnionMember0AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1,
]


class UnionMember0AfterRuleConditionFlagshipLogicalCondition(BaseModel):
    clauses: List[UnionMember0AfterRuleConditionFlagshipLogicalConditionClause]

    logical_operator: Literal["AND", "OR"]


UnionMember0AfterRuleCondition: TypeAlias = Union[
    UnionMember0AfterRuleConditionFlagshipBaseCondition, UnionMember0AfterRuleConditionFlagshipLogicalCondition
]


class UnionMember0AfterRuleRollout(BaseModel):
    percentage: float
    """
    Percentage of matching traffic (0–100, up to 2 decimal places) served this
    variation. For multi-way splits, use cumulative upper bounds across rules (e.g.
    30, 70, 100).
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
    """Evaluation order: the API evaluates rules with lower numbers first.

    Must be unique across the flag's rules.
    """

    serve_variation: str
    """Variation the API serves when this rule matches. Must be a key in `variations`."""

    rollout: Optional[UnionMember0AfterRuleRollout] = None


class UnionMember0After(BaseModel):
    default_variation: str
    """
    Variation the API serves when the flag is off, or when it's on but no rule
    matches the context. Must be a key in `variations`.
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

    type: Literal["boolean", "string", "number", "json"]
    """Server-inferred value type shared by all of the flag's variations."""

    variations: Dict[str, Union[Optional[str], float, bool, Dict[str, object], List[object]]]
    """Map of variation name to value.

    All values share the same type (boolean, string, number, or JSON object/array),
    and each serialized value stays within 10KB.
    """

    description: Optional[str] = None
    """Optional operator-facing description. It does not affect flag evaluation."""

    metadata: Optional[Dict[str, Union[bool, str, float]]] = None
    """Key-value metadata associated with the flag.

    Returned only when the flag has metadata.
    """

    updated_at: Optional[str] = None

    updated_by: Optional[str] = None


class UnionMember0(BaseModel):
    after: UnionMember0After

    event: Literal["create"]

    flag_key: str


class UnionMember1AfterRuleConditionFlagshipBaseCondition(BaseModel):
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
        "has",
        "not_has",
    ]

    value: Union[Optional[str], float, bool, Dict[str, object], List[object]]


class UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipBaseCondition(BaseModel):
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
        "has",
        "not_has",
    ]

    value: Union[Optional[str], float, bool, Dict[str, object], List[object]]


class UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipBaseCondition(
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
        "has",
        "not_has",
    ]

    value: Union[Optional[str], float, bool, Dict[str, object], List[object]]


class UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipBaseCondition(
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
        "has",
        "not_has",
    ]

    value: Union[Optional[str], float, bool, Dict[str, object], List[object]]


class UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipBaseCondition(
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
        "has",
        "not_has",
    ]

    value: Union[Optional[str], float, bool, Dict[str, object], List[object]]


class UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4Clause(
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
        "has",
        "not_has",
    ]

    value: Union[Optional[str], float, bool, Dict[str, object], List[object]]


class UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4(
    BaseModel
):
    clauses: List[
        UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4Clause
    ]

    logical_operator: Literal["AND", "OR"]


UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3Clause: TypeAlias = Union[
    UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipBaseCondition,
    UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4,
]


class UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3(
    BaseModel
):
    clauses: List[
        UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3Clause
    ]

    logical_operator: Literal["AND", "OR"]


UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2Clause: TypeAlias = Union[
    UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipBaseCondition,
    UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3,
]


class UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2(
    BaseModel
):
    clauses: List[
        UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2Clause
    ]

    logical_operator: Literal["AND", "OR"]


UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1Clause: TypeAlias = Union[
    UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipBaseCondition,
    UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2,
]


class UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1(BaseModel):
    clauses: List[UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1Clause]

    logical_operator: Literal["AND", "OR"]


UnionMember1AfterRuleConditionFlagshipLogicalConditionClause: TypeAlias = Union[
    UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipBaseCondition,
    UnionMember1AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1,
]


class UnionMember1AfterRuleConditionFlagshipLogicalCondition(BaseModel):
    clauses: List[UnionMember1AfterRuleConditionFlagshipLogicalConditionClause]

    logical_operator: Literal["AND", "OR"]


UnionMember1AfterRuleCondition: TypeAlias = Union[
    UnionMember1AfterRuleConditionFlagshipBaseCondition, UnionMember1AfterRuleConditionFlagshipLogicalCondition
]


class UnionMember1AfterRuleRollout(BaseModel):
    percentage: float
    """
    Percentage of matching traffic (0–100, up to 2 decimal places) served this
    variation. For multi-way splits, use cumulative upper bounds across rules (e.g.
    30, 70, 100).
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
    """Evaluation order: the API evaluates rules with lower numbers first.

    Must be unique across the flag's rules.
    """

    serve_variation: str
    """Variation the API serves when this rule matches. Must be a key in `variations`."""

    rollout: Optional[UnionMember1AfterRuleRollout] = None


class UnionMember1After(BaseModel):
    default_variation: str
    """
    Variation the API serves when the flag is off, or when it's on but no rule
    matches the context. Must be a key in `variations`.
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

    type: Literal["boolean", "string", "number", "json"]
    """Server-inferred value type shared by all of the flag's variations."""

    variations: Dict[str, Union[Optional[str], float, bool, Dict[str, object], List[object]]]
    """Map of variation name to value.

    All values share the same type (boolean, string, number, or JSON object/array),
    and each serialized value stays within 10KB.
    """

    description: Optional[str] = None
    """Optional operator-facing description. It does not affect flag evaluation."""

    metadata: Optional[Dict[str, Union[bool, str, float]]] = None
    """Key-value metadata associated with the flag.

    Returned only when the flag has metadata.
    """

    updated_at: Optional[str] = None

    updated_by: Optional[str] = None


class UnionMember1(BaseModel):
    after: UnionMember1After

    event: Literal["delete"]

    flag_key: str


class UnionMember2AfterRuleConditionFlagshipBaseCondition(BaseModel):
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
        "has",
        "not_has",
    ]

    value: Union[Optional[str], float, bool, Dict[str, object], List[object]]


class UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipBaseCondition(BaseModel):
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
        "has",
        "not_has",
    ]

    value: Union[Optional[str], float, bool, Dict[str, object], List[object]]


class UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipBaseCondition(
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
        "has",
        "not_has",
    ]

    value: Union[Optional[str], float, bool, Dict[str, object], List[object]]


class UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipBaseCondition(
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
        "has",
        "not_has",
    ]

    value: Union[Optional[str], float, bool, Dict[str, object], List[object]]


class UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipBaseCondition(
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
        "has",
        "not_has",
    ]

    value: Union[Optional[str], float, bool, Dict[str, object], List[object]]


class UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4Clause(
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
        "has",
        "not_has",
    ]

    value: Union[Optional[str], float, bool, Dict[str, object], List[object]]


class UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4(
    BaseModel
):
    clauses: List[
        UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4Clause
    ]

    logical_operator: Literal["AND", "OR"]


UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3Clause: TypeAlias = Union[
    UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipBaseCondition,
    UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4,
]


class UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3(
    BaseModel
):
    clauses: List[
        UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3Clause
    ]

    logical_operator: Literal["AND", "OR"]


UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2Clause: TypeAlias = Union[
    UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipBaseCondition,
    UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3,
]


class UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2(
    BaseModel
):
    clauses: List[
        UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2Clause
    ]

    logical_operator: Literal["AND", "OR"]


UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1Clause: TypeAlias = Union[
    UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipBaseCondition,
    UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2,
]


class UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1(BaseModel):
    clauses: List[UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1Clause]

    logical_operator: Literal["AND", "OR"]


UnionMember2AfterRuleConditionFlagshipLogicalConditionClause: TypeAlias = Union[
    UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipBaseCondition,
    UnionMember2AfterRuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1,
]


class UnionMember2AfterRuleConditionFlagshipLogicalCondition(BaseModel):
    clauses: List[UnionMember2AfterRuleConditionFlagshipLogicalConditionClause]

    logical_operator: Literal["AND", "OR"]


UnionMember2AfterRuleCondition: TypeAlias = Union[
    UnionMember2AfterRuleConditionFlagshipBaseCondition, UnionMember2AfterRuleConditionFlagshipLogicalCondition
]


class UnionMember2AfterRuleRollout(BaseModel):
    percentage: float
    """
    Percentage of matching traffic (0–100, up to 2 decimal places) served this
    variation. For multi-way splits, use cumulative upper bounds across rules (e.g.
    30, 70, 100).
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
    """Evaluation order: the API evaluates rules with lower numbers first.

    Must be unique across the flag's rules.
    """

    serve_variation: str
    """Variation the API serves when this rule matches. Must be a key in `variations`."""

    rollout: Optional[UnionMember2AfterRuleRollout] = None


class UnionMember2After(BaseModel):
    default_variation: str
    """
    Variation the API serves when the flag is off, or when it's on but no rule
    matches the context. Must be a key in `variations`.
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

    type: Literal["boolean", "string", "number", "json"]
    """Server-inferred value type shared by all of the flag's variations."""

    variations: Dict[str, Union[Optional[str], float, bool, Dict[str, object], List[object]]]
    """Map of variation name to value.

    All values share the same type (boolean, string, number, or JSON object/array),
    and each serialized value stays within 10KB.
    """

    description: Optional[str] = None
    """Optional operator-facing description. It does not affect flag evaluation."""

    metadata: Optional[Dict[str, Union[bool, str, float]]] = None
    """Key-value metadata associated with the flag.

    Returned only when the flag has metadata.
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
