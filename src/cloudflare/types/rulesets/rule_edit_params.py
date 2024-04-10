# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .logging_param import LoggingParam

__all__ = [
    "RuleEditParams",
    "BlockRule",
    "BlockRuleActionParameters",
    "BlockRuleActionParametersResponse",
    "ExecuteRule",
    "ExecuteRuleActionParameters",
    "ExecuteRuleActionParametersMatchedData",
    "ExecuteRuleActionParametersOverrides",
    "ExecuteRuleActionParametersOverridesCategory",
    "ExecuteRuleActionParametersOverridesRule",
    "LogRule",
    "SkipRule",
    "SkipRuleActionParameters",
]


class BlockRule(TypedDict, total=False):
    ruleset_id: Required[str]
    """The unique ID of the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["block"]
    """The action to perform when the rule matches."""

    action_parameters: BlockRuleActionParameters
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


class BlockRuleActionParametersResponse(TypedDict, total=False):
    content: Required[str]
    """The content to return."""

    content_type: Required[str]
    """The type of the content to return."""

    status_code: Required[int]
    """The status code to return."""


class BlockRuleActionParameters(TypedDict, total=False):
    response: BlockRuleActionParametersResponse
    """The response to show when the block is applied."""


class ExecuteRule(TypedDict, total=False):
    ruleset_id: Required[str]
    """The unique ID of the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["execute"]
    """The action to perform when the rule matches."""

    action_parameters: ExecuteRuleActionParameters
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


class ExecuteRuleActionParametersMatchedData(TypedDict, total=False):
    public_key: Required[str]
    """The public key to encrypt matched data logs with."""


class ExecuteRuleActionParametersOverridesCategory(TypedDict, total=False):
    category: Required[str]
    """The name of the category to override."""

    action: str
    """The action to override rules in the category with."""

    enabled: bool
    """Whether to enable execution of rules in the category."""

    sensitivity_level: Literal["default", "medium", "low", "eoff"]
    """The sensitivity level to use for rules in the category."""


class ExecuteRuleActionParametersOverridesRule(TypedDict, total=False):
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


class ExecuteRuleActionParametersOverrides(TypedDict, total=False):
    action: str
    """An action to override all rules with.

    This option has lower precedence than rule and category overrides.
    """

    categories: Iterable[ExecuteRuleActionParametersOverridesCategory]
    """A list of category-level overrides.

    This option has the second-highest precedence after rule-level overrides.
    """

    enabled: bool
    """Whether to enable execution of all rules.

    This option has lower precedence than rule and category overrides.
    """

    rules: Iterable[ExecuteRuleActionParametersOverridesRule]
    """A list of rule-level overrides. This option has the highest precedence."""

    sensitivity_level: Literal["default", "medium", "low", "eoff"]
    """A sensitivity level to set for all rules.

    This option has lower precedence than rule and category overrides and is only
    applicable for DDoS phases.
    """


class ExecuteRuleActionParameters(TypedDict, total=False):
    id: Required[str]
    """The ID of the ruleset to execute."""

    matched_data: ExecuteRuleActionParametersMatchedData
    """The configuration to use for matched data logging."""

    overrides: ExecuteRuleActionParametersOverrides
    """A set of overrides to apply to the target ruleset."""


class LogRule(TypedDict, total=False):
    ruleset_id: Required[str]
    """The unique ID of the ruleset."""

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

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""


class SkipRule(TypedDict, total=False):
    ruleset_id: Required[str]
    """The unique ID of the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["skip"]
    """The action to perform when the rule matches."""

    action_parameters: SkipRuleActionParameters
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


class SkipRuleActionParameters(TypedDict, total=False):
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


RuleEditParams = Union[BlockRule, ExecuteRule, LogRule, SkipRule]
