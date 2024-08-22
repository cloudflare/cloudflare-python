# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing_extensions import Literal

from typing import Optional, List, Dict

from datetime import datetime

from .logging import Logging

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["SetCacheSettingsRule", "ActionParameters", "ActionParametersBrowserTTL", "ActionParametersCacheKey", "ActionParametersCacheKeyCustomKey", "ActionParametersCacheKeyCustomKeyCookie", "ActionParametersCacheKeyCustomKeyHeader", "ActionParametersCacheKeyCustomKeyHost", "ActionParametersCacheKeyCustomKeyQueryString", "ActionParametersCacheKeyCustomKeyQueryStringExclude", "ActionParametersCacheKeyCustomKeyQueryStringInclude", "ActionParametersCacheKeyCustomKeyUser", "ActionParametersCacheReserve", "ActionParametersEdgeTTL", "ActionParametersEdgeTTLStatusCodeTTL", "ActionParametersEdgeTTLStatusCodeTTLStatusCodeRange", "ActionParametersServeStale"]

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

class ActionParametersCacheKeyCustomKeyQueryStringExclude(BaseModel):
    all: Optional[bool] = None
    """Exclude all query string parameters from use in building the cache key."""

    rule_list: Optional[List[str]] = FieldInfo(alias = "list", default = None)
    """A list of query string parameters NOT used to build the cache key.

    All parameters present in the request but missing in this list will be used to
    build the cache key.
    """

class ActionParametersCacheKeyCustomKeyQueryStringInclude(BaseModel):
    all: Optional[bool] = None
    """Use all query string parameters in the cache key."""

    rule_list: Optional[List[str]] = FieldInfo(alias = "list", default = None)
    """A list of query string parameters used to build the cache key."""

class ActionParametersCacheKeyCustomKeyQueryString(BaseModel):
    exclude: Optional[ActionParametersCacheKeyCustomKeyQueryStringExclude] = None
    """
    build the cache key using all query string parameters EXCECPT these excluded
    parameters
    """

    include: Optional[ActionParametersCacheKeyCustomKeyQueryStringInclude] = None
    """
    build the cache key using a list of query string parameters that ARE in the
    request.
    """

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
    """
    Use the presence or absence of parameters in the query string to build the cache
    key.
    """

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

    min_file_size: int
    """The minimum file size eligible for store in cache reserve."""

class ActionParametersEdgeTTLStatusCodeTTLStatusCodeRange(BaseModel):
    from_: int = FieldInfo(alias = "from")
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

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule ID by default)."""