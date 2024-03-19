# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "RulesetsRulesetResponse",
    "Rule",
    "RuleRulesetsBlockRule",
    "RuleRulesetsBlockRuleActionParameters",
    "RuleRulesetsBlockRuleActionParametersResponse",
    "RuleRulesetsBlockRuleLogging",
    "RuleRulesetsExecuteRule",
    "RuleRulesetsExecuteRuleActionParameters",
    "RuleRulesetsExecuteRuleActionParametersMatchedData",
    "RuleRulesetsExecuteRuleActionParametersOverrides",
    "RuleRulesetsExecuteRuleActionParametersOverridesCategory",
    "RuleRulesetsExecuteRuleActionParametersOverridesRule",
    "RuleRulesetsExecuteRuleLogging",
    "RuleRulesetsLogRule",
    "RuleRulesetsLogRuleLogging",
    "RuleRulesetsSkipRule",
    "RuleRulesetsSkipRuleActionParameters",
    "RuleRulesetsSkipRuleLogging",
]


class RuleRulesetsBlockRuleActionParametersResponse(BaseModel):
    content: str
    """The content to return."""

    content_type: str
    """The type of the content to return."""

    status_code: int
    """The status code to return."""


class RuleRulesetsBlockRuleActionParameters(BaseModel):
    response: Optional[RuleRulesetsBlockRuleActionParametersResponse] = None
    """The response to show when the block is applied."""


class RuleRulesetsBlockRuleLogging(BaseModel):
    enabled: bool
    """Whether to generate a log when the rule matches."""


class RuleRulesetsBlockRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["block"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[RuleRulesetsBlockRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    enabled: Optional[bool] = None
    """Whether the rule should be executed."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[RuleRulesetsBlockRuleLogging] = None
    """An object configuring the rule's logging behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule ID by default)."""


class RuleRulesetsExecuteRuleActionParametersMatchedData(BaseModel):
    public_key: str
    """The public key to encrypt matched data logs with."""


class RuleRulesetsExecuteRuleActionParametersOverridesCategory(BaseModel):
    category: str
    """The name of the category to override."""

    action: Optional[str] = None
    """The action to override rules in the category with."""

    enabled: Optional[bool] = None
    """Whether to enable execution of rules in the category."""

    sensitivity_level: Optional[Literal["default", "medium", "low", "eoff"]] = None
    """The sensitivity level to use for rules in the category."""


class RuleRulesetsExecuteRuleActionParametersOverridesRule(BaseModel):
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


class RuleRulesetsExecuteRuleActionParametersOverrides(BaseModel):
    action: Optional[str] = None
    """An action to override all rules with.

    This option has lower precedence than rule and category overrides.
    """

    categories: Optional[List[RuleRulesetsExecuteRuleActionParametersOverridesCategory]] = None
    """A list of category-level overrides.

    This option has the second-highest precedence after rule-level overrides.
    """

    enabled: Optional[bool] = None
    """Whether to enable execution of all rules.

    This option has lower precedence than rule and category overrides.
    """

    rules: Optional[List[RuleRulesetsExecuteRuleActionParametersOverridesRule]] = None
    """A list of rule-level overrides. This option has the highest precedence."""

    sensitivity_level: Optional[Literal["default", "medium", "low", "eoff"]] = None
    """A sensitivity level to set for all rules.

    This option has lower precedence than rule and category overrides and is only
    applicable for DDoS phases.
    """


class RuleRulesetsExecuteRuleActionParameters(BaseModel):
    id: str
    """The ID of the ruleset to execute."""

    matched_data: Optional[RuleRulesetsExecuteRuleActionParametersMatchedData] = None
    """The configuration to use for matched data logging."""

    overrides: Optional[RuleRulesetsExecuteRuleActionParametersOverrides] = None
    """A set of overrides to apply to the target ruleset."""


class RuleRulesetsExecuteRuleLogging(BaseModel):
    enabled: bool
    """Whether to generate a log when the rule matches."""


class RuleRulesetsExecuteRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["execute"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[RuleRulesetsExecuteRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    enabled: Optional[bool] = None
    """Whether the rule should be executed."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[RuleRulesetsExecuteRuleLogging] = None
    """An object configuring the rule's logging behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule ID by default)."""


class RuleRulesetsLogRuleLogging(BaseModel):
    enabled: bool
    """Whether to generate a log when the rule matches."""


class RuleRulesetsLogRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["log"]] = None
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

    logging: Optional[RuleRulesetsLogRuleLogging] = None
    """An object configuring the rule's logging behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule ID by default)."""


class RuleRulesetsSkipRuleActionParameters(BaseModel):
    phases: Optional[
        List[
            Literal[
                "ddos_l4",
                "ddos_l7",
                "http_config_settings",
                "http_custom_errors",
                "http_log_custom_fields",
                "http_ratelimit",
                "http_request_cache_settings",
                "http_request_dynamic_redirect",
                "http_request_firewall_custom",
                "http_request_firewall_managed",
                "http_request_late_transform",
                "http_request_origin",
                "http_request_redirect",
                "http_request_sanitize",
                "http_request_sbfm",
                "http_request_select_configuration",
                "http_request_transform",
                "http_response_compression",
                "http_response_firewall_managed",
                "http_response_headers_transform",
                "magic_transit",
                "magic_transit_ids_managed",
                "magic_transit_managed",
            ]
        ]
    ] = None
    """A list of phases to skip the execution of.

    This option is incompatible with the ruleset and rulesets options.
    """

    products: Optional[
        List[Literal["bic", "hot", "rateLimit", "securityLevel", "uaBlock", "waf", "zoneLockdown"]]
    ] = None
    """A list of legacy security products to skip the execution of."""

    rules: Optional[Dict[str, List[str]]] = None
    """
    A mapping of ruleset IDs to a list of rule IDs in that ruleset to skip the
    execution of. This option is incompatible with the ruleset option.
    """

    ruleset: Optional[Literal["current"]] = None
    """A ruleset to skip the execution of.

    This option is incompatible with the rulesets, rules and phases options.
    """

    rulesets: Optional[List[str]] = None
    """A list of ruleset IDs to skip the execution of.

    This option is incompatible with the ruleset and phases options.
    """


class RuleRulesetsSkipRuleLogging(BaseModel):
    enabled: bool
    """Whether to generate a log when the rule matches."""


class RuleRulesetsSkipRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["skip"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[RuleRulesetsSkipRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    enabled: Optional[bool] = None
    """Whether the rule should be executed."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[RuleRulesetsSkipRuleLogging] = None
    """An object configuring the rule's logging behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule ID by default)."""


Rule = Union[RuleRulesetsBlockRule, RuleRulesetsExecuteRule, RuleRulesetsLogRule, RuleRulesetsSkipRule]


class RulesetsRulesetResponse(BaseModel):
    id: str
    """The unique ID of the ruleset."""

    kind: Literal["managed", "custom", "root", "zone"]
    """The kind of the ruleset."""

    last_updated: datetime
    """The timestamp of when the ruleset was last modified."""

    name: str
    """The human-readable name of the ruleset."""

    phase: Literal[
        "ddos_l4",
        "ddos_l7",
        "http_config_settings",
        "http_custom_errors",
        "http_log_custom_fields",
        "http_ratelimit",
        "http_request_cache_settings",
        "http_request_dynamic_redirect",
        "http_request_firewall_custom",
        "http_request_firewall_managed",
        "http_request_late_transform",
        "http_request_origin",
        "http_request_redirect",
        "http_request_sanitize",
        "http_request_sbfm",
        "http_request_select_configuration",
        "http_request_transform",
        "http_response_compression",
        "http_response_firewall_managed",
        "http_response_headers_transform",
        "magic_transit",
        "magic_transit_ids_managed",
        "magic_transit_managed",
    ]
    """The phase of the ruleset."""

    rules: List[Rule]
    """The list of rules in the ruleset."""

    version: str
    """The version of the ruleset."""

    description: Optional[str] = None
    """An informative description of the ruleset."""
