# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .kind import Kind
from .phase import Phase
from .logging import Logging
from ..._utils import PropertyInfo
from .log_rule import LogRule
from ..._models import BaseModel
from .skip_rule import SkipRule
from .block_rule import BlockRule
from .route_rule import RouteRule
from .score_rule import ScoreRule
from .execute_rule import ExecuteRule
from .rewrite_rule import RewriteRule
from .redirect_rule import RedirectRule
from .set_config_rule import SetConfigRule
from .serve_error_rule import ServeErrorRule
from .ddos_dynamic_rule import DDoSDynamicRule
from .log_custom_field_rule import LogCustomFieldRule
from .compress_response_rule import CompressResponseRule
from .managed_challenge_rule import ManagedChallengeRule
from .set_cache_settings_rule import SetCacheSettingsRule
from .force_connection_close_rule import ForceConnectionCloseRule

__all__ = [
    "RulesetCreateResponse",
    "Rule",
    "RuleRulesetsChallengeRule",
    "RuleRulesetsChallengeRuleExposedCredentialCheck",
    "RuleRulesetsChallengeRuleRatelimit",
    "RuleRulesetsJSChallengeRule",
    "RuleRulesetsJSChallengeRuleExposedCredentialCheck",
    "RuleRulesetsJSChallengeRuleRatelimit",
]


class RuleRulesetsChallengeRuleExposedCredentialCheck(BaseModel):
    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class RuleRulesetsChallengeRuleRatelimit(BaseModel):
    characteristics: List[str]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: int
    """Period in seconds over which the counter is being incremented."""

    counting_expression: Optional[str] = None
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
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
    """Whether counting is only performed when an origin is reached."""

    score_per_period: Optional[int] = None
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: Optional[str] = None
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class RuleRulesetsChallengeRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["challenge"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[object] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    enabled: Optional[bool] = None
    """Whether the rule should be executed."""

    exposed_credential_check: Optional[RuleRulesetsChallengeRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[RuleRulesetsChallengeRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule's ID by default)."""


class RuleRulesetsJSChallengeRuleExposedCredentialCheck(BaseModel):
    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class RuleRulesetsJSChallengeRuleRatelimit(BaseModel):
    characteristics: List[str]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: int
    """Period in seconds over which the counter is being incremented."""

    counting_expression: Optional[str] = None
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
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
    """Whether counting is only performed when an origin is reached."""

    score_per_period: Optional[int] = None
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: Optional[str] = None
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class RuleRulesetsJSChallengeRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["js_challenge"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[object] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    enabled: Optional[bool] = None
    """Whether the rule should be executed."""

    exposed_credential_check: Optional[RuleRulesetsJSChallengeRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[RuleRulesetsJSChallengeRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule's ID by default)."""


Rule: TypeAlias = Annotated[
    Union[
        BlockRule,
        RuleRulesetsChallengeRule,
        CompressResponseRule,
        DDoSDynamicRule,
        ExecuteRule,
        ForceConnectionCloseRule,
        RuleRulesetsJSChallengeRule,
        LogRule,
        LogCustomFieldRule,
        ManagedChallengeRule,
        RedirectRule,
        RewriteRule,
        RouteRule,
        ScoreRule,
        ServeErrorRule,
        SetCacheSettingsRule,
        SetConfigRule,
        SkipRule,
    ],
    PropertyInfo(discriminator="action"),
]


class RulesetCreateResponse(BaseModel):
    id: str
    """The unique ID of the ruleset."""

    kind: Kind
    """The kind of the ruleset."""

    last_updated: datetime
    """The timestamp of when the ruleset was last modified."""

    name: str
    """The human-readable name of the ruleset."""

    phase: Phase
    """The phase of the ruleset."""

    rules: List[Rule]
    """The list of rules in the ruleset."""

    version: str
    """The version of the ruleset."""

    description: Optional[str] = None
    """An informative description of the ruleset."""
