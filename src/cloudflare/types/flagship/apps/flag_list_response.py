# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = [
    "FlagListResponse",
    "Rule",
    "RuleCondition",
    "RuleConditionFlagshipBaseCondition",
    "RuleConditionFlagshipLogicalCondition",
    "RuleConditionFlagshipLogicalConditionClause",
    "RuleConditionFlagshipLogicalConditionClauseFlagshipBaseCondition",
    "RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1",
    "RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1Clause",
    "RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipBaseCondition",
    "RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2",
    "RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2Clause",
    "RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipBaseCondition",
    "RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3",
    "RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3Clause",
    "RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipBaseCondition",
    "RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4",
    "RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4Clause",
    "RuleRollout",
]


class RuleConditionFlagshipBaseCondition(BaseModel):
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


class RuleConditionFlagshipLogicalConditionClauseFlagshipBaseCondition(BaseModel):
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


class RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipBaseCondition(BaseModel):
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


class RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipBaseCondition(
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


class RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipBaseCondition(
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


class RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4Clause(
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


class RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4(
    BaseModel
):
    clauses: List[
        RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4Clause
    ]

    logical_operator: Literal["AND", "OR"]


RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3Clause: TypeAlias = Union[
    RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipBaseCondition,
    RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4,
]


class RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3(
    BaseModel
):
    clauses: List[
        RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3Clause
    ]

    logical_operator: Literal["AND", "OR"]


RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2Clause: TypeAlias = Union[
    RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipBaseCondition,
    RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3,
]


class RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2(BaseModel):
    clauses: List[
        RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2Clause
    ]

    logical_operator: Literal["AND", "OR"]


RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1Clause: TypeAlias = Union[
    RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipBaseCondition,
    RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2,
]


class RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1(BaseModel):
    clauses: List[RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1Clause]

    logical_operator: Literal["AND", "OR"]


RuleConditionFlagshipLogicalConditionClause: TypeAlias = Union[
    RuleConditionFlagshipLogicalConditionClauseFlagshipBaseCondition,
    RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1,
]


class RuleConditionFlagshipLogicalCondition(BaseModel):
    clauses: List[RuleConditionFlagshipLogicalConditionClause]

    logical_operator: Literal["AND", "OR"]


RuleCondition: TypeAlias = Union[RuleConditionFlagshipBaseCondition, RuleConditionFlagshipLogicalCondition]


class RuleRollout(BaseModel):
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


class Rule(BaseModel):
    conditions: List[RuleCondition]
    """Conditions the context must satisfy for this rule to match.

    An empty array matches all contexts.
    """

    priority: int
    """Evaluation order: the API evaluates rules with lower numbers first.

    Must be unique across the flag's rules.
    """

    serve_variation: str
    """Variation the API serves when this rule matches. Must be a key in `variations`."""

    rollout: Optional[RuleRollout] = None


class FlagListResponse(BaseModel):
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

    rules: List[Rule]
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
