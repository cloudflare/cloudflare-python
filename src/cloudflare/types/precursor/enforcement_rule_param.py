# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["EnforcementRuleParam"]


class EnforcementRuleParam(TypedDict, total=False):
    expression: Required[str]
    """The filter expression that determines which requests the rule matches."""

    mode: Required[Literal["min-friction", "max-security"]]
    """The override mode Precursor applies to requests matching an enforcement rule.

    Unlike `default_mode`, this cannot be `off`.
    """

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule is active."""
