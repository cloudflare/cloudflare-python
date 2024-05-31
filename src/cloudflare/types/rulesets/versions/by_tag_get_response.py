# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated

from ..kind import Kind
from ..phase import Phase
from ..logging import Logging
from ...._utils import PropertyInfo
from ..log_rule import LogRule
from ...._models import BaseModel
from ..skip_rule import SkipRule
from ..block_rule import BlockRule
from ..route_rule import RouteRule
from ..score_rule import ScoreRule
from ..execute_rule import ExecuteRule
from ..rewrite_rule import RewriteRule
from ..redirect_rule import RedirectRule
from ..challenge_rule import ChallengeRule
from ..set_config_rule import SetConfigRule
from ..serve_error_rule import ServeErrorRule
from ..js_challenge_rule import JSChallengeRule
from ..compress_response_rule import CompressResponseRule
from ..managed_challenge_rule import ManagedChallengeRule
from ..set_cache_settings_rule import SetCacheSettingsRule

__all__ = [
    "ByTagGetResponse",
    "Rule",
    "RuleRulesetsLogCustomFieldRule",
    "RuleRulesetsLogCustomFieldRuleActionParameters",
    "RuleRulesetsLogCustomFieldRuleActionParametersCookieField",
    "RuleRulesetsLogCustomFieldRuleActionParametersRequestField",
    "RuleRulesetsLogCustomFieldRuleActionParametersResponseField",
    "RuleRulesetsDDoSDynamicRule",
    "RuleRulesetsForceConnectionCloseRule",
]


class RuleRulesetsLogCustomFieldRuleActionParametersCookieField(BaseModel):
    name: str
    """The name of the field."""


class RuleRulesetsLogCustomFieldRuleActionParametersRequestField(BaseModel):
    name: str
    """The name of the field."""


class RuleRulesetsLogCustomFieldRuleActionParametersResponseField(BaseModel):
    name: str
    """The name of the field."""


class RuleRulesetsLogCustomFieldRuleActionParameters(BaseModel):
    cookie_fields: Optional[List[RuleRulesetsLogCustomFieldRuleActionParametersCookieField]] = None
    """The cookie fields to log."""

    request_fields: Optional[List[RuleRulesetsLogCustomFieldRuleActionParametersRequestField]] = None
    """The request fields to log."""

    response_fields: Optional[List[RuleRulesetsLogCustomFieldRuleActionParametersResponseField]] = None
    """The response fields to log."""


class RuleRulesetsLogCustomFieldRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["log_custom_field"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[RuleRulesetsLogCustomFieldRuleActionParameters] = None
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


class RuleRulesetsDDoSDynamicRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["ddos_dynamic"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[object] = None
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


class RuleRulesetsForceConnectionCloseRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["force_connection_close"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[object] = None
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


Rule = Annotated[
    Union[
        BlockRule,
        ChallengeRule,
        CompressResponseRule,
        ExecuteRule,
        JSChallengeRule,
        LogRule,
        ManagedChallengeRule,
        RedirectRule,
        RewriteRule,
        RouteRule,
        ScoreRule,
        ServeErrorRule,
        SetConfigRule,
        SkipRule,
        SetCacheSettingsRule,
        RuleRulesetsLogCustomFieldRule,
        RuleRulesetsDDoSDynamicRule,
        RuleRulesetsForceConnectionCloseRule,
    ],
    PropertyInfo(discriminator="action"),
]


class ByTagGetResponse(BaseModel):
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
