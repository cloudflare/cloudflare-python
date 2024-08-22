# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal, TypeAlias

from .kind import Kind

from .phase import Phase

from typing import Iterable, Union

from .logging_param import LoggingParam

from .block_rule_param import BlockRuleParam

from .compress_response_rule_param import CompressResponseRuleParam

from .execute_rule_param import ExecuteRuleParam

from .log_rule_param import LogRuleParam

from .managed_challenge_rule_param import ManagedChallengeRuleParam

from .redirect_rule_param import RedirectRuleParam

from .rewrite_rule_param import RewriteRuleParam

from .route_rule_param import RouteRuleParam

from .score_rule_param import ScoreRuleParam

from .serve_error_rule_param import ServeErrorRuleParam

from .set_config_rule_param import SetConfigRuleParam

from .skip_rule_param import SkipRuleParam

from .set_cache_settings_rule_param import SetCacheSettingsRuleParam

from .log_custom_field_rule_param import LogCustomFieldRuleParam

from .ddos_dynamic_rule_param import DDoSDynamicRuleParam

from .force_connection_close_rule_param import ForceConnectionCloseRuleParam

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["RulesetCreateParams", "Rule", "RuleRulesetsChallengeRule", "RuleRulesetsJSChallengeRule"]

class RulesetCreateParams(TypedDict, total=False):
    kind: Required[Kind]
    """The kind of the ruleset."""

    name: Required[str]
    """The human-readable name of the ruleset."""

    phase: Required[Phase]
    """The phase of the ruleset."""

    rules: Required[Iterable[Rule]]
    """The list of rules in the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    description: str
    """An informative description of the ruleset."""

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

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""

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

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""

Rule: TypeAlias = Union[BlockRuleParam, RuleRulesetsChallengeRule, CompressResponseRuleParam, ExecuteRuleParam, RuleRulesetsJSChallengeRule, LogRuleParam, ManagedChallengeRuleParam, RedirectRuleParam, RewriteRuleParam, RouteRuleParam, ScoreRuleParam, ServeErrorRuleParam, SetConfigRuleParam, SkipRuleParam, SetCacheSettingsRuleParam, LogCustomFieldRuleParam, DDoSDynamicRuleParam, ForceConnectionCloseRuleParam]