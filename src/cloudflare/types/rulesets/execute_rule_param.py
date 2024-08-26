# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict, Required

from .logging_param import LoggingParam

from typing import Iterable

__all__ = ["ExecuteRuleParam", "ActionParameters", "ActionParametersMatchedData", "ActionParametersOverrides", "ActionParametersOverridesCategory", "ActionParametersOverridesRule"]

class ActionParametersMatchedData(TypedDict, total=False):
    public_key: Required[str]
    """The public key to encrypt matched data logs with."""

class ActionParametersOverridesCategory(TypedDict, total=False):
    category: Required[str]
    """The name of the category to override."""

    action: str
    """The action to override rules in the category with."""

    enabled: bool
    """Whether to enable execution of rules in the category."""

    sensitivity_level: Literal["default", "medium", "low", "eoff"]
    """The sensitivity level to use for rules in the category."""

class ActionParametersOverridesRule(TypedDict, total=False):
    id: Required[str]
    """The ID of the rule to override."""

    action: str
    """The action to override the rule with."""

    enabled: bool
    """Whether to enable execution of the rule."""

    score_threshold: int
    """The score threshold to use for the rule."""

    sensitivity_level: Literal["default", "medium", "low", "eoff"]
    """The sensitivity level to use for the rule."""

class ActionParametersOverrides(TypedDict, total=False):
    action: str
    """An action to override all rules with.

    This option has lower precedence than rule and category overrides.
    """

    categories: Iterable[ActionParametersOverridesCategory]
    """A list of category-level overrides.

    This option has the second-highest precedence after rule-level overrides.
    """

    enabled: bool
    """Whether to enable execution of all rules.

    This option has lower precedence than rule and category overrides.
    """

    rules: Iterable[ActionParametersOverridesRule]
    """A list of rule-level overrides. This option has the highest precedence."""

    sensitivity_level: Literal["default", "medium", "low", "eoff"]
    """A sensitivity level to set for all rules.

    This option has lower precedence than rule and category overrides and is only
    applicable for DDoS phases.
    """

class ActionParameters(TypedDict, total=False):
    id: Required[str]
    """The ID of the ruleset to execute."""

    matched_data: ActionParametersMatchedData
    """The configuration to use for matched data logging."""

    overrides: ActionParametersOverrides
    """A set of overrides to apply to the target ruleset."""

class ExecuteRuleParam(TypedDict, total=False):
    id: str
    """The unique ID of the rule."""

    action: Literal["execute"]
    """The action to perform when the rule matches."""

    action_parameters: ActionParameters
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""