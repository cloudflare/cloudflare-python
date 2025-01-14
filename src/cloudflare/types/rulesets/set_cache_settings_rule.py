# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .logging import Logging
from ..._models import BaseModel

__all__ = [
    "SetCacheSettingsRule",
    "ActionParameters",
    "ActionParametersBrowserTTL",
    "ActionParametersCacheKey",
    "ActionParametersCacheKeyCustomKey",
    "ActionParametersCacheKeyCustomKeyCookie",
    "ActionParametersCacheKeyCustomKeyHeader",
    "ActionParametersCacheKeyCustomKeyHost",
    "ActionParametersCacheKeyCustomKeyQueryString",
    "ActionParametersCacheKeyCustomKeyQueryStringIncludedQueryStringParameters",
    "ActionParametersCacheKeyCustomKeyQueryStringIncludedQueryStringParametersInclude",
    "ActionParametersCacheKeyCustomKeyQueryStringIncludedQueryStringParametersIncludeSomeQueryStringParameters",
    "ActionParametersCacheKeyCustomKeyQueryStringIncludedQueryStringParametersIncludeAllQueryStringParameters",
    "ActionParametersCacheKeyCustomKeyQueryStringExcludedQueryStringParameters",
    "ActionParametersCacheKeyCustomKeyQueryStringExcludedQueryStringParametersExclude",
    "ActionParametersCacheKeyCustomKeyQueryStringExcludedQueryStringParametersExcludeSomeQueryStringParameters",
    "ActionParametersCacheKeyCustomKeyQueryStringExcludedQueryStringParametersExcludeAllQueryStringParameters",
    "ActionParametersCacheKeyCustomKeyUser",
    "ActionParametersCacheReserve",
    "ActionParametersEdgeTTL",
    "ActionParametersEdgeTTLStatusCodeTTL",
    "ActionParametersEdgeTTLStatusCodeTTLStatusCodeRange",
    "ActionParametersServeStale",
    "ExposedCredentialCheck",
    "Ratelimit",
]


class ActionParametersBrowserTTL(BaseModel):
    mode: Literal["respect_origin", "bypass_by_default", "override_origin"]
    """Determines which browser ttl mode to use."""

    default: Optional[int] = None
    """The TTL (in seconds) if you choose override_origin mode."""


class ActionParametersCacheKeyCustomKeyCookie(BaseModel):
    check_presence: Optional[List[str]] = None
    """Checks for the presence of these cookie names.

    The presence of these cookies is used in building the cache key.
    """

    include: Optional[List[str]] = None
    """Include these cookies' names and their values."""


class ActionParametersCacheKeyCustomKeyHeader(BaseModel):
    check_presence: Optional[List[str]] = None
    """Checks for the presence of these header names.

    The presence of these headers is used in building the cache key.
    """

    contains: Optional[Dict[str, List[str]]] = None
    """
    For each header name and list of values combination, check if the request header
    contains any of the values provided. The presence of the request header and
    whether any of the values provided are contained in the request header value is
    used in building the cache key.
    """

    exclude_origin: Optional[bool] = None
    """Whether or not to include the origin header.

    A value of true will exclude the origin header in the cache key.
    """

    include: Optional[List[str]] = None
    """Include these headers' names and their values."""


class ActionParametersCacheKeyCustomKeyHost(BaseModel):
    resolved: Optional[bool] = None
    """Use the resolved host in the cache key.

    A value of true will use the resolved host, while a value or false will use the
    original host.
    """


class ActionParametersCacheKeyCustomKeyQueryStringIncludedQueryStringParametersIncludeSomeQueryStringParameters(
    BaseModel
):
    rule_list: Optional[List[str]] = FieldInfo(alias="list", default=None)


class ActionParametersCacheKeyCustomKeyQueryStringIncludedQueryStringParametersIncludeAllQueryStringParameters(
    BaseModel
):
    all: Optional[bool] = None
    """Determines whether to include all query string parameters in the cache key."""


ActionParametersCacheKeyCustomKeyQueryStringIncludedQueryStringParametersInclude: TypeAlias = Union[
    ActionParametersCacheKeyCustomKeyQueryStringIncludedQueryStringParametersIncludeSomeQueryStringParameters,
    ActionParametersCacheKeyCustomKeyQueryStringIncludedQueryStringParametersIncludeAllQueryStringParameters,
]


class ActionParametersCacheKeyCustomKeyQueryStringIncludedQueryStringParameters(BaseModel):
    include: Optional[ActionParametersCacheKeyCustomKeyQueryStringIncludedQueryStringParametersInclude] = None
    """A list of query string parameters used to build the cache key."""


class ActionParametersCacheKeyCustomKeyQueryStringExcludedQueryStringParametersExcludeSomeQueryStringParameters(
    BaseModel
):
    rule_list: Optional[List[str]] = FieldInfo(alias="list", default=None)


class ActionParametersCacheKeyCustomKeyQueryStringExcludedQueryStringParametersExcludeAllQueryStringParameters(
    BaseModel
):
    all: Optional[bool] = None
    """Determines whether to exclude all query string parameters from the cache key."""


ActionParametersCacheKeyCustomKeyQueryStringExcludedQueryStringParametersExclude: TypeAlias = Union[
    ActionParametersCacheKeyCustomKeyQueryStringExcludedQueryStringParametersExcludeSomeQueryStringParameters,
    ActionParametersCacheKeyCustomKeyQueryStringExcludedQueryStringParametersExcludeAllQueryStringParameters,
]


class ActionParametersCacheKeyCustomKeyQueryStringExcludedQueryStringParameters(BaseModel):
    exclude: Optional[ActionParametersCacheKeyCustomKeyQueryStringExcludedQueryStringParametersExclude] = None
    """A list of query string parameters NOT used to build the cache key.

    All parameters present in the request but missing in this list will be used to
    build the cache key.
    """


ActionParametersCacheKeyCustomKeyQueryString: TypeAlias = Union[
    ActionParametersCacheKeyCustomKeyQueryStringIncludedQueryStringParameters,
    ActionParametersCacheKeyCustomKeyQueryStringExcludedQueryStringParameters,
]


class ActionParametersCacheKeyCustomKeyUser(BaseModel):
    device_type: Optional[bool] = None
    """Use the user agent's device type in the cache key."""

    geo: Optional[bool] = None
    """Use the user agents's country in the cache key."""

    lang: Optional[bool] = None
    """Use the user agent's language in the cache key."""


class ActionParametersCacheKeyCustomKey(BaseModel):
    cookie: Optional[ActionParametersCacheKeyCustomKeyCookie] = None
    """The cookies to include in building the cache key."""

    header: Optional[ActionParametersCacheKeyCustomKeyHeader] = None
    """The header names and values to include in building the cache key."""

    host: Optional[ActionParametersCacheKeyCustomKeyHost] = None
    """Whether to use the original host or the resolved host in the cache key."""

    query_string: Optional[ActionParametersCacheKeyCustomKeyQueryString] = None
    """Use the presence of parameters in the query string to build the cache key."""

    user: Optional[ActionParametersCacheKeyCustomKeyUser] = None
    """Characteristics of the request user agent used in building the cache key."""


class ActionParametersCacheKey(BaseModel):
    cache_by_device_type: Optional[bool] = None
    """Separate cached content based on the visitor’s device type"""

    cache_deception_armor: Optional[bool] = None
    """
    Protect from web cache deception attacks while allowing static assets to be
    cached
    """

    custom_key: Optional[ActionParametersCacheKeyCustomKey] = None
    """
    Customize which components of the request are included or excluded from the
    cache key.
    """

    ignore_query_strings_order: Optional[bool] = None
    """
    Treat requests with the same query parameters the same, regardless of the order
    those query parameters are in. A value of true ignores the query strings' order.
    """


class ActionParametersCacheReserve(BaseModel):
    eligible: bool
    """Determines whether cache reserve is enabled.

    If this is true and a request meets eligibility criteria, Cloudflare will write
    the resource to cache reserve.
    """

    minimum_file_size: int
    """The minimum file size eligible for store in cache reserve."""


class ActionParametersEdgeTTLStatusCodeTTLStatusCodeRange(BaseModel):
    from_: int = FieldInfo(alias="from")
    """response status code lower bound"""

    to: int
    """response status code upper bound"""


class ActionParametersEdgeTTLStatusCodeTTL(BaseModel):
    value: int
    """Time to cache a response (in seconds).

    A value of 0 is equivalent to setting the Cache-Control header with the value
    "no-cache". A value of -1 is equivalent to setting Cache-Control header with the
    value of "no-store".
    """

    status_code_range: Optional[ActionParametersEdgeTTLStatusCodeTTLStatusCodeRange] = None
    """The range of status codes used to apply the selected mode."""

    status_code_value: Optional[int] = None
    """Set the ttl for responses with this specific status code"""


class ActionParametersEdgeTTL(BaseModel):
    default: int
    """The TTL (in seconds) if you choose override_origin mode."""

    mode: Literal["respect_origin", "bypass_by_default", "override_origin"]
    """edge ttl options"""

    status_code_ttl: List[ActionParametersEdgeTTLStatusCodeTTL]
    """List of single status codes, or status code ranges to apply the selected mode"""


class ActionParametersServeStale(BaseModel):
    disable_stale_while_updating: bool
    """Defines whether Cloudflare should serve stale content while updating.

    If true, Cloudflare will not serve stale content while getting the latest
    content from the origin.
    """


class ActionParameters(BaseModel):
    additional_cacheable_ports: Optional[List[int]] = None
    """List of additional ports that caching can be enabled on."""

    browser_ttl: Optional[ActionParametersBrowserTTL] = None
    """Specify how long client browsers should cache the response.

    Cloudflare cache purge will not purge content cached on client browsers, so high
    browser TTLs may lead to stale content.
    """

    cache: Optional[bool] = None
    """Mark whether the request’s response from origin is eligible for caching.

    Caching itself will still depend on the cache-control header and your other
    caching configurations.
    """

    cache_key: Optional[ActionParametersCacheKey] = None
    """
    Define which components of the request are included or excluded from the cache
    key Cloudflare uses to store the response in cache.
    """

    cache_reserve: Optional[ActionParametersCacheReserve] = None
    """
    Mark whether the request's response from origin is eligible for Cache Reserve
    (requires a Cache Reserve add-on plan).
    """

    edge_ttl: Optional[ActionParametersEdgeTTL] = None
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

    serve_stale: Optional[ActionParametersServeStale] = None
    """
    Define if Cloudflare should serve stale content while getting the latest content
    from the origin. If on, Cloudflare will not serve stale content while getting
    the latest content from the origin.
    """


class ExposedCredentialCheck(BaseModel):
    password_expression: str
    """Expression that selects the password used in the credentials check."""

    username_expression: str
    """Expression that selects the user ID used in the credentials check."""


class Ratelimit(BaseModel):
    characteristics: List[str]
    """
    Characteristics of the request on which the ratelimiter counter will be
    incremented.
    """

    period: Literal[10, 60, 600, 3600]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: Optional[str] = None
    """Defines when the ratelimit counter should be incremented.

    It is optional and defaults to the same as the rule's expression.
    """

    mitigation_timeout: Optional[int] = None
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: Optional[int] = None
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: Optional[bool] = None
    """Defines if ratelimit counting is only done when an origin is reached."""

    score_per_period: Optional[int] = None
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: Optional[str] = None
    """
    The response header name provided by the origin which should contain the score
    to increment ratelimit counter on.
    """


class SetCacheSettingsRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["set_cache_settings"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[ActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    enabled: Optional[bool] = None
    """Whether the rule should be executed."""

    exposed_credential_check: Optional[ExposedCredentialCheck] = None
    """Configure checks for exposed credentials."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[Ratelimit] = None
    """An object configuring the rule's ratelimit behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule ID by default)."""
