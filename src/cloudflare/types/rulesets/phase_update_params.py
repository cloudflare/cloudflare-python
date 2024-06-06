# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .logging_param import LoggingParam
from .log_rule_param import LogRuleParam
from .skip_rule_param import SkipRuleParam
from .block_rule_param import BlockRuleParam
from .route_rule_param import RouteRuleParam
from .score_rule_param import ScoreRuleParam
from .execute_rule_param import ExecuteRuleParam
from .rewrite_rule_param import RewriteRuleParam
from .redirect_rule_param import RedirectRuleParam
from .challenge_rule_param import ChallengeRuleParam
from .set_config_rule_param import SetConfigRuleParam
from .serve_error_rule_param import ServeErrorRuleParam
from .js_challenge_rule_param import JSChallengeRuleParam
from .compress_response_rule_param import CompressResponseRuleParam
from .managed_challenge_rule_param import ManagedChallengeRuleParam
from .set_cache_settings_rule_param import SetCacheSettingsRuleParam

__all__ = [
    "PhaseUpdateParams",
    "Rule",
    "RuleRulesetsLogCustomFieldRule",
    "RuleRulesetsLogCustomFieldRuleActionParameters",
    "RuleRulesetsLogCustomFieldRuleActionParametersCookieField",
    "RuleRulesetsLogCustomFieldRuleActionParametersRequestField",
    "RuleRulesetsLogCustomFieldRuleActionParametersResponseField",
    "RuleRulesetsDDoSDynamicRule",
    "RuleRulesetsForceConnectionCloseRule",
]


class PhaseUpdateParams(TypedDict, total=False):
    rules: Required[Iterable[Rule]]
    """The list of rules in the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    description: str
    """An informative description of the ruleset."""

    name: str
    """The human-readable name of the ruleset."""


class RuleRulesetsLogCustomFieldRuleActionParametersCookieField(TypedDict, total=False):
    name: Required[str]
    """The name of the field."""


class RuleRulesetsLogCustomFieldRuleActionParametersRequestField(TypedDict, total=False):
    name: Required[str]
    """The name of the field."""


class RuleRulesetsLogCustomFieldRuleActionParametersResponseField(TypedDict, total=False):
    name: Required[str]
    """The name of the field."""


class RuleRulesetsLogCustomFieldRuleActionParameters(TypedDict, total=False):
    cookie_fields: Iterable[RuleRulesetsLogCustomFieldRuleActionParametersCookieField]
    """The cookie fields to log."""

    request_fields: Iterable[RuleRulesetsLogCustomFieldRuleActionParametersRequestField]
    """The request fields to log."""

    response_fields: Iterable[RuleRulesetsLogCustomFieldRuleActionParametersResponseField]
    """The response fields to log."""


class RuleRulesetsLogCustomFieldRule(TypedDict, total=False):
    id: str
    """The unique ID of the rule."""

    action: Literal["log_custom_field"]
    """The action to perform when the rule matches."""

    action_parameters: RuleRulesetsLogCustomFieldRuleActionParameters
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


class RuleRulesetsDDoSDynamicRule(TypedDict, total=False):
    id: str
    """The unique ID of the rule."""

    action: Literal["ddos_dynamic"]
    """The action to perform when the rule matches."""

    action_parameters: object
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


class RuleRulesetsForceConnectionCloseRule(TypedDict, total=False):
    id: str
    """The unique ID of the rule."""

    action: Literal["force_connection_close"]
    """The action to perform when the rule matches."""

    action_parameters: object
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


Rule = Union[
    BlockRuleParam,
    ChallengeRuleParam,
    CompressResponseRuleParam,
    ExecuteRuleParam,
    JSChallengeRuleParam,
    LogRuleParam,
    ManagedChallengeRuleParam,
    RedirectRuleParam,
    RewriteRuleParam,
    RouteRuleParam,
    ScoreRuleParam,
    ServeErrorRuleParam,
    SetConfigRuleParam,
    SkipRuleParam,
    SetCacheSettingsRuleParam,
    RuleRulesetsLogCustomFieldRule,
    RuleRulesetsDDoSDynamicRule,
    RuleRulesetsForceConnectionCloseRule,
]
