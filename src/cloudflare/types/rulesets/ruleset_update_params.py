# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .kind import Kind
from .phase import Phase
from .logging_param import LoggingParam
from .log_rule_param import LogRuleParam
from .skip_rule_param import SkipRuleParam
from .block_rule_param import BlockRuleParam
from .route_rule_param import RouteRuleParam
from .score_rule_param import ScoreRuleParam
from .execute_rule_param import ExecuteRuleParam
from .rewrite_rule_param import RewriteRuleParam
from .redirect_rule_param import RedirectRuleParam
from .set_config_rule_param import SetConfigRuleParam
from .serve_error_rule_param import ServeErrorRuleParam
from .ddos_dynamic_rule_param import DDoSDynamicRuleParam
from .log_custom_field_rule_param import LogCustomFieldRuleParam
from .compress_response_rule_param import CompressResponseRuleParam
from .managed_challenge_rule_param import ManagedChallengeRuleParam
from .set_cache_settings_rule_param import SetCacheSettingsRuleParam
from .force_connection_close_rule_param import ForceConnectionCloseRuleParam

__all__ = [
    "RulesetUpdateParams",
    "Rule",
    "RuleRulesetsChallengeRule",
    "RuleRulesetsChallengeRuleExposedCredentialCheck",
    "RuleRulesetsChallengeRuleRatelimit",
    "RuleRulesetsJSChallengeRule",
    "RuleRulesetsJSChallengeRuleExposedCredentialCheck",
    "RuleRulesetsJSChallengeRuleRatelimit",
]


class RulesetUpdateParams(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    description: str
    """An informative description of the ruleset."""

    kind: Kind
    """The kind of the ruleset."""

    name: str
    """The human-readable name of the ruleset."""

    phase: Phase
    """The phase of the ruleset."""

    rules: Iterable[Rule]
    """The list of rules in the ruleset."""


class RuleRulesetsChallengeRuleExposedCredentialCheck(TypedDict, total=False):
    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class RuleRulesetsChallengeRuleRatelimit(TypedDict, total=False):
    characteristics: Required[List[str]]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: Required[int]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
    """

    mitigation_timeout: int
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: int
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: bool
    """Whether counting is only performed when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class RuleRulesetsChallengeRule(TypedDict, total=False):
    id: str
    """The unique ID of the rule."""

    action: Literal["challenge"]
    """The action to perform when the rule matches."""

    action_parameters: object
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: RuleRulesetsChallengeRuleExposedCredentialCheck
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    ratelimit: RuleRulesetsChallengeRuleRatelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""


class RuleRulesetsJSChallengeRuleExposedCredentialCheck(TypedDict, total=False):
    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class RuleRulesetsJSChallengeRuleRatelimit(TypedDict, total=False):
    characteristics: Required[List[str]]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: Required[int]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
    """

    mitigation_timeout: int
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: int
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: bool
    """Whether counting is only performed when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class RuleRulesetsJSChallengeRule(TypedDict, total=False):
    id: str
    """The unique ID of the rule."""

    action: Literal["js_challenge"]
    """The action to perform when the rule matches."""

    action_parameters: object
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: RuleRulesetsJSChallengeRuleExposedCredentialCheck
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    ratelimit: RuleRulesetsJSChallengeRuleRatelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""


Rule: TypeAlias = Union[
    BlockRuleParam,
    RuleRulesetsChallengeRule,
    CompressResponseRuleParam,
    DDoSDynamicRuleParam,
    ExecuteRuleParam,
    ForceConnectionCloseRuleParam,
    RuleRulesetsJSChallengeRule,
    LogRuleParam,
    LogCustomFieldRuleParam,
    ManagedChallengeRuleParam,
    RedirectRuleParam,
    RewriteRuleParam,
    RouteRuleParam,
    ScoreRuleParam,
    ServeErrorRuleParam,
    SetCacheSettingsRuleParam,
    SetConfigRuleParam,
    SkipRuleParam,
]
