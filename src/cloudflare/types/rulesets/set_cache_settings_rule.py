# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

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


class ActionParametersBrowserTTL(BaseModel):
    mode: Literal["respect_origin", "bypass_by_default", "override_origin", "bypass"]
    """The browser TTL mode."""

    default: Optional[int] = None
    """The browser TTL (in seconds) if you choose the "override_origin" mode."""


class ActionParametersCacheKeyCustomKeyCookie(BaseModel):
    check_presence: Optional[List[str]] = None
    """A list of cookies to check for the presence of.

    The presence of these cookies is included in the cache key.
    """

    include: Optional[List[str]] = None
    """A list of cookies to include in the cache key."""


class ActionParametersCacheKeyCustomKeyHeader(BaseModel):
    check_presence: Optional[List[str]] = None
    """A list of headers to check for the presence of.

    The presence of these headers is included in the cache key.
    """

    contains: Optional[Dict[str, List[str]]] = None
    """A mapping of header names to a list of values.

    If a header is present in the request and contains any of the values provided,
    its value is included in the cache key.
    """

    exclude_origin: Optional[bool] = None
    """Whether to exclude the origin header in the cache key."""

    include: Optional[List[str]] = None
    """A list of headers to include in the cache key."""


class ActionParametersCacheKeyCustomKeyHost(BaseModel):
    resolved: Optional[bool] = None
    """Whether to use the resolved host in the cache key."""


class ActionParametersCacheKeyCustomKeyQueryStringExclude(BaseModel):
    all: Optional[Literal[True]] = None
    """Whether to exclude all query string parameters from the cache key."""

    rule_list: Optional[List[str]] = FieldInfo(alias="list", default=None)
    """A list of query string parameters to exclude from the cache key."""


class ActionParametersCacheKeyCustomKeyQueryStringInclude(BaseModel):
    all: Optional[Literal[True]] = None
    """Whether to include all query string parameters in the cache key."""

    rule_list: Optional[List[str]] = FieldInfo(alias="list", default=None)
    """A list of query string parameters to include in the cache key."""


class ActionParametersCacheKeyCustomKeyQueryString(BaseModel):
    exclude: Optional[ActionParametersCacheKeyCustomKeyQueryStringExclude] = None
    """Which query string parameters to exclude from the cache key."""

    include: Optional[ActionParametersCacheKeyCustomKeyQueryStringInclude] = None
    """Which query string parameters to include in the cache key."""


class ActionParametersCacheKeyCustomKeyUser(BaseModel):
    device_type: Optional[bool] = None
    """Whether to use the user agent's device type in the cache key."""

    geo: Optional[bool] = None
    """Whether to use the user agents's country in the cache key."""

    lang: Optional[bool] = None
    """Whether to use the user agent's language in the cache key."""


class ActionParametersCacheKeyCustomKey(BaseModel):
    cookie: Optional[ActionParametersCacheKeyCustomKeyCookie] = None
    """Which cookies to include in the cache key."""

    header: Optional[ActionParametersCacheKeyCustomKeyHeader] = None
    """Which headers to include in the cache key."""

    host: Optional[ActionParametersCacheKeyCustomKeyHost] = None
    """How to use the host in the cache key."""

    query_string: Optional[ActionParametersCacheKeyCustomKeyQueryString] = None
    """Which query string parameters to include in or exclude from the cache key."""

    user: Optional[ActionParametersCacheKeyCustomKeyUser] = None
    """How to use characteristics of the request user agent in the cache key."""


class ActionParametersCacheKey(BaseModel):
    cache_by_device_type: Optional[bool] = None
    """Whether to separate cached content based on the visitor's device type."""

    cache_deception_armor: Optional[bool] = None
    """
    Whether to protect from web cache deception attacks, while allowing static
    assets to be cached.
    """

    custom_key: Optional[ActionParametersCacheKeyCustomKey] = None
    """Which components of the request are included or excluded from the cache key."""

    ignore_query_strings_order: Optional[bool] = None
    """
    Whether to treat requests with the same query parameters the same, regardless of
    the order those query parameters are in.
    """


class ActionParametersCacheReserve(BaseModel):
    eligible: bool
    """Whether Cache Reserve is enabled.

    If this is true and a request meets eligibility criteria, Cloudflare will write
    the resource to Cache Reserve.
    """

    minimum_file_size: Optional[int] = None
    """The minimum file size eligible for storage in Cache Reserve."""


class ActionParametersEdgeTTLStatusCodeTTLStatusCodeRange(BaseModel):
    from_: Optional[int] = FieldInfo(alias="from", default=None)
    """The lower bound of the range."""

    to: Optional[int] = None
    """The upper bound of the range."""


class ActionParametersEdgeTTLStatusCodeTTL(BaseModel):
    value: int
    """The time to cache the response for (in seconds).

    A value of 0 is equivalent to setting the cache control header with the value
    "no-cache". A value of -1 is equivalent to setting the cache control header with
    the value of "no-store".
    """

    status_code: Optional[int] = None
    """A single status code to apply the TTL to."""

    status_code_range: Optional[ActionParametersEdgeTTLStatusCodeTTLStatusCodeRange] = None
    """A range of status codes to apply the TTL to."""


class ActionParametersEdgeTTL(BaseModel):
    mode: Literal["respect_origin", "bypass_by_default", "override_origin"]
    """The edge TTL mode."""

    default: Optional[int] = None
    """The edge TTL (in seconds) if you choose the "override_origin" mode."""

    status_code_ttl: Optional[List[ActionParametersEdgeTTLStatusCodeTTL]] = None
    """A list of TTLs to apply to specific status codes or status code ranges."""


class ActionParametersServeStale(BaseModel):
    disable_stale_while_updating: Optional[bool] = None
    """
    Whether Cloudflare should disable serving stale content while getting the latest
    content from the origin.
    """


class ActionParameters(BaseModel):
    additional_cacheable_ports: Optional[List[int]] = None
    """A list of additional ports that caching should be enabled on."""

    browser_ttl: Optional[ActionParametersBrowserTTL] = None
    """How long client browsers should cache the response.

    Cloudflare cache purge will not purge content cached on client browsers, so high
    browser TTLs may lead to stale content.
    """

    cache: Optional[bool] = None
    """Whether the request's response from the origin is eligible for caching.

    Caching itself will still depend on the cache control header and your other
    caching configurations.
    """

    cache_key: Optional[ActionParametersCacheKey] = None
    """
    Which components of the request are included in or excluded from the cache key
    Cloudflare uses to store the response in cache.
    """

    cache_reserve: Optional[ActionParametersCacheReserve] = None
    """
    Settings to determine whether the request's response from origin is eligible for
    Cache Reserve (requires a Cache Reserve add-on plan).
    """

    edge_ttl: Optional[ActionParametersEdgeTTL] = None
    """How long the Cloudflare edge network should cache the response."""

    origin_cache_control: Optional[bool] = None
    """Whether Cloudflare will aim to strictly adhere to RFC 7234."""

    origin_error_page_passthru: Optional[bool] = None
    """Whether to generate Cloudflare error pages for issues from the origin server."""

    read_timeout: Optional[int] = None
    """
    A timeout value between two successive read operations to use for your origin
    server. Historically, the timeout value between two read options from Cloudflare
    to an origin server is 100 seconds. If you are attempting to reduce HTTP 524
    errors because of timeouts from an origin server, try increasing this timeout
    value.
    """

    respect_strong_etags: Optional[bool] = None
    """Whether Cloudflare should respect strong ETag (entity tag) headers.

    If false, Cloudflare converts strong ETag headers to weak ETag headers.
    """

    serve_stale: Optional[ActionParametersServeStale] = None
    """When to serve stale content from cache."""


class ExposedCredentialCheck(BaseModel):
    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class Ratelimit(BaseModel):
    characteristics: List[str]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: int
    """Period in seconds over which the counter is being incremented."""

    counting_expression: Optional[str] = None
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
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
    """Whether counting is only performed when an origin is reached."""

    score_per_period: Optional[int] = None
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: Optional[str] = None
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
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
    """Configuration for exposed credential checking."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[Ratelimit] = None
    """An object configuring the rule's rate limit behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule's ID by default)."""
