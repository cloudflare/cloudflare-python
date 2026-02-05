# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from .logging_param import LoggingParam

__all__ = [
    "SetCacheSettingsRuleParam",
    "ActionParameters",
    "ActionParametersBrowserTTL",
    "ActionParametersCacheKey",
    "ActionParametersCacheKeyCustomKey",
    "ActionParametersCacheKeyCustomKeyCookie",
    "ActionParametersCacheKeyCustomKeyHeader",
    "ActionParametersCacheKeyCustomKeyHost",
    "ActionParametersCacheKeyCustomKeyQueryString",
    "ActionParametersCacheKeyCustomKeyQueryStringExclude",
    "ActionParametersCacheKeyCustomKeyQueryStringInclude",
    "ActionParametersCacheKeyCustomKeyUser",
    "ActionParametersCacheReserve",
    "ActionParametersEdgeTTL",
    "ActionParametersEdgeTTLStatusCodeTTL",
    "ActionParametersEdgeTTLStatusCodeTTLStatusCodeRange",
    "ActionParametersServeStale",
    "ExposedCredentialCheck",
    "Ratelimit",
]


class ActionParametersBrowserTTL(TypedDict, total=False):
    """How long client browsers should cache the response.

    Cloudflare cache purge will not purge content cached on client browsers, so high browser TTLs may lead to stale content.
    """

    mode: Required[Literal["respect_origin", "bypass_by_default", "override_origin", "bypass"]]
    """The browser TTL mode."""

    default: int
    """The browser TTL (in seconds) if you choose the "override_origin" mode."""


class ActionParametersCacheKeyCustomKeyCookie(TypedDict, total=False):
    """Which cookies to include in the cache key."""

    check_presence: SequenceNotStr[str]
    """A list of cookies to check for the presence of.

    The presence of these cookies is included in the cache key.
    """

    include: SequenceNotStr[str]
    """A list of cookies to include in the cache key."""


class ActionParametersCacheKeyCustomKeyHeader(TypedDict, total=False):
    """Which headers to include in the cache key."""

    check_presence: SequenceNotStr[str]
    """A list of headers to check for the presence of.

    The presence of these headers is included in the cache key.
    """

    contains: Dict[str, SequenceNotStr[str]]
    """A mapping of header names to a list of values.

    If a header is present in the request and contains any of the values provided,
    its value is included in the cache key.
    """

    exclude_origin: bool
    """Whether to exclude the origin header in the cache key."""

    include: SequenceNotStr[str]
    """A list of headers to include in the cache key."""


class ActionParametersCacheKeyCustomKeyHost(TypedDict, total=False):
    """How to use the host in the cache key."""

    resolved: bool
    """Whether to use the resolved host in the cache key."""


class ActionParametersCacheKeyCustomKeyQueryStringExclude(TypedDict, total=False):
    """Which query string parameters to exclude from the cache key."""

    all: Literal[True]
    """Whether to exclude all query string parameters from the cache key."""

    list: SequenceNotStr[str]
    """A list of query string parameters to exclude from the cache key."""


class ActionParametersCacheKeyCustomKeyQueryStringInclude(TypedDict, total=False):
    """Which query string parameters to include in the cache key."""

    all: Literal[True]
    """Whether to include all query string parameters in the cache key."""

    list: SequenceNotStr[str]
    """A list of query string parameters to include in the cache key."""


class ActionParametersCacheKeyCustomKeyQueryString(TypedDict, total=False):
    """Which query string parameters to include in or exclude from the cache key."""

    exclude: ActionParametersCacheKeyCustomKeyQueryStringExclude
    """Which query string parameters to exclude from the cache key."""

    include: ActionParametersCacheKeyCustomKeyQueryStringInclude
    """Which query string parameters to include in the cache key."""


class ActionParametersCacheKeyCustomKeyUser(TypedDict, total=False):
    """How to use characteristics of the request user agent in the cache key."""

    device_type: bool
    """Whether to use the user agent's device type in the cache key."""

    geo: bool
    """Whether to use the user agents's country in the cache key."""

    lang: bool
    """Whether to use the user agent's language in the cache key."""


class ActionParametersCacheKeyCustomKey(TypedDict, total=False):
    """Which components of the request are included or excluded from the cache key."""

    cookie: ActionParametersCacheKeyCustomKeyCookie
    """Which cookies to include in the cache key."""

    header: ActionParametersCacheKeyCustomKeyHeader
    """Which headers to include in the cache key."""

    host: ActionParametersCacheKeyCustomKeyHost
    """How to use the host in the cache key."""

    query_string: ActionParametersCacheKeyCustomKeyQueryString
    """Which query string parameters to include in or exclude from the cache key."""

    user: ActionParametersCacheKeyCustomKeyUser
    """How to use characteristics of the request user agent in the cache key."""


class ActionParametersCacheKey(TypedDict, total=False):
    """
    Which components of the request are included in or excluded from the cache key Cloudflare uses to store the response in cache.
    """

    cache_by_device_type: bool
    """Whether to separate cached content based on the visitor's device type."""

    cache_deception_armor: bool
    """
    Whether to protect from web cache deception attacks, while allowing static
    assets to be cached.
    """

    custom_key: ActionParametersCacheKeyCustomKey
    """Which components of the request are included or excluded from the cache key."""

    ignore_query_strings_order: bool
    """
    Whether to treat requests with the same query parameters the same, regardless of
    the order those query parameters are in.
    """


class ActionParametersCacheReserve(TypedDict, total=False):
    """
    Settings to determine whether the request's response from origin is eligible for Cache Reserve (requires a Cache Reserve add-on plan).
    """

    eligible: Required[bool]
    """Whether Cache Reserve is enabled.

    If this is true and a request meets eligibility criteria, Cloudflare will write
    the resource to Cache Reserve.
    """

    minimum_file_size: int
    """The minimum file size eligible for storage in Cache Reserve."""


_ActionParametersEdgeTTLStatusCodeTTLStatusCodeRangeReservedKeywords = TypedDict(
    "_ActionParametersEdgeTTLStatusCodeTTLStatusCodeRangeReservedKeywords",
    {
        "from": int,
    },
    total=False,
)


class ActionParametersEdgeTTLStatusCodeTTLStatusCodeRange(
    _ActionParametersEdgeTTLStatusCodeTTLStatusCodeRangeReservedKeywords, total=False
):
    """A range of status codes to apply the TTL to."""

    to: int
    """The upper bound of the range."""


class ActionParametersEdgeTTLStatusCodeTTL(TypedDict, total=False):
    value: Required[int]
    """The time to cache the response for (in seconds).

    A value of 0 is equivalent to setting the cache control header with the value
    "no-cache". A value of -1 is equivalent to setting the cache control header with
    the value of "no-store".
    """

    status_code: int
    """A single status code to apply the TTL to."""

    status_code_range: ActionParametersEdgeTTLStatusCodeTTLStatusCodeRange
    """A range of status codes to apply the TTL to."""


class ActionParametersEdgeTTL(TypedDict, total=False):
    """How long the Cloudflare edge network should cache the response."""

    mode: Required[Literal["respect_origin", "bypass_by_default", "override_origin"]]
    """The edge TTL mode."""

    default: int
    """The edge TTL (in seconds) if you choose the "override_origin" mode."""

    status_code_ttl: Iterable[ActionParametersEdgeTTLStatusCodeTTL]
    """A list of TTLs to apply to specific status codes or status code ranges."""


class ActionParametersServeStale(TypedDict, total=False):
    """When to serve stale content from cache."""

    disable_stale_while_updating: bool
    """
    Whether Cloudflare should disable serving stale content while getting the latest
    content from the origin.
    """


class ActionParameters(TypedDict, total=False):
    """The parameters configuring the rule's action."""

    additional_cacheable_ports: Iterable[int]
    """A list of additional ports that caching should be enabled on."""

    browser_ttl: ActionParametersBrowserTTL
    """How long client browsers should cache the response.

    Cloudflare cache purge will not purge content cached on client browsers, so high
    browser TTLs may lead to stale content.
    """

    cache: bool
    """Whether the request's response from the origin is eligible for caching.

    Caching itself will still depend on the cache control header and your other
    caching configurations.
    """

    cache_key: ActionParametersCacheKey
    """
    Which components of the request are included in or excluded from the cache key
    Cloudflare uses to store the response in cache.
    """

    cache_reserve: ActionParametersCacheReserve
    """
    Settings to determine whether the request's response from origin is eligible for
    Cache Reserve (requires a Cache Reserve add-on plan).
    """

    edge_ttl: ActionParametersEdgeTTL
    """How long the Cloudflare edge network should cache the response."""

    origin_cache_control: bool
    """Whether Cloudflare will aim to strictly adhere to RFC 7234."""

    origin_error_page_passthru: bool
    """Whether to generate Cloudflare error pages for issues from the origin server."""

    read_timeout: int
    """
    A timeout value between two successive read operations to use for your origin
    server. Historically, the timeout value between two read options from Cloudflare
    to an origin server is 100 seconds. If you are attempting to reduce HTTP 524
    errors because of timeouts from an origin server, try increasing this timeout
    value.
    """

    respect_strong_etags: bool
    """Whether Cloudflare should respect strong ETag (entity tag) headers.

    If false, Cloudflare converts strong ETag headers to weak ETag headers.
    """

    serve_stale: ActionParametersServeStale
    """When to serve stale content from cache."""


class ExposedCredentialCheck(TypedDict, total=False):
    """Configuration for exposed credential checking."""

    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class Ratelimit(TypedDict, total=False):
    """An object configuring the rule's rate limit behavior."""

    characteristics: Required[SequenceNotStr[str]]
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


class SetCacheSettingsRuleParam(TypedDict, total=False):
    id: str
    """The unique ID of the rule."""

    action: Literal["set_cache_settings"]
    """The action to perform when the rule matches."""

    action_parameters: ActionParameters
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: ExposedCredentialCheck
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    ratelimit: Ratelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""
