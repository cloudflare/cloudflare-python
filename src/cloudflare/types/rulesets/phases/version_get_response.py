# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..logging import Logging
from ..log_rule import LogRule
from ...._models import BaseModel
from ..skip_rule import SkipRule
from ..block_rule import BlockRule
from ..execute_rule import ExecuteRule

__all__ = [
    "VersionGetResponse",
    "Rule",
    "RuleRulesetsChallengeRule",
    "RuleRulesetsCompressResponseRule",
    "RuleRulesetsCompressResponseRuleActionParameters",
    "RuleRulesetsCompressResponseRuleActionParametersAlgorithm",
    "RuleRulesetsJsChallengeRule",
    "RuleRulesetsManagedChallengeRule",
    "RuleRulesetsRedirectRule",
    "RuleRulesetsRedirectRuleActionParameters",
    "RuleRulesetsRedirectRuleActionParametersFromList",
    "RuleRulesetsRedirectRuleActionParametersFromValue",
    "RuleRulesetsRedirectRuleActionParametersFromValueTargetURL",
    "RuleRulesetsRedirectRuleActionParametersFromValueTargetURLStaticURLRedirect",
    "RuleRulesetsRedirectRuleActionParametersFromValueTargetURLDynamicURLRedirect",
    "RuleRulesetsRewriteRule",
    "RuleRulesetsRewriteRuleActionParameters",
    "RuleRulesetsRewriteRuleActionParametersHeaders",
    "RuleRulesetsRewriteRuleActionParametersHeadersRemoveHeader",
    "RuleRulesetsRewriteRuleActionParametersHeadersStaticHeader",
    "RuleRulesetsRewriteRuleActionParametersHeadersDynamicHeader",
    "RuleRulesetsRewriteRuleActionParametersURI",
    "RuleRulesetsRewriteRuleActionParametersURIPath",
    "RuleRulesetsRewriteRuleActionParametersURIPathStaticValue",
    "RuleRulesetsRewriteRuleActionParametersURIPathDynamicValue",
    "RuleRulesetsRewriteRuleActionParametersURIQuery",
    "RuleRulesetsRewriteRuleActionParametersURIQueryStaticValue",
    "RuleRulesetsRewriteRuleActionParametersURIQueryDynamicValue",
    "RuleRulesetsRouteRule",
    "RuleRulesetsRouteRuleActionParameters",
    "RuleRulesetsRouteRuleActionParametersOrigin",
    "RuleRulesetsRouteRuleActionParametersSni",
    "RuleRulesetsScoreRule",
    "RuleRulesetsScoreRuleActionParameters",
    "RuleRulesetsServeErrorRule",
    "RuleRulesetsServeErrorRuleActionParameters",
    "RuleRulesetsSetConfigRule",
    "RuleRulesetsSetConfigRuleActionParameters",
    "RuleRulesetsSetConfigRuleActionParametersAutominify",
    "RuleRulesetsSetCacheSettingsRule",
    "RuleRulesetsSetCacheSettingsRuleActionParameters",
    "RuleRulesetsSetCacheSettingsRuleActionParametersBrowserTTL",
    "RuleRulesetsSetCacheSettingsRuleActionParametersCacheKey",
    "RuleRulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKey",
    "RuleRulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyCookie",
    "RuleRulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyHeader",
    "RuleRulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyHost",
    "RuleRulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryString",
    "RuleRulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringExclude",
    "RuleRulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringInclude",
    "RuleRulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyUser",
    "RuleRulesetsSetCacheSettingsRuleActionParametersCacheReserve",
    "RuleRulesetsSetCacheSettingsRuleActionParametersEdgeTTL",
    "RuleRulesetsSetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTL",
    "RuleRulesetsSetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTLStatusCodeRange",
    "RuleRulesetsSetCacheSettingsRuleActionParametersServeStale",
]


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

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule ID by default)."""


class RuleRulesetsCompressResponseRuleActionParametersAlgorithm(BaseModel):
    name: Optional[Literal["none", "auto", "default", "gzip", "brotli"]] = None
    """Name of compression algorithm to enable."""


class RuleRulesetsCompressResponseRuleActionParameters(BaseModel):
    algorithms: Optional[List[RuleRulesetsCompressResponseRuleActionParametersAlgorithm]] = None
    """Custom order for compression algorithms."""


class RuleRulesetsCompressResponseRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["compress_response"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[RuleRulesetsCompressResponseRuleActionParameters] = None
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


class RuleRulesetsJsChallengeRule(BaseModel):
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

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule ID by default)."""


class RuleRulesetsManagedChallengeRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["managed_challenge"]] = None
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


class RuleRulesetsRedirectRuleActionParametersFromList(BaseModel):
    key: Optional[str] = None
    """Expression that evaluates to the list lookup key."""

    name: Optional[str] = None
    """The name of the list to match against."""


class RuleRulesetsRedirectRuleActionParametersFromValueTargetURLStaticURLRedirect(BaseModel):
    value: Optional[str] = None
    """The URL to redirect the request to."""


class RuleRulesetsRedirectRuleActionParametersFromValueTargetURLDynamicURLRedirect(BaseModel):
    expression: Optional[str] = None
    """An expression to evaluate to get the URL to redirect the request to."""


RuleRulesetsRedirectRuleActionParametersFromValueTargetURL = Union[
    RuleRulesetsRedirectRuleActionParametersFromValueTargetURLStaticURLRedirect,
    RuleRulesetsRedirectRuleActionParametersFromValueTargetURLDynamicURLRedirect,
]


class RuleRulesetsRedirectRuleActionParametersFromValue(BaseModel):
    preserve_query_string: Optional[bool] = None
    """Keep the query string of the original request."""

    status_code: Optional[Literal[301, 302, 303, 307, 308]] = None
    """The status code to be used for the redirect."""

    target_url: Optional[RuleRulesetsRedirectRuleActionParametersFromValueTargetURL] = None
    """The URL to redirect the request to."""


class RuleRulesetsRedirectRuleActionParameters(BaseModel):
    from_list: Optional[RuleRulesetsRedirectRuleActionParametersFromList] = None
    """Serve a redirect based on a bulk list lookup."""

    from_value: Optional[RuleRulesetsRedirectRuleActionParametersFromValue] = None
    """Serve a redirect based on the request properties."""


class RuleRulesetsRedirectRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["redirect"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[RuleRulesetsRedirectRuleActionParameters] = None
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


class RuleRulesetsRewriteRuleActionParametersHeadersRemoveHeader(BaseModel):
    operation: Literal["remove"]


class RuleRulesetsRewriteRuleActionParametersHeadersStaticHeader(BaseModel):
    operation: Literal["set"]

    value: str
    """Static value for the header."""


class RuleRulesetsRewriteRuleActionParametersHeadersDynamicHeader(BaseModel):
    expression: str
    """Expression for the header value."""

    operation: Literal["set"]


RuleRulesetsRewriteRuleActionParametersHeaders = Union[
    RuleRulesetsRewriteRuleActionParametersHeadersRemoveHeader,
    RuleRulesetsRewriteRuleActionParametersHeadersStaticHeader,
    RuleRulesetsRewriteRuleActionParametersHeadersDynamicHeader,
]


class RuleRulesetsRewriteRuleActionParametersURIPathStaticValue(BaseModel):
    value: str
    """Predefined replacement value."""


class RuleRulesetsRewriteRuleActionParametersURIPathDynamicValue(BaseModel):
    expression: str
    """Expression to evaluate for the replacement value."""


RuleRulesetsRewriteRuleActionParametersURIPath = Union[
    RuleRulesetsRewriteRuleActionParametersURIPathStaticValue,
    RuleRulesetsRewriteRuleActionParametersURIPathDynamicValue,
]


class RuleRulesetsRewriteRuleActionParametersURIQueryStaticValue(BaseModel):
    value: str
    """Predefined replacement value."""


class RuleRulesetsRewriteRuleActionParametersURIQueryDynamicValue(BaseModel):
    expression: str
    """Expression to evaluate for the replacement value."""


RuleRulesetsRewriteRuleActionParametersURIQuery = Union[
    RuleRulesetsRewriteRuleActionParametersURIQueryStaticValue,
    RuleRulesetsRewriteRuleActionParametersURIQueryDynamicValue,
]


class RuleRulesetsRewriteRuleActionParametersURI(BaseModel):
    path: Optional[RuleRulesetsRewriteRuleActionParametersURIPath] = None
    """Path portion rewrite."""

    query: Optional[RuleRulesetsRewriteRuleActionParametersURIQuery] = None
    """Query portion rewrite."""


class RuleRulesetsRewriteRuleActionParameters(BaseModel):
    headers: Optional[Dict[str, RuleRulesetsRewriteRuleActionParametersHeaders]] = None
    """Map of request headers to modify."""

    uri: Optional[RuleRulesetsRewriteRuleActionParametersURI] = None
    """URI to rewrite the request to."""


class RuleRulesetsRewriteRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["rewrite"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[RuleRulesetsRewriteRuleActionParameters] = None
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


class RuleRulesetsRouteRuleActionParametersOrigin(BaseModel):
    host: Optional[str] = None
    """Override the resolved hostname."""

    port: Optional[float] = None
    """Override the destination port."""


class RuleRulesetsRouteRuleActionParametersSni(BaseModel):
    value: str
    """The SNI override."""


class RuleRulesetsRouteRuleActionParameters(BaseModel):
    host_header: Optional[str] = None
    """Rewrite the HTTP Host header."""

    origin: Optional[RuleRulesetsRouteRuleActionParametersOrigin] = None
    """Override the IP/TCP destination."""

    sni: Optional[RuleRulesetsRouteRuleActionParametersSni] = None
    """Override the Server Name Indication (SNI)."""


class RuleRulesetsRouteRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["route"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[RuleRulesetsRouteRuleActionParameters] = None
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


class RuleRulesetsScoreRuleActionParameters(BaseModel):
    increment: Optional[int] = None
    """
    Increment contains the delta to change the score and can be either positive or
    negative.
    """


class RuleRulesetsScoreRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["score"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[RuleRulesetsScoreRuleActionParameters] = None
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


class RuleRulesetsServeErrorRuleActionParameters(BaseModel):
    content: Optional[str] = None
    """Error response content."""

    content_type: Optional[Literal["application/json", "text/xml", "text/plain", "text/html"]] = None
    """Content-type header to set with the response."""

    status_code: Optional[float] = None
    """The status code to use for the error."""


class RuleRulesetsServeErrorRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["serve_error"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[RuleRulesetsServeErrorRuleActionParameters] = None
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


class RuleRulesetsSetConfigRuleActionParametersAutominify(BaseModel):
    css: Optional[bool] = None
    """Minify CSS files."""

    html: Optional[bool] = None
    """Minify HTML files."""

    js: Optional[bool] = None
    """Minify JS files."""


class RuleRulesetsSetConfigRuleActionParameters(BaseModel):
    automatic_https_rewrites: Optional[bool] = None
    """Turn on or off Automatic HTTPS Rewrites."""

    autominify: Optional[RuleRulesetsSetConfigRuleActionParametersAutominify] = None
    """Select which file extensions to minify automatically."""

    bic: Optional[bool] = None
    """Turn on or off Browser Integrity Check."""

    disable_apps: Optional[bool] = None
    """Turn off all active Cloudflare Apps."""

    disable_zaraz: Optional[bool] = None
    """Turn off Zaraz."""

    email_obfuscation: Optional[bool] = None
    """Turn on or off Email Obfuscation."""

    hotlink_protection: Optional[bool] = None
    """Turn on or off the Hotlink Protection."""

    mirage: Optional[bool] = None
    """Turn on or off Mirage."""

    opportunistic_encryption: Optional[bool] = None
    """Turn on or off Opportunistic Encryption."""

    polish: Optional[Literal["off", "lossless", "lossy"]] = None
    """Configure the Polish level."""

    rocket_loader: Optional[bool] = None
    """Turn on or off Rocket Loader"""

    security_level: Optional[Literal["off", "essentially_off", "low", "medium", "high", "under_attack"]] = None
    """Configure the Security Level."""

    server_side_excludes: Optional[bool] = None
    """Turn on or off Server Side Excludes."""

    ssl: Optional[Literal["off", "flexible", "full", "strict", "origin_pull"]] = None
    """Configure the SSL level."""

    sxg: Optional[bool] = None
    """Turn on or off Signed Exchanges (SXG)."""


class RuleRulesetsSetConfigRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["set_config"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[RuleRulesetsSetConfigRuleActionParameters] = None
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


class RuleRulesetsSetCacheSettingsRuleActionParametersBrowserTTL(BaseModel):
    mode: Literal["respect_origin", "bypass_by_default", "override_origin"]
    """Determines which browser ttl mode to use."""

    default: Optional[int] = None
    """The TTL (in seconds) if you choose override_origin mode."""


class RuleRulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyCookie(BaseModel):
    check_presence: Optional[List[str]] = None
    """Checks for the presence of these cookie names.

    The presence of these cookies is used in building the cache key.
    """

    include: Optional[List[str]] = None
    """Include these cookies' names and their values."""


class RuleRulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyHeader(BaseModel):
    check_presence: Optional[List[str]] = None
    """Checks for the presence of these header names.

    The presence of these headers is used in building the cache key.
    """

    exclude_origin: Optional[bool] = None
    """Whether or not to include the origin header.

    A value of true will exclude the origin header in the cache key.
    """

    include: Optional[List[str]] = None
    """Include these headers' names and their values."""


class RuleRulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyHost(BaseModel):
    resolved: Optional[bool] = None
    """Use the resolved host in the cache key.

    A value of true will use the resolved host, while a value or false will use the
    original host.
    """


class RuleRulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringExclude(BaseModel):
    all: Optional[bool] = None
    """Exclude all query string parameters from use in building the cache key."""

    rule_list: Optional[List[str]] = FieldInfo(alias="list", default=None)
    """A list of query string parameters NOT used to build the cache key.

    All parameters present in the request but missing in this list will be used to
    build the cache key.
    """


class RuleRulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringInclude(BaseModel):
    all: Optional[bool] = None
    """Use all query string parameters in the cache key."""

    rule_list: Optional[List[str]] = FieldInfo(alias="list", default=None)
    """A list of query string parameters used to build the cache key."""


class RuleRulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryString(BaseModel):
    exclude: Optional[RuleRulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringExclude] = None
    """
    build the cache key using all query string parameters EXCECPT these excluded
    parameters
    """

    include: Optional[RuleRulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringInclude] = None
    """
    build the cache key using a list of query string parameters that ARE in the
    request.
    """


class RuleRulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyUser(BaseModel):
    device_type: Optional[bool] = None
    """Use the user agent's device type in the cache key."""

    geo: Optional[bool] = None
    """Use the user agents's country in the cache key."""

    lang: Optional[bool] = None
    """Use the user agent's language in the cache key."""


class RuleRulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKey(BaseModel):
    cookie: Optional[RuleRulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyCookie] = None
    """The cookies to include in building the cache key."""

    header: Optional[RuleRulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyHeader] = None
    """The header names and values to include in building the cache key."""

    host: Optional[RuleRulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyHost] = None
    """Whether to use the original host or the resolved host in the cache key."""

    query_string: Optional[RuleRulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryString] = None
    """
    Use the presence or absence of parameters in the query string to build the cache
    key.
    """

    user: Optional[RuleRulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKeyUser] = None
    """Characteristics of the request user agent used in building the cache key."""


class RuleRulesetsSetCacheSettingsRuleActionParametersCacheKey(BaseModel):
    cache_by_device_type: Optional[bool] = None
    """Separate cached content based on the visitor’s device type"""

    cache_deception_armor: Optional[bool] = None
    """
    Protect from web cache deception attacks while allowing static assets to be
    cached
    """

    custom_key: Optional[RuleRulesetsSetCacheSettingsRuleActionParametersCacheKeyCustomKey] = None
    """
    Customize which components of the request are included or excluded from the
    cache key.
    """

    ignore_query_strings_order: Optional[bool] = None
    """
    Treat requests with the same query parameters the same, regardless of the order
    those query parameters are in. A value of true ignores the query strings' order.
    """


class RuleRulesetsSetCacheSettingsRuleActionParametersCacheReserve(BaseModel):
    eligible: bool
    """Determines whether cache reserve is enabled.

    If this is true and a request meets eligibility criteria, Cloudflare will write
    the resource to cache reserve.
    """

    min_file_size: int
    """The minimum file size eligible for store in cache reserve."""


class RuleRulesetsSetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTLStatusCodeRange(BaseModel):
    from_: int = FieldInfo(alias="from")
    """response status code lower bound"""

    to: int
    """response status code upper bound"""


class RuleRulesetsSetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTL(BaseModel):
    value: int
    """Time to cache a response (in seconds).

    A value of 0 is equivalent to setting the Cache-Control header with the value
    "no-cache". A value of -1 is equivalent to setting Cache-Control header with the
    value of "no-store".
    """

    status_code_range: Optional[
        RuleRulesetsSetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTLStatusCodeRange
    ] = None
    """The range of status codes used to apply the selected mode."""

    status_code_value: Optional[int] = None
    """Set the ttl for responses with this specific status code"""


class RuleRulesetsSetCacheSettingsRuleActionParametersEdgeTTL(BaseModel):
    default: int
    """The TTL (in seconds) if you choose override_origin mode."""

    mode: Literal["respect_origin", "bypass_by_default", "override_origin"]
    """edge ttl options"""

    status_code_ttl: List[RuleRulesetsSetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTL]
    """List of single status codes, or status code ranges to apply the selected mode"""


class RuleRulesetsSetCacheSettingsRuleActionParametersServeStale(BaseModel):
    disable_stale_while_updating: bool
    """Defines whether Cloudflare should serve stale content while updating.

    If true, Cloudflare will not serve stale content while getting the latest
    content from the origin.
    """


class RuleRulesetsSetCacheSettingsRuleActionParameters(BaseModel):
    additional_cacheable_ports: Optional[List[int]] = None
    """List of additional ports that caching can be enabled on."""

    browser_ttl: Optional[RuleRulesetsSetCacheSettingsRuleActionParametersBrowserTTL] = None
    """Specify how long client browsers should cache the response.

    Cloudflare cache purge will not purge content cached on client browsers, so high
    browser TTLs may lead to stale content.
    """

    cache: Optional[bool] = None
    """Mark whether the request’s response from origin is eligible for caching.

    Caching itself will still depend on the cache-control header and your other
    caching configurations.
    """

    cache_key: Optional[RuleRulesetsSetCacheSettingsRuleActionParametersCacheKey] = None
    """
    Define which components of the request are included or excluded from the cache
    key Cloudflare uses to store the response in cache.
    """

    cache_reserve: Optional[RuleRulesetsSetCacheSettingsRuleActionParametersCacheReserve] = None
    """
    Mark whether the request's response from origin is eligible for Cache Reserve
    (requires a Cache Reserve add-on plan).
    """

    edge_ttl: Optional[RuleRulesetsSetCacheSettingsRuleActionParametersEdgeTTL] = None
    """
    TTL (Time to Live) specifies the maximum time to cache a resource in the
    Cloudflare edge network.
    """

    origin_cache_control: Optional[bool] = None
    """When enabled, Cloudflare will aim to strictly adhere to RFC 7234."""

    origin_error_page_passthru: Optional[bool] = None
    """Generate Cloudflare error pages from issues sent from the origin server.

    When on, error pages will trigger for issues from the origin
    """

    read_timeout: Optional[int] = None
    """
    Define a timeout value between two successive read operations to your origin
    server. Historically, the timeout value between two read options from Cloudflare
    to an origin server is 100 seconds. If you are attempting to reduce HTTP 524
    errors because of timeouts from an origin server, try increasing this timeout
    value.
    """

    respect_strong_etags: Optional[bool] = None
    """
    Specify whether or not Cloudflare should respect strong ETag (entity tag)
    headers. When off, Cloudflare converts strong ETag headers to weak ETag headers.
    """

    serve_stale: Optional[RuleRulesetsSetCacheSettingsRuleActionParametersServeStale] = None
    """
    Define if Cloudflare should serve stale content while getting the latest content
    from the origin. If on, Cloudflare will not serve stale content while getting
    the latest content from the origin.
    """


class RuleRulesetsSetCacheSettingsRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["set_cache_settings"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[RuleRulesetsSetCacheSettingsRuleActionParameters] = None
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


Rule = Union[
    BlockRule,
    RuleRulesetsChallengeRule,
    RuleRulesetsCompressResponseRule,
    ExecuteRule,
    RuleRulesetsJsChallengeRule,
    LogRule,
    RuleRulesetsManagedChallengeRule,
    RuleRulesetsRedirectRule,
    RuleRulesetsRewriteRule,
    RuleRulesetsRouteRule,
    RuleRulesetsScoreRule,
    RuleRulesetsServeErrorRule,
    RuleRulesetsSetConfigRule,
    SkipRule,
    RuleRulesetsSetCacheSettingsRule,
]


class VersionGetResponse(BaseModel):
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
