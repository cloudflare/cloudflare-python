# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ...._types import SequenceNotStr

__all__ = [
    "FlagCreateParams",
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


class FlagCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID."""

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

    type: Literal["boolean", "string", "number", "json"]
    """Value type of the flag's variations.

    The API infers this from the variation values on write, so you can omit it in
    requests.
    """


class RuleConditionUnionMember0(TypedDict, total=False):
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
        ]
    ]

    value: Required[Union[Optional[str], float, bool, Dict[str, object], Iterable[object]]]


class RuleConditionUnionMember1ClauseUnionMember0(TypedDict, total=False):
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
        ]
    ]

    value: Required[Union[Optional[str], float, bool, Dict[str, object], Iterable[object]]]


class RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember0(TypedDict, total=False):
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
        ]
    ]

    value: Required[Union[Optional[str], float, bool, Dict[str, object], Iterable[object]]]


class RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0(TypedDict, total=False):
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
        ]
    ]

    value: Required[Union[Optional[str], float, bool, Dict[str, object], Iterable[object]]]


class RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0(
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
        ]
    ]

    value: Required[Union[Optional[str], float, bool, Dict[str, object], Iterable[object]]]


class RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0(
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
        ]
    ]

    value: Required[Union[Optional[str], float, bool, Dict[str, object], Iterable[object]]]


class RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1(
    TypedDict, total=False
):
    clauses: Required[SequenceNotStr[Union[Optional[str], float, bool, Dict[str, object], Iterable[object]]]]

    logical_operator: Required[Literal["AND", "OR"]]


RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause: TypeAlias = Union[
    RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0,
    RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1,
]


class RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1(
    TypedDict, total=False
):
    clauses: Required[
        Iterable[
            RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause
        ]
    ]

    logical_operator: Required[Literal["AND", "OR"]]


RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause: TypeAlias = Union[
    RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0,
    RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1,
]


class RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1(TypedDict, total=False):
    clauses: Required[Iterable[RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1Clause]]

    logical_operator: Required[Literal["AND", "OR"]]


RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1Clause: TypeAlias = Union[
    RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember0,
    RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1ClauseUnionMember1,
]


class RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1(TypedDict, total=False):
    clauses: Required[Iterable[RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1Clause]]

    logical_operator: Required[Literal["AND", "OR"]]


RuleConditionUnionMember1ClauseUnionMember1Clause: TypeAlias = Union[
    RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember0,
    RuleConditionUnionMember1ClauseUnionMember1ClauseUnionMember1,
]


class RuleConditionUnionMember1ClauseUnionMember1(TypedDict, total=False):
    clauses: Required[Iterable[RuleConditionUnionMember1ClauseUnionMember1Clause]]

    logical_operator: Required[Literal["AND", "OR"]]


RuleConditionUnionMember1Clause: TypeAlias = Union[
    RuleConditionUnionMember1ClauseUnionMember0, RuleConditionUnionMember1ClauseUnionMember1
]


class RuleConditionUnionMember1(TypedDict, total=False):
    clauses: Required[Iterable[RuleConditionUnionMember1Clause]]

    logical_operator: Required[Literal["AND", "OR"]]


RuleCondition: TypeAlias = Union[RuleConditionUnionMember0, RuleConditionUnionMember1]


class RuleRollout(TypedDict, total=False):
    percentage: Required[float]
    """Percentage of matching traffic (0–100) served this variation.

    For multi-way splits, use cumulative upper bounds across rules (e.g. 30, 70,
    100).
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
