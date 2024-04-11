# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .logging_param import LoggingParam

__all__ = [
    "RuleCreateParams",
    "BlockRule",
    "BlockRuleActionParameters",
    "BlockRuleActionParametersResponse",
    "RulesetsChallengeRule",
    "RulesetsCompressResponseRule",
    "RulesetsCompressResponseRuleActionParameters",
    "RulesetsCompressResponseRuleActionParametersAlgorithm",
    "ExecuteRule",
    "ExecuteRuleActionParameters",
    "ExecuteRuleActionParametersMatchedData",
    "ExecuteRuleActionParametersOverrides",
    "ExecuteRuleActionParametersOverridesCategory",
    "ExecuteRuleActionParametersOverridesRule",
    "RulesetsJsChallengeRule",
    "LogRule",
    "RulesetsManagedChallengeRule",
    "RulesetsRedirectRule",
    "RulesetsRedirectRuleActionParameters",
    "RulesetsRedirectRuleActionParametersFromList",
    "RulesetsRedirectRuleActionParametersFromValue",
    "RulesetsRedirectRuleActionParametersFromValueTargetURL",
    "RulesetsRedirectRuleActionParametersFromValueTargetURLStaticURLRedirect",
    "RulesetsRedirectRuleActionParametersFromValueTargetURLDynamicURLRedirect",
    "RulesetsRewriteRule",
    "RulesetsRewriteRuleActionParameters",
    "RulesetsRewriteRuleActionParametersHeaders",
    "RulesetsRewriteRuleActionParametersHeadersRemoveHeader",
    "RulesetsRewriteRuleActionParametersHeadersStaticHeader",
    "RulesetsRewriteRuleActionParametersHeadersDynamicHeader",
    "RulesetsRewriteRuleActionParametersURI",
    "RulesetsRewriteRuleActionParametersURIPath",
    "RulesetsRewriteRuleActionParametersURIPathStaticValue",
    "RulesetsRewriteRuleActionParametersURIPathDynamicValue",
    "RulesetsRewriteRuleActionParametersURIQuery",
    "RulesetsRewriteRuleActionParametersURIQueryStaticValue",
    "RulesetsRewriteRuleActionParametersURIQueryDynamicValue",
    "RulesetsRouteRule",
    "RulesetsRouteRuleActionParameters",
    "RulesetsRouteRuleActionParametersOrigin",
    "RulesetsRouteRuleActionParametersSni",
    "RulesetsScoreRule",
    "RulesetsScoreRuleActionParameters",
    "RulesetsServeErrorRule",
    "RulesetsServeErrorRuleActionParameters",
    "RulesetsSetConfigRule",
    "RulesetsSetConfigRuleActionParameters",
    "RulesetsSetConfigRuleActionParametersAutominify",
    "SkipRule",
    "SkipRuleActionParameters",
    "RulesetsSetCacheSettingsRule",
    "RulesetsSetCacheSettingsRuleActionParameters",
    "RulesetsSetCacheSettingsRuleActionParametersBrowserTTL",
    "RulesetsSetCacheSettingsRuleActionParametersCacheKey",
    "RulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKey",
    "RulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyCookie",
    "RulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyHeader",
    "RulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyHost",
    "RulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryString",
    "RulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringExclude",
    "RulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringInclude",
    "RulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyUser",
    "RulesetsSetCacheSettingsRuleActionParametersCacheReserve",
    "RulesetsSetCacheSettingsRuleActionParametersEdgeTTL",
    "RulesetsSetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTL",
    "RulesetsSetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTLStatusCodeRange",
    "RulesetsSetCacheSettingsRuleActionParametersServeStale",
]


class BlockRule(TypedDict, total=False):
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


class RulesetsChallengeRule(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

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


class RulesetsCompressResponseRule(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["compress_response"]
    """The action to perform when the rule matches."""

    action_parameters: RulesetsCompressResponseRuleActionParameters
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


class RulesetsCompressResponseRuleActionParametersAlgorithm(TypedDict, total=False):
    name: Literal["none", "auto", "default", "gzip", "brotli"]
    """Name of compression algorithm to enable."""


class RulesetsCompressResponseRuleActionParameters(TypedDict, total=False):
    algorithms: Iterable[RulesetsCompressResponseRuleActionParametersAlgorithm]
    """Custom order for compression algorithms."""


class ExecuteRule(TypedDict, total=False):
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


class RulesetsJsChallengeRule(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

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


class LogRule(TypedDict, total=False):
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


class RulesetsManagedChallengeRule(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["managed_challenge"]
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


class RulesetsRedirectRule(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["redirect"]
    """The action to perform when the rule matches."""

    action_parameters: RulesetsRedirectRuleActionParameters
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


class RulesetsRedirectRuleActionParametersFromList(TypedDict, total=False):
    key: str
    """Expression that evaluates to the list lookup key."""

    name: str
    """The name of the list to match against."""


class RulesetsRedirectRuleActionParametersFromValueTargetURLStaticURLRedirect(TypedDict, total=False):
    value: str
    """The URL to redirect the request to."""


class RulesetsRedirectRuleActionParametersFromValueTargetURLDynamicURLRedirect(TypedDict, total=False):
    expression: str
    """An expression to evaluate to get the URL to redirect the request to."""


RulesetsRedirectRuleActionParametersFromValueTargetURL = Union[
    RulesetsRedirectRuleActionParametersFromValueTargetURLStaticURLRedirect,
    RulesetsRedirectRuleActionParametersFromValueTargetURLDynamicURLRedirect,
]


class RulesetsRedirectRuleActionParametersFromValue(TypedDict, total=False):
    preserve_query_string: bool
    """Keep the query string of the original request."""

    status_code: Literal[301, 302, 303, 307, 308]
    """The status code to be used for the redirect."""

    target_url: RulesetsRedirectRuleActionParametersFromValueTargetURL
    """The URL to redirect the request to."""


class RulesetsRedirectRuleActionParameters(TypedDict, total=False):
    from_list: RulesetsRedirectRuleActionParametersFromList
    """Serve a redirect based on a bulk list lookup."""

    from_value: RulesetsRedirectRuleActionParametersFromValue
    """Serve a redirect based on the request properties."""


class RulesetsRewriteRule(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["rewrite"]
    """The action to perform when the rule matches."""

    action_parameters: RulesetsRewriteRuleActionParameters
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


class RulesetsRewriteRuleActionParametersHeadersRemoveHeader(TypedDict, total=False):
    operation: Required[Literal["remove"]]


class RulesetsRewriteRuleActionParametersHeadersStaticHeader(TypedDict, total=False):
    operation: Required[Literal["set"]]

    value: Required[str]
    """Static value for the header."""


class RulesetsRewriteRuleActionParametersHeadersDynamicHeader(TypedDict, total=False):
    expression: Required[str]
    """Expression for the header value."""

    operation: Required[Literal["set"]]


RulesetsRewriteRuleActionParametersHeaders = Union[
    RulesetsRewriteRuleActionParametersHeadersRemoveHeader,
    RulesetsRewriteRuleActionParametersHeadersStaticHeader,
    RulesetsRewriteRuleActionParametersHeadersDynamicHeader,
]


class RulesetsRewriteRuleActionParametersURIPathStaticValue(TypedDict, total=False):
    value: Required[str]
    """Predefined replacement value."""


class RulesetsRewriteRuleActionParametersURIPathDynamicValue(TypedDict, total=False):
    expression: Required[str]
    """Expression to evaluate for the replacement value."""


RulesetsRewriteRuleActionParametersURIPath = Union[
    RulesetsRewriteRuleActionParametersURIPathStaticValue, RulesetsRewriteRuleActionParametersURIPathDynamicValue
]


class RulesetsRewriteRuleActionParametersURIQueryStaticValue(TypedDict, total=False):
    value: Required[str]
    """Predefined replacement value."""


class RulesetsRewriteRuleActionParametersURIQueryDynamicValue(TypedDict, total=False):
    expression: Required[str]
    """Expression to evaluate for the replacement value."""


RulesetsRewriteRuleActionParametersURIQuery = Union[
    RulesetsRewriteRuleActionParametersURIQueryStaticValue, RulesetsRewriteRuleActionParametersURIQueryDynamicValue
]


class RulesetsRewriteRuleActionParametersURI(TypedDict, total=False):
    path: RulesetsRewriteRuleActionParametersURIPath
    """Path portion rewrite."""

    query: RulesetsRewriteRuleActionParametersURIQuery
    """Query portion rewrite."""


class RulesetsRewriteRuleActionParameters(TypedDict, total=False):
    headers: Dict[str, RulesetsRewriteRuleActionParametersHeaders]
    """Map of request headers to modify."""

    uri: RulesetsRewriteRuleActionParametersURI
    """URI to rewrite the request to."""


class RulesetsRouteRule(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["route"]
    """The action to perform when the rule matches."""

    action_parameters: RulesetsRouteRuleActionParameters
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


class RulesetsRouteRuleActionParametersOrigin(TypedDict, total=False):
    host: str
    """Override the resolved hostname."""

    port: float
    """Override the destination port."""


class RulesetsRouteRuleActionParametersSni(TypedDict, total=False):
    value: Required[str]
    """The SNI override."""


class RulesetsRouteRuleActionParameters(TypedDict, total=False):
    host_header: str
    """Rewrite the HTTP Host header."""

    origin: RulesetsRouteRuleActionParametersOrigin
    """Override the IP/TCP destination."""

    sni: RulesetsRouteRuleActionParametersSni
    """Override the Server Name Indication (SNI)."""


class RulesetsScoreRule(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["score"]
    """The action to perform when the rule matches."""

    action_parameters: RulesetsScoreRuleActionParameters
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


class RulesetsScoreRuleActionParameters(TypedDict, total=False):
    increment: int
    """
    Increment contains the delta to change the score and can be either positive or
    negative.
    """


class RulesetsServeErrorRule(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["serve_error"]
    """The action to perform when the rule matches."""

    action_parameters: RulesetsServeErrorRuleActionParameters
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


class RulesetsServeErrorRuleActionParameters(TypedDict, total=False):
    content: str
    """Error response content."""

    content_type: Literal["application/json", "text/xml", "text/plain", "text/html"]
    """Content-type header to set with the response."""

    status_code: float
    """The status code to use for the error."""


class RulesetsSetConfigRule(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["set_config"]
    """The action to perform when the rule matches."""

    action_parameters: RulesetsSetConfigRuleActionParameters
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


class RulesetsSetConfigRuleActionParametersAutominify(TypedDict, total=False):
    css: bool
    """Minify CSS files."""

    html: bool
    """Minify HTML files."""

    js: bool
    """Minify JS files."""


class RulesetsSetConfigRuleActionParameters(TypedDict, total=False):
    automatic_https_rewrites: bool
    """Turn on or off Automatic HTTPS Rewrites."""

    autominify: RulesetsSetConfigRuleActionParametersAutominify
    """Select which file extensions to minify automatically."""

    bic: bool
    """Turn on or off Browser Integrity Check."""

    disable_apps: bool
    """Turn off all active Cloudflare Apps."""

    disable_zaraz: bool
    """Turn off Zaraz."""

    email_obfuscation: bool
    """Turn on or off Email Obfuscation."""

    hotlink_protection: bool
    """Turn on or off the Hotlink Protection."""

    mirage: bool
    """Turn on or off Mirage."""

    opportunistic_encryption: bool
    """Turn on or off Opportunistic Encryption."""

    polish: Literal["off", "lossless", "lossy"]
    """Configure the Polish level."""

    rocket_loader: bool
    """Turn on or off Rocket Loader"""

    security_level: Literal["off", "essentially_off", "low", "medium", "high", "under_attack"]
    """Configure the Security Level."""

    server_side_excludes: bool
    """Turn on or off Server Side Excludes."""

    ssl: Literal["off", "flexible", "full", "strict", "origin_pull"]
    """Configure the SSL level."""

    sxg: bool
    """Turn on or off Signed Exchanges (SXG)."""


class SkipRule(TypedDict, total=False):
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


class RulesetsSetCacheSettingsRule(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["set_cache_settings"]
    """The action to perform when the rule matches."""

    action_parameters: RulesetsSetCacheSettingsRuleActionParameters
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


class RulesetsSetCacheSettingsRuleActionParametersBrowserTTL(TypedDict, total=False):
    mode: Required[Literal["respect_origin", "bypass_by_default", "override_origin"]]
    """Determines which browser ttl mode to use."""

    default: int
    """The TTL (in seconds) if you choose override_origin mode."""


class RulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyCookie(TypedDict, total=False):
    check_presence: List[str]
    """Checks for the presence of these cookie names.

    The presence of these cookies is used in building the cache key.
    """

    include: List[str]
    """Include these cookies' names and their values."""


class RulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyHeader(TypedDict, total=False):
    check_presence: List[str]
    """Checks for the presence of these header names.

    The presence of these headers is used in building the cache key.
    """

    exclude_origin: bool
    """Whether or not to include the origin header.

    A value of true will exclude the origin header in the cache key.
    """

    include: List[str]
    """Include these headers' names and their values."""


class RulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyHost(TypedDict, total=False):
    resolved: bool
    """Use the resolved host in the cache key.

    A value of true will use the resolved host, while a value or false will use the
    original host.
    """


class RulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringExclude(TypedDict, total=False):
    all: bool
    """Exclude all query string parameters from use in building the cache key."""

    list: List[str]
    """A list of query string parameters NOT used to build the cache key.

    All parameters present in the request but missing in this list will be used to
    build the cache key.
    """


class RulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringInclude(TypedDict, total=False):
    all: bool
    """Use all query string parameters in the cache key."""

    list: List[str]
    """A list of query string parameters used to build the cache key."""


class RulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryString(TypedDict, total=False):
    exclude: RulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringExclude
    """
    build the cache key using all query string parameters EXCECPT these excluded
    parameters
    """

    include: RulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringInclude
    """
    build the cache key using a list of query string parameters that ARE in the
    request.
    """


class RulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyUser(TypedDict, total=False):
    device_type: bool
    """Use the user agent's device type in the cache key."""

    geo: bool
    """Use the user agents's country in the cache key."""

    lang: bool
    """Use the user agent's language in the cache key."""


class RulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKey(TypedDict, total=False):
    cookie: RulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyCookie
    """The cookies to include in building the cache key."""

    header: RulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyHeader
    """The header names and values to include in building the cache key."""

    host: RulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyHost
    """Whether to use the original host or the resolved host in the cache key."""

    query_string: RulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryString
    """
    Use the presence or absence of parameters in the query string to build the cache
    key.
    """

    user: RulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyUser
    """Characteristics of the request user agent used in building the cache key."""


class RulesetsSetCacheSettingsRuleActionParametersCacheKey(TypedDict, total=False):
    cache_by_device_type: bool
    """Separate cached content based on the visitor’s device type"""

    cache_deception_armor: bool
    """
    Protect from web cache deception attacks while allowing static assets to be
    cached
    """

    custom_key: RulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKey
    """
    Customize which components of the request are included or excluded from the
    cache key.
    """

    ignore_query_strings_order: bool
    """
    Treat requests with the same query parameters the same, regardless of the order
    those query parameters are in. A value of true ignores the query strings' order.
    """


class RulesetsSetCacheSettingsRuleActionParametersCacheReserve(TypedDict, total=False):
    eligible: Required[bool]
    """Determines whether cache reserve is enabled.

    If this is true and a request meets eligibility criteria, Cloudflare will write
    the resource to cache reserve.
    """

    min_file_size: Required[int]
    """The minimum file size eligible for store in cache reserve."""


_RulesetsSetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTLStatusCodeRangeReservedKeywords = TypedDict(
    "_RulesetsSetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTLStatusCodeRangeReservedKeywords",
    {
        "from": int,
    },
    total=False,
)


class RulesetsSetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTLStatusCodeRange(
    _RulesetsSetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTLStatusCodeRangeReservedKeywords, total=False
):
    to: Required[int]
    """response status code upper bound"""


class RulesetsSetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTL(TypedDict, total=False):
    value: Required[int]
    """Time to cache a response (in seconds).

    A value of 0 is equivalent to setting the Cache-Control header with the value
    "no-cache". A value of -1 is equivalent to setting Cache-Control header with the
    value of "no-store".
    """

    status_code_range: RulesetsSetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTLStatusCodeRange
    """The range of status codes used to apply the selected mode."""

    status_code_value: int
    """Set the ttl for responses with this specific status code"""


class RulesetsSetCacheSettingsRuleActionParametersEdgeTTL(TypedDict, total=False):
    default: Required[int]
    """The TTL (in seconds) if you choose override_origin mode."""

    mode: Required[Literal["respect_origin", "bypass_by_default", "override_origin"]]
    """edge ttl options"""

    status_code_ttl: Required[Iterable[RulesetsSetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTL]]
    """List of single status codes, or status code ranges to apply the selected mode"""


class RulesetsSetCacheSettingsRuleActionParametersServeStale(TypedDict, total=False):
    disable_stale_while_updating: Required[bool]
    """Defines whether Cloudflare should serve stale content while updating.

    If true, Cloudflare will not serve stale content while getting the latest
    content from the origin.
    """


class RulesetsSetCacheSettingsRuleActionParameters(TypedDict, total=False):
    additional_cacheable_ports: Iterable[int]
    """List of additional ports that caching can be enabled on."""

    browser_ttl: RulesetsSetCacheSettingsRuleActionParametersBrowserTTL
    """Specify how long client browsers should cache the response.

    Cloudflare cache purge will not purge content cached on client browsers, so high
    browser TTLs may lead to stale content.
    """

    cache: bool
    """Mark whether the request’s response from origin is eligible for caching.

    Caching itself will still depend on the cache-control header and your other
    caching configurations.
    """

    cache_key: RulesetsSetCacheSettingsRuleActionParametersCacheKey
    """
    Define which components of the request are included or excluded from the cache
    key Cloudflare uses to store the response in cache.
    """

    cache_reserve: RulesetsSetCacheSettingsRuleActionParametersCacheReserve
    """
    Mark whether the request's response from origin is eligible for Cache Reserve
    (requires a Cache Reserve add-on plan).
    """

    edge_ttl: RulesetsSetCacheSettingsRuleActionParametersEdgeTTL
    """
    TTL (Time to Live) specifies the maximum time to cache a resource in the
    Cloudflare edge network.
    """

    origin_cache_control: bool
    """When enabled, Cloudflare will aim to strictly adhere to RFC 7234."""

    origin_error_page_passthru: bool
    """Generate Cloudflare error pages from issues sent from the origin server.

    When on, error pages will trigger for issues from the origin
    """

    read_timeout: int
    """
    Define a timeout value between two successive read operations to your origin
    server. Historically, the timeout value between two read options from Cloudflare
    to an origin server is 100 seconds. If you are attempting to reduce HTTP 524
    errors because of timeouts from an origin server, try increasing this timeout
    value.
    """

    respect_strong_etags: bool
    """
    Specify whether or not Cloudflare should respect strong ETag (entity tag)
    headers. When off, Cloudflare converts strong ETag headers to weak ETag headers.
    """

    serve_stale: RulesetsSetCacheSettingsRuleActionParametersServeStale
    """
    Define if Cloudflare should serve stale content while getting the latest content
    from the origin. If on, Cloudflare will not serve stale content while getting
    the latest content from the origin.
    """


RuleCreateParams = Union[
    BlockRule,
    RulesetsChallengeRule,
    RulesetsCompressResponseRule,
    ExecuteRule,
    RulesetsJsChallengeRule,
    LogRule,
    RulesetsManagedChallengeRule,
    RulesetsRedirectRule,
    RulesetsRewriteRule,
    RulesetsRouteRule,
    RulesetsScoreRule,
    RulesetsServeErrorRule,
    RulesetsSetConfigRule,
    SkipRule,
    RulesetsSetCacheSettingsRule,
]
