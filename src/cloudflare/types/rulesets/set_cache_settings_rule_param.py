# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal, Required, TypedDict

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
]


class ActionParametersBrowserTTL(TypedDict, total=False):
    mode: Required[Literal["respect_origin", "bypass_by_default", "override_origin"]]
    """Determines which browser ttl mode to use."""

    default: int
    """The TTL (in seconds) if you choose override_origin mode."""


class ActionParametersCacheKeyCustomKeyCookie(TypedDict, total=False):
    check_presence: List[str]
    """Checks for the presence of these cookie names.

    The presence of these cookies is used in building the cache key.
    """

    include: List[str]
    """Include these cookies' names and their values."""


class ActionParametersCacheKeyCustomKeyHeader(TypedDict, total=False):
    check_presence: List[str]
    """Checks for the presence of these header names.

    The presence of these headers is used in building the cache key.
    """

    contains: Dict[str, List[str]]
    """
    For each header name and list of values combination, check if the request header
    contains any of the values provided. The presence of the request header and
    whether any of the values provided are contained in the request header value is
    used in building the cache key.
    """

    exclude_origin: bool
    """Whether or not to include the origin header.

    A value of true will exclude the origin header in the cache key.
    """

    include: List[str]
    """Include these headers' names and their values."""


class ActionParametersCacheKeyCustomKeyHost(TypedDict, total=False):
    resolved: bool
    """Use the resolved host in the cache key.

    A value of true will use the resolved host, while a value or false will use the
    original host.
    """


class ActionParametersCacheKeyCustomKeyQueryStringExclude(TypedDict, total=False):
    all: bool
    """Exclude all query string parameters from use in building the cache key."""

    list: List[str]
    """A list of query string parameters NOT used to build the cache key.

    All parameters present in the request but missing in this list will be used to
    build the cache key.
    """


class ActionParametersCacheKeyCustomKeyQueryStringInclude(TypedDict, total=False):
    all: bool
    """Use all query string parameters in the cache key."""

    list: List[str]
    """A list of query string parameters used to build the cache key."""


class ActionParametersCacheKeyCustomKeyQueryString(TypedDict, total=False):
    exclude: ActionParametersCacheKeyCustomKeyQueryStringExclude
    """
    build the cache key using all query string parameters EXCECPT these excluded
    parameters
    """

    include: ActionParametersCacheKeyCustomKeyQueryStringInclude
    """
    build the cache key using a list of query string parameters that ARE in the
    request.
    """


class ActionParametersCacheKeyCustomKeyUser(TypedDict, total=False):
    device_type: bool
    """Use the user agent's device type in the cache key."""

    geo: bool
    """Use the user agents's country in the cache key."""

    lang: bool
    """Use the user agent's language in the cache key."""


class ActionParametersCacheKeyCustomKey(TypedDict, total=False):
    cookie: ActionParametersCacheKeyCustomKeyCookie
    """The cookies to include in building the cache key."""

    header: ActionParametersCacheKeyCustomKeyHeader
    """The header names and values to include in building the cache key."""

    host: ActionParametersCacheKeyCustomKeyHost
    """Whether to use the original host or the resolved host in the cache key."""

    query_string: ActionParametersCacheKeyCustomKeyQueryString
    """
    Use the presence or absence of parameters in the query string to build the cache
    key.
    """

    user: ActionParametersCacheKeyCustomKeyUser
    """Characteristics of the request user agent used in building the cache key."""


class ActionParametersCacheKey(TypedDict, total=False):
    cache_by_device_type: bool
    """Separate cached content based on the visitor’s device type"""

    cache_deception_armor: bool
    """
    Protect from web cache deception attacks while allowing static assets to be
    cached
    """

    custom_key: ActionParametersCacheKeyCustomKey
    """
    Customize which components of the request are included or excluded from the
    cache key.
    """

    ignore_query_strings_order: bool
    """
    Treat requests with the same query parameters the same, regardless of the order
    those query parameters are in. A value of true ignores the query strings' order.
    """


class ActionParametersCacheReserve(TypedDict, total=False):
    eligible: Required[bool]
    """Determines whether cache reserve is enabled.

    If this is true and a request meets eligibility criteria, Cloudflare will write
    the resource to cache reserve.
    """

    minimum_file_size: Required[int]
    """The minimum file size eligible for store in cache reserve."""


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
    to: Required[int]
    """response status code upper bound"""


class ActionParametersEdgeTTLStatusCodeTTL(TypedDict, total=False):
    value: Required[int]
    """Time to cache a response (in seconds).

    A value of 0 is equivalent to setting the Cache-Control header with the value
    "no-cache". A value of -1 is equivalent to setting Cache-Control header with the
    value of "no-store".
    """

    status_code_range: ActionParametersEdgeTTLStatusCodeTTLStatusCodeRange
    """The range of status codes used to apply the selected mode."""

    status_code_value: int
    """Set the ttl for responses with this specific status code"""


class ActionParametersEdgeTTL(TypedDict, total=False):
    default: Required[int]
    """The TTL (in seconds) if you choose override_origin mode."""

    mode: Required[Literal["respect_origin", "bypass_by_default", "override_origin"]]
    """edge ttl options"""

    status_code_ttl: Required[Iterable[ActionParametersEdgeTTLStatusCodeTTL]]
    """List of single status codes, or status code ranges to apply the selected mode"""


class ActionParametersServeStale(TypedDict, total=False):
    disable_stale_while_updating: Required[bool]
    """Defines whether Cloudflare should serve stale content while updating.

    If true, Cloudflare will not serve stale content while getting the latest
    content from the origin.
    """


class ActionParameters(TypedDict, total=False):
    additional_cacheable_ports: Iterable[int]
    """List of additional ports that caching can be enabled on."""

    browser_ttl: ActionParametersBrowserTTL
    """Specify how long client browsers should cache the response.

    Cloudflare cache purge will not purge content cached on client browsers, so high
    browser TTLs may lead to stale content.
    """

    cache: bool
    """Mark whether the request’s response from origin is eligible for caching.

    Caching itself will still depend on the cache-control header and your other
    caching configurations.
    """

    cache_key: ActionParametersCacheKey
    """
    Define which components of the request are included or excluded from the cache
    key Cloudflare uses to store the response in cache.
    """

    cache_reserve: ActionParametersCacheReserve
    """
    Mark whether the request's response from origin is eligible for Cache Reserve
    (requires a Cache Reserve add-on plan).
    """

    edge_ttl: ActionParametersEdgeTTL
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

    serve_stale: ActionParametersServeStale
    """
    Define if Cloudflare should serve stale content while getting the latest content
    from the origin. If on, Cloudflare will not serve stale content while getting
    the latest content from the origin.
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

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""
