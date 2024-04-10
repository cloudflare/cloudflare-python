# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .logging import Logging
from ..._models import BaseModel

__all__ = [
    "ExecuteRule",
    "ActionParameters",
    "ActionParametersMatchedData",
    "ActionParametersOverrides",
    "ActionParametersOverridesCategory",
    "ActionParametersOverridesRule",
]


class ActionParametersMatchedData(BaseModel):
    public_key: str
    """The public key to encrypt matched data logs with."""


class ActionParametersOverridesCategory(BaseModel):
    category: str
    """The name of the category to override."""

    action: Optional[str] = None
    """The action to override rules in the category with."""

    enabled: Optional[bool] = None
    """Whether to enable execution of rules in the category."""

    sensitivity_level: Optional[Literal["default", "medium", "low", "eoff"]] = None
    """The sensitivity level to use for rules in the category."""


class ActionParametersOverridesRule(BaseModel):
    id: str
    """The ID of the rule to override."""

    action: Optional[str] = None
    """The action to override the rule with."""

    enabled: Optional[bool] = None
    """Whether to enable execution of the rule."""

    score_threshold: Optional[int] = None
    """The score threshold to use for the rule."""

    sensitivity_level: Optional[Literal["default", "medium", "low", "eoff"]] = None
    """The sensitivity level to use for the rule."""


class ActionParametersOverrides(BaseModel):
    action: Optional[str] = None
    """An action to override all rules with.

    This option has lower precedence than rule and category overrides.
    """

    categories: Optional[List[ActionParametersOverridesCategory]] = None
    """A list of category-level overrides.

    This option has the second-highest precedence after rule-level overrides.
    """

    enabled: Optional[bool] = None
    """Whether to enable execution of all rules.

    This option has lower precedence than rule and category overrides.
    """

    rules: Optional[List[ActionParametersOverridesRule]] = None
    """A list of rule-level overrides. This option has the highest precedence."""

    sensitivity_level: Optional[Literal["default", "medium", "low", "eoff"]] = None
    """A sensitivity level to set for all rules.

    This option has lower precedence than rule and category overrides and is only
    applicable for DDoS phases.
    """


class ActionParameters(BaseModel):
    id: str
    """The ID of the ruleset to execute."""

    matched_data: Optional[ActionParametersMatchedData] = None
    """The configuration to use for matched data logging."""

    overrides: Optional[ActionParametersOverrides] = None
    """A set of overrides to apply to the target ruleset."""


class ExecuteRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["execute"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[ActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    enabled: Optional[bool] = None
    """Whether the rule should be executed."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule ID by default)."""
