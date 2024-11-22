# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
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
from ..zones.development_mode_param import DevelopmentModeParam
from ..zones.browser_cache_ttl_param import BrowserCacheTTLParam
from ..zones.email_obfuscation_param import EmailObfuscationParam
from ..zones.hotlink_protection_param import HotlinkProtectionParam
from ..zones.response_buffering_param import ResponseBufferingParam
from ..zones.server_side_excludes_param import ServerSideExcludesParam
from ..zones.true_client_ip_header_param import TrueClientIPHeaderParam
from ..zones.automatic_https_rewrites_param import AutomaticHTTPSRewritesParam
from ..zones.opportunistic_encryption_param import OpportunisticEncryptionParam
from ..zones.origin_error_page_pass_thru_param import OriginErrorPagePassThruParam
from ..zones.sort_query_string_for_cache_param import SortQueryStringForCacheParam

__all__ = [
    "PageruleUpdateParams",
    "Action",
    "ActionBypassCacheOnCookie",
    "ActionCacheByDeviceType",
    "ActionCacheDeceptionArmor",
    "ActionCacheKey",
    "ActionCacheKeyValue",
    "ActionCacheKeyValueCookie",
    "ActionCacheKeyValueHeader",
    "ActionCacheKeyValueHost",
    "ActionCacheKeyValueQueryString",
    "ActionCacheKeyValueUser",
    "ActionCacheKeyFields",
    "ActionCacheOnCookie",
    "ActionCacheTTLByStatus",
    "ActionDDoSProtection",
    "ActionDisableApps",
    "ActionDisablePerformance",
    "ActionDisableSecurity",
    "ActionDisableZaraz",
    "ActionEdgeCacheTTL",
    "ActionExplicitCacheControl",
    "ActionForwardingURL",
    "ActionForwardingURLValue",
    "ActionHostHeaderOverride",
    "ActionMinify",
    "ActionPurgeByPageRule",
    "ActionResolveOverride",
    "ActionRespectStrongEtag",
]


class PageruleUpdateParams(TypedDict, total=False):
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


class ActionCacheKeyValueCookie(TypedDict, total=False):
    check_presence: List[str]
    """
    A list of cookies to check for the presence of, without including their actual
    values.
    """

    include: List[str]
    """A list of cookies to include."""


class ActionCacheKeyValueHeader(TypedDict, total=False):
    check_presence: List[str]
    """
    A list of headers to check for the presence of, without including their actual
    values.
    """

    exclude: List[str]
    """A list of headers to ignore."""

    include: List[str]
    """A list of headers to include."""


class ActionCacheKeyValueHost(TypedDict, total=False):
    resolved: bool
    """Whether to include the Host header in the HTTP request sent to the origin."""


class ActionCacheKeyValueQueryString(TypedDict, total=False):
    exclude: Union[Literal["*"], List[str]]
    """Ignore all query string parameters."""

    include: Union[Literal["*"], List[str]]
    """Include all query string parameters."""


class ActionCacheKeyValueUser(TypedDict, total=False):
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


class ActionCacheKeyValue(TypedDict, total=False):
    cookie: ActionCacheKeyValueCookie
    """Controls which cookies appear in the Cache Key."""

    header: ActionCacheKeyValueHeader
    """Controls which headers go into the Cache Key.

    Exactly one of `include` or `exclude` is expected.
    """

    host: ActionCacheKeyValueHost
    """Determines which host header to include in the Cache Key."""

    query_string: ActionCacheKeyValueQueryString
    """Controls which URL query string parameters go into the Cache Key.

    Exactly one of `include` or `exclude` is expected.
    """

    user: ActionCacheKeyValueUser
    """Feature fields to add features about the end-user (client) into the Cache Key."""


class ActionCacheKey(TypedDict, total=False):
    id: Literal["cache_key"]
    """
    Control specifically what variables to include when deciding which resources to
    cache. This allows customers to determine what to cache based on something other
    than just the URL.
    """

    value: ActionCacheKeyValue


class ActionCacheKeyFields(TypedDict, total=False):
    id: Literal["cache_key_fields"]


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


class ActionDDoSProtection(TypedDict, total=False):
    id: Literal["ddos_protection"]


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


class ActionMinify(TypedDict, total=False):
    id: Literal["minify"]


class ActionPurgeByPageRule(TypedDict, total=False):
    id: Literal["purge_by_page_rule"]


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
    ActionCacheKey,
    ActionCacheKeyFields,
    CacheLevelParam,
    ActionCacheOnCookie,
    ActionCacheTTLByStatus,
    ActionDDoSProtection,
    DevelopmentModeParam,
    ActionDisableApps,
    ActionDisablePerformance,
    ActionDisableSecurity,
    ActionDisableZaraz,
    ActionEdgeCacheTTL,
    EmailObfuscationParam,
    ActionExplicitCacheControl,
    ActionForwardingURL,
    ActionHostHeaderOverride,
    HotlinkProtectionParam,
    IPGeolocationParam,
    ActionMinify,
    MirageParam,
    OpportunisticEncryptionParam,
    OriginErrorPagePassThruParam,
    PolishParam,
    ActionPurgeByPageRule,
    ActionResolveOverride,
    ActionRespectStrongEtag,
    ResponseBufferingParam,
    RocketLoaderParam,
    SecurityLevelParam,
    ServerSideExcludesParam,
    SortQueryStringForCacheParam,
    SSLParam,
    TrueClientIPHeaderParam,
    WAFParam,
]
