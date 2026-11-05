# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "FlagCreateParams",
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


class FlagCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID that owns the Flagship app."""

    default_variation: Required[str]
    """
    Variation the API serves when the flag is off, or when it's on but no rule
    matches the context. Must be a key in `variations`.
    """

    enabled: Required[bool]
    """When false, the flag bypasses all rules and always serves `default_variation`."""

    key: Required[str]
    """Unique identifier for the flag within an app.

    Used in all evaluation and SDK calls.
    """

    rules: Required[Iterable[Rule]]
    """Targeting rules evaluated in ascending `priority`; the first matching rule wins.

    An empty array means the flag always serves `default_variation`.
    """

    variations: Required[Dict[str, Union[Optional[str], float, bool, Dict[str, object], Iterable[object]]]]
    """Map of variation name to value.

    All values share the same type (boolean, string, number, or JSON object/array),
    and each serialized value stays within 10KB.
    """

    description: Optional[str]
    """Optional operator-facing description. It does not affect flag evaluation."""

    metadata: Optional[Dict[str, Union[bool, str, float]]]
    """Key-value metadata associated with the flag.

    `null` or an empty object clears existing metadata; omission semantics depend on
    the endpoint (PUT clears it, PATCH preserves it).
    """

    type: Literal["boolean", "string", "number", "json"]
    """Deprecated compatibility field.

    Omit it; the API ignores this value and infers the type from the flag's
    variations.
    """


class RuleConditionFlagshipBaseCondition(TypedDict, total=False):
    attribute: Required[str]

    operator: Required[
        Literal[
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
    ]

    value: Required[Union[Optional[str], float, bool, Dict[str, object], Iterable[object]]]


class RuleConditionFlagshipLogicalConditionClauseFlagshipBaseCondition(TypedDict, total=False):
    attribute: Required[str]

    operator: Required[
        Literal[
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
    ]

    value: Required[Union[Optional[str], float, bool, Dict[str, object], Iterable[object]]]


class RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipBaseCondition(
    TypedDict, total=False
):
    attribute: Required[str]

    operator: Required[
        Literal[
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
    ]

    value: Required[Union[Optional[str], float, bool, Dict[str, object], Iterable[object]]]


class RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipBaseCondition(
    TypedDict, total=False
):
    attribute: Required[str]

    operator: Required[
        Literal[
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
    ]

    value: Required[Union[Optional[str], float, bool, Dict[str, object], Iterable[object]]]


class RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipBaseCondition(
    TypedDict, total=False
):
    attribute: Required[str]

    operator: Required[
        Literal[
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
    ]

    value: Required[Union[Optional[str], float, bool, Dict[str, object], Iterable[object]]]


class RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4Clause(
    TypedDict, total=False
):
    attribute: Required[str]

    operator: Required[
        Literal[
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
    ]

    value: Required[Union[Optional[str], float, bool, Dict[str, object], Iterable[object]]]


class RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4(
    TypedDict, total=False
):
    clauses: Required[
        Iterable[
            RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4Clause
        ]
    ]

    logical_operator: Required[Literal["AND", "OR"]]


RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3Clause: TypeAlias = Union[
    RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipBaseCondition,
    RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3ClauseFlagshipLogicalCondition4,
]


class RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3(
    TypedDict, total=False
):
    clauses: Required[
        Iterable[
            RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3Clause
        ]
    ]

    logical_operator: Required[Literal["AND", "OR"]]


RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2Clause: TypeAlias = Union[
    RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipBaseCondition,
    RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2ClauseFlagshipLogicalCondition3,
]


class RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2(
    TypedDict, total=False
):
    clauses: Required[
        Iterable[
            RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2Clause
        ]
    ]

    logical_operator: Required[Literal["AND", "OR"]]


RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1Clause: TypeAlias = Union[
    RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipBaseCondition,
    RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1ClauseFlagshipLogicalCondition2,
]


class RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1(TypedDict, total=False):
    clauses: Required[Iterable[RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1Clause]]

    logical_operator: Required[Literal["AND", "OR"]]


RuleConditionFlagshipLogicalConditionClause: TypeAlias = Union[
    RuleConditionFlagshipLogicalConditionClauseFlagshipBaseCondition,
    RuleConditionFlagshipLogicalConditionClauseFlagshipLogicalCondition1,
]


class RuleConditionFlagshipLogicalCondition(TypedDict, total=False):
    clauses: Required[Iterable[RuleConditionFlagshipLogicalConditionClause]]

    logical_operator: Required[Literal["AND", "OR"]]


RuleCondition: TypeAlias = Union[RuleConditionFlagshipBaseCondition, RuleConditionFlagshipLogicalCondition]


class RuleRollout(TypedDict, total=False):
    percentage: Required[float]
    """
    Percentage of matching traffic (0–100, up to 2 decimal places) served this
    variation. For multi-way splits, use cumulative upper bounds across rules (e.g.
    30, 70, 100).
    """

    attribute: str
    """Context attribute used for sticky bucketing.

    Defaults to `targetingKey`. If absent at evaluation time, bucketing is random
    per request.
    """


class Rule(TypedDict, total=False):
    conditions: Required[Iterable[RuleCondition]]
    """Conditions the context must satisfy for this rule to match.

    An empty array matches all contexts.
    """

    priority: Required[int]
    """Evaluation order: the API evaluates rules with lower numbers first.

    Must be unique across the flag's rules.
    """

    serve_variation: Required[str]
    """Variation the API serves when this rule matches. Must be a key in `variations`."""

    rollout: RuleRollout
