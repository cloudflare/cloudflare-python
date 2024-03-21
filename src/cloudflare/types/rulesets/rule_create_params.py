# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "RuleCreateParams",
    "RulesetsBlockRule",
    "RulesetsBlockRuleActionParameters",
    "RulesetsBlockRuleActionParametersResponse",
    "RulesetsBlockRuleLogging",
    "RulesetsExecuteRule",
    "RulesetsExecuteRuleActionParameters",
    "RulesetsExecuteRuleActionParametersMatchedData",
    "RulesetsExecuteRuleActionParametersOverrides",
    "RulesetsExecuteRuleActionParametersOverridesCategory",
    "RulesetsExecuteRuleActionParametersOverridesRule",
    "RulesetsExecuteRuleLogging",
    "RulesetsLogRule",
    "RulesetsLogRuleLogging",
    "RulesetsSkipRule",
    "RulesetsSkipRuleActionParameters",
    "RulesetsSkipRuleLogging",
]


class RulesetsBlockRule(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["block"]
    """The action to perform when the rule matches."""

    action_parameters: RulesetsBlockRuleActionParameters
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: RulesetsBlockRuleLogging
    """An object configuring the rule's logging behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""


class RulesetsBlockRuleActionParametersResponse(TypedDict, total=False):
    content: Required[str]
    """The content to return."""

    content_type: Required[str]
    """The type of the content to return."""

    status_code: Required[int]
    """The status code to return."""


class RulesetsBlockRuleActionParameters(TypedDict, total=False):
    response: RulesetsBlockRuleActionParametersResponse
    """The response to show when the block is applied."""


class RulesetsBlockRuleLogging(TypedDict, total=False):
    enabled: Required[bool]
    """Whether to generate a log when the rule matches."""


class RulesetsExecuteRule(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["execute"]
    """The action to perform when the rule matches."""

    action_parameters: RulesetsExecuteRuleActionParameters
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: RulesetsExecuteRuleLogging
    """An object configuring the rule's logging behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""


class RulesetsExecuteRuleActionParametersMatchedData(TypedDict, total=False):
    public_key: Required[str]
    """The public key to encrypt matched data logs with."""


class RulesetsExecuteRuleActionParametersOverridesCategory(TypedDict, total=False):
    category: Required[str]
    """The name of the category to override."""

    action: str
    """The action to override rules in the category with."""

    enabled: bool
    """Whether to enable execution of rules in the category."""

    sensitivity_level: Literal["default", "medium", "low", "eoff"]
    """The sensitivity level to use for rules in the category."""


class RulesetsExecuteRuleActionParametersOverridesRule(TypedDict, total=False):
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


class RulesetsExecuteRuleActionParametersOverrides(TypedDict, total=False):
    action: str
    """An action to override all rules with.

    This option has lower precedence than rule and category overrides.
    """

    categories: Iterable[RulesetsExecuteRuleActionParametersOverridesCategory]
    """A list of category-level overrides.

    This option has the second-highest precedence after rule-level overrides.
    """

    enabled: bool
    """Whether to enable execution of all rules.

    This option has lower precedence than rule and category overrides.
    """

    rules: Iterable[RulesetsExecuteRuleActionParametersOverridesRule]
    """A list of rule-level overrides. This option has the highest precedence."""

    sensitivity_level: Literal["default", "medium", "low", "eoff"]
    """A sensitivity level to set for all rules.

    This option has lower precedence than rule and category overrides and is only
    applicable for DDoS phases.
    """


class RulesetsExecuteRuleActionParameters(TypedDict, total=False):
    id: Required[str]
    """The ID of the ruleset to execute."""

    matched_data: RulesetsExecuteRuleActionParametersMatchedData
    """The configuration to use for matched data logging."""

    overrides: RulesetsExecuteRuleActionParametersOverrides
    """A set of overrides to apply to the target ruleset."""


class RulesetsExecuteRuleLogging(TypedDict, total=False):
    enabled: Required[bool]
    """Whether to generate a log when the rule matches."""


class RulesetsLogRule(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["log"]
    """The action to perform when the rule matches."""

    action_parameters: object
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: RulesetsLogRuleLogging
    """An object configuring the rule's logging behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""


class RulesetsLogRuleLogging(TypedDict, total=False):
    enabled: Required[bool]
    """Whether to generate a log when the rule matches."""


class RulesetsSkipRule(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["skip"]
    """The action to perform when the rule matches."""

    action_parameters: RulesetsSkipRuleActionParameters
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: RulesetsSkipRuleLogging
    """An object configuring the rule's logging behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""


class RulesetsSkipRuleActionParameters(TypedDict, total=False):
    phases: List[
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
    """A list of phases to skip the execution of.

    This option is incompatible with the ruleset and rulesets options.
    """

    products: List[Literal["bic", "hot", "rateLimit", "securityLevel", "uaBlock", "waf", "zoneLockdown"]]
    """A list of legacy security products to skip the execution of."""

    rules: Dict[str, List[str]]
    """
    A mapping of ruleset IDs to a list of rule IDs in that ruleset to skip the
    execution of. This option is incompatible with the ruleset option.
    """

    ruleset: Literal["current"]
    """A ruleset to skip the execution of.

    This option is incompatible with the rulesets, rules and phases options.
    """

    rulesets: List[str]
    """A list of ruleset IDs to skip the execution of.

    This option is incompatible with the ruleset and phases options.
    """


class RulesetsSkipRuleLogging(TypedDict, total=False):
    enabled: Required[bool]
    """Whether to generate a log when the rule matches."""


RuleCreateParams = Union[RulesetsBlockRule, RulesetsExecuteRule, RulesetsLogRule, RulesetsSkipRule]
