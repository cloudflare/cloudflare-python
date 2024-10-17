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
    "ExposedCredentialCheck",
    "Ratelimit",
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


class ExposedCredentialCheck(BaseModel):
    password_expression: str
    """Expression that selects the password used in the credentials check."""

    username_expression: str
    """Expression that selects the user ID used in the credentials check."""


class Ratelimit(BaseModel):
    characteristics: List[str]
    """
    Characteristics of the request on which the ratelimiter counter will be
    incremented.
    """

    period: Literal[10, 60, 600, 3600]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: Optional[str] = None
    """Defines when the ratelimit counter should be incremented.

    It is optional and defaults to the same as the rule's expression.
    """

    mitigation_timeout: Optional[int] = None
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: Optional[int] = None
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: Optional[bool] = None
    """Defines if ratelimit counting is only done when an origin is reached."""

    score_per_period: Optional[int] = None
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: Optional[str] = None
    """
    The response header name provided by the origin which should contain the score
    to increment ratelimit counter on.
    """


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

    exposed_credential_check: Optional[ExposedCredentialCheck] = None
    """Configure checks for exposed credentials."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[Ratelimit] = None
    """An object configuring the rule's ratelimit behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule ID by default)."""
