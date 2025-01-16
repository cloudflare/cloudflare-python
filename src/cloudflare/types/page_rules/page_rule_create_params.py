# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .target_param import TargetParam
from ..zones.ssl_param import SSLParam
from ..zones.waf_param import WAFParam
from ..zones.mirage_param import MirageParam
from ..zones.polish_param import PolishParam
from ..zones.cache_level_param import CacheLevelParam
from ..zones.browser_check_param import BrowserCheckParam
from ..zones.rocket_loader_param import RocketLoaderParam
from ..zones.ip_geolocation_param import IPGeolocationParam
from ..zones.security_level_param import SecurityLevelParam
from ..zones.always_use_https_param import AlwaysUseHTTPSParam
from ..zones.browser_cache_ttl_param import BrowserCacheTTLParam
from ..zones.email_obfuscation_param import EmailObfuscationParam
from ..zones.response_buffering_param import ResponseBufferingParam
from ..zones.true_client_ip_header_param import TrueClientIPHeaderParam
from ..zones.automatic_https_rewrites_param import AutomaticHTTPSRewritesParam
from ..zones.opportunistic_encryption_param import OpportunisticEncryptionParam
from ..zones.origin_error_page_pass_thru_param import OriginErrorPagePassThruParam
from ..zones.sort_query_string_for_cache_param import SortQueryStringForCacheParam

__all__ = [
    "PageRuleCreateParams",
    "Action",
    "ActionBypassCacheOnCookie",
    "ActionCacheByDeviceType",
    "ActionCacheDeceptionArmor",
    "ActionCacheKeyFields",
    "ActionCacheKeyFieldsValue",
    "ActionCacheKeyFieldsValueCookie",
    "ActionCacheKeyFieldsValueHeader",
    "ActionCacheKeyFieldsValueHost",
    "ActionCacheKeyFieldsValueQueryString",
    "ActionCacheKeyFieldsValueUser",
    "ActionCacheOnCookie",
    "ActionCacheTTLByStatus",
    "ActionDisableApps",
    "ActionDisablePerformance",
    "ActionDisableSecurity",
    "ActionDisableZaraz",
    "ActionEdgeCacheTTL",
    "ActionExplicitCacheControl",
    "ActionForwardingURL",
    "ActionForwardingURLValue",
    "ActionHostHeaderOverride",
    "ActionResolveOverride",
    "ActionRespectStrongEtag",
]


class PageRuleCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    actions: Required[Iterable[Action]]
    """The set of actions to perform if the targets of this rule match the request.

    Actions can redirect to another URL or override settings, but not both.
    """

    targets: Required[Iterable[TargetParam]]
    """The rule targets to evaluate on each request."""

    priority: int
    """
    The priority of the rule, used to define which Page Rule is processed over
    another. A higher number indicates a higher priority. For example, if you have a
    catch-all Page Rule (rule A: `/images/*`) but want a more specific Page Rule to
    take precedence (rule B: `/images/special/*`), specify a higher priority for
    rule B so it overrides rule A.
    """

    status: Literal["active", "disabled"]
    """The status of the Page Rule."""


class ActionBypassCacheOnCookie(TypedDict, total=False):
    id: Literal["bypass_cache_on_cookie"]
    """
    Bypass cache and fetch resources from the origin server if a regular expression
    matches against a cookie name present in the request.
    """

    value: str
    """The regular expression to use for matching cookie names in the request.

    Refer to
    [Bypass Cache on Cookie setting](https://developers.cloudflare.com/rules/page-rules/reference/additional-reference/#bypass-cache-on-cookie-setting)
    to learn about limited regular expression support.
    """


class ActionCacheByDeviceType(TypedDict, total=False):
    id: Literal["cache_by_device_type"]
    """Separate cached content based on the visitor's device type."""

    value: Literal["on", "off"]
    """The status of Cache By Device Type."""


class ActionCacheDeceptionArmor(TypedDict, total=False):
    id: Literal["cache_deception_armor"]
    """
    Protect from web cache deception attacks while still allowing static assets to
    be cached. This setting verifies that the URL's extension matches the returned
    `Content-Type`.
    """

    value: Literal["on", "off"]
    """The status of Cache Deception Armor."""


class ActionCacheKeyFieldsValueCookie(TypedDict, total=False):
    check_presence: List[str]
    """
    A list of cookies to check for the presence of, without including their actual
    values.
    """

    include: List[str]
    """A list of cookies to include."""


class ActionCacheKeyFieldsValueHeader(TypedDict, total=False):
    check_presence: List[str]
    """
    A list of headers to check for the presence of, without including their actual
    values.
    """

    exclude: List[str]
    """A list of headers to ignore."""

    include: List[str]
    """A list of headers to include."""


class ActionCacheKeyFieldsValueHost(TypedDict, total=False):
    resolved: bool
    """Whether to include the Host header in the HTTP request sent to the origin."""


class ActionCacheKeyFieldsValueQueryString(TypedDict, total=False):
    exclude: Union[Literal["*"], List[str]]
    """Ignore all query string parameters."""

    include: Union[Literal["*"], List[str]]
    """Include all query string parameters."""


class ActionCacheKeyFieldsValueUser(TypedDict, total=False):
    device_type: bool
    """
    Classifies a request as `mobile`, `desktop`, or `tablet` based on the User
    Agent.
    """

    geo: bool
    """Includes the client's country, derived from the IP address."""

    lang: bool
    """
    Includes the first language code contained in the `Accept-Language` header sent
    by the client.
    """


class ActionCacheKeyFieldsValue(TypedDict, total=False):
    cookie: ActionCacheKeyFieldsValueCookie
    """Controls which cookies appear in the Cache Key."""

    header: ActionCacheKeyFieldsValueHeader
    """Controls which headers go into the Cache Key.

    Exactly one of `include` or `exclude` is expected.
    """

    host: ActionCacheKeyFieldsValueHost
    """Determines which host header to include in the Cache Key."""

    query_string: ActionCacheKeyFieldsValueQueryString
    """Controls which URL query string parameters go into the Cache Key.

    Exactly one of `include` or `exclude` is expected.
    """

    user: ActionCacheKeyFieldsValueUser
    """Feature fields to add features about the end-user (client) into the Cache Key."""


class ActionCacheKeyFields(TypedDict, total=False):
    id: Literal["cache_key_fields"]
    """
    Control specifically what variables to include when deciding which resources to
    cache. This allows customers to determine what to cache based on something other
    than just the URL.
    """

    value: ActionCacheKeyFieldsValue


class ActionCacheOnCookie(TypedDict, total=False):
    id: Literal["cache_on_cookie"]
    """
    Apply the Cache Everything option (Cache Level setting) based on a regular
    expression match against a cookie name.
    """

    value: str
    """The regular expression to use for matching cookie names in the request."""


class ActionCacheTTLByStatus(TypedDict, total=False):
    id: Literal["cache_ttl_by_status"]
    """
    Enterprise customers can set cache time-to-live (TTL) based on the response
    status from the origin web server. Cache TTL refers to the duration of a
    resource in the Cloudflare network before being marked as stale or discarded
    from cache. Status codes are returned by a resource's origin. Setting cache TTL
    based on response status overrides the default cache behavior (standard caching)
    for static files and overrides cache instructions sent by the origin web server.
    To cache non-static assets, set a Cache Level of Cache Everything using a Page
    Rule. Setting no-store Cache-Control or a low TTL (using `max-age`/`s-maxage`)
    increases requests to origin web servers and decreases performance.
    """

    value: Dict[str, Union[Literal["no-cache", "no-store"], int]]
    """
    A JSON object containing status codes and their corresponding TTLs. Each
    key-value pair in the cache TTL by status cache rule has the following syntax

    - `status_code`: An integer value such as 200 or 500. status_code matches the
      exact status code from the origin web server. Valid status codes are between
      100-999.
    - `status_code_range`: Integer values for from and to. status_code_range matches
      any status code from the origin web server within the specified range.
    - `value`: An integer value that defines the duration an asset is valid in
      seconds or one of the following strings: no-store (equivalent to -1), no-cache
      (equivalent to 0).
    """


class ActionDisableApps(TypedDict, total=False):
    id: Literal["disable_apps"]
    """
    Turn off all active
    [Cloudflare Apps](https://developers.cloudflare.com/support/more-dashboard-apps/cloudflare-apps/)
    (deprecated).
    """


class ActionDisablePerformance(TypedDict, total=False):
    id: Literal["disable_performance"]
    """
    Turn off
    [Rocket Loader](https://developers.cloudflare.com/speed/optimization/content/rocket-loader/),
    [Mirage](https://developers.cloudflare.com/speed/optimization/images/mirage/),
    and [Polish](https://developers.cloudflare.com/images/polish/).
    """


class ActionDisableSecurity(TypedDict, total=False):
    id: Literal["disable_security"]
    """
    Turn off
    [Email Obfuscation](https://developers.cloudflare.com/waf/tools/scrape-shield/email-address-obfuscation/),
    [Rate Limiting (previous version, deprecated)](https://developers.cloudflare.com/waf/reference/legacy/old-rate-limiting/),
    [Scrape Shield](https://developers.cloudflare.com/waf/tools/scrape-shield/),
    [URL (Zone) Lockdown](https://developers.cloudflare.com/waf/tools/zone-lockdown/),
    and
    [WAF managed rules (previous version, deprecated)](https://developers.cloudflare.com/waf/reference/legacy/old-waf-managed-rules/).
    """


class ActionDisableZaraz(TypedDict, total=False):
    id: Literal["disable_zaraz"]
    """Turn off [Zaraz](https://developers.cloudflare.com/zaraz/)."""


class ActionEdgeCacheTTL(TypedDict, total=False):
    id: Literal["edge_cache_ttl"]
    """Specify how long to cache a resource in the Cloudflare global network.

    _Edge Cache TTL_ is not visible in response headers.
    """

    value: int


class ActionExplicitCacheControl(TypedDict, total=False):
    id: Literal["explicit_cache_control"]
    """
    Origin Cache Control is enabled by default for Free, Pro, and Business domains
    and disabled by default for Enterprise domains.
    """

    value: Literal["on", "off"]
    """The status of Origin Cache Control."""


class ActionForwardingURLValue(TypedDict, total=False):
    status_code: Literal[301, 302]
    """The status code to use for the URL redirect.

    301 is a permanent redirect. 302 is a temporary redirect.
    """

    url: str
    """
    The URL to redirect the request to. Notes: ${num} refers to the position of '\\**'
    in the constraint value.
    """


class ActionForwardingURL(TypedDict, total=False):
    id: Literal["forwarding_url"]
    """Redirects one URL to another using an `HTTP 301/302` redirect.

    Refer to
    [Wildcard matching and referencing](https://developers.cloudflare.com/rules/page-rules/reference/wildcard-matching/).
    """

    value: ActionForwardingURLValue


class ActionHostHeaderOverride(TypedDict, total=False):
    id: Literal["host_header_override"]
    """Apply a specific host header."""

    value: str
    """The hostname to use in the `Host` header"""


class ActionResolveOverride(TypedDict, total=False):
    id: Literal["resolve_override"]
    """Change the origin address to the value specified in this setting."""

    value: str
    """The origin address you want to override with."""


class ActionRespectStrongEtag(TypedDict, total=False):
    id: Literal["respect_strong_etag"]
    """
    Turn on or off byte-for-byte equivalency checks between the Cloudflare cache and
    the origin server.
    """

    value: Literal["on", "off"]
    """The status of Respect Strong ETags"""


Action: TypeAlias = Union[
    AlwaysUseHTTPSParam,
    AutomaticHTTPSRewritesParam,
    BrowserCacheTTLParam,
    BrowserCheckParam,
    ActionBypassCacheOnCookie,
    ActionCacheByDeviceType,
    ActionCacheDeceptionArmor,
    ActionCacheKeyFields,
    CacheLevelParam,
    ActionCacheOnCookie,
    ActionCacheTTLByStatus,
    ActionDisableApps,
    ActionDisablePerformance,
    ActionDisableSecurity,
    ActionDisableZaraz,
    ActionEdgeCacheTTL,
    EmailObfuscationParam,
    ActionExplicitCacheControl,
    ActionForwardingURL,
    ActionHostHeaderOverride,
    IPGeolocationParam,
    MirageParam,
    OpportunisticEncryptionParam,
    OriginErrorPagePassThruParam,
    PolishParam,
    ActionResolveOverride,
    ActionRespectStrongEtag,
    ResponseBufferingParam,
    RocketLoaderParam,
    SecurityLevelParam,
    SortQueryStringForCacheParam,
    SSLParam,
    TrueClientIPHeaderParam,
    WAFParam,
]
