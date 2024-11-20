# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .target import Target
from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..zones.ssl import SSL
from ..zones.waf import WAF
from ..zones.mirage import Mirage
from ..zones.polish import Polish
from ..zones.cache_level import CacheLevel
from ..zones.browser_check import BrowserCheck
from ..zones.rocket_loader import RocketLoader
from ..zones.ip_geolocation import IPGeolocation
from ..zones.security_level import SecurityLevel
from ..zones.always_use_https import AlwaysUseHTTPS
from ..zones.development_mode import DevelopmentMode
from ..zones.browser_cache_ttl import BrowserCacheTTL
from ..zones.email_obfuscation import EmailObfuscation
from ..zones.hotlink_protection import HotlinkProtection
from ..zones.response_buffering import ResponseBuffering
from ..zones.server_side_excludes import ServerSideExcludes
from ..zones.true_client_ip_header import TrueClientIPHeader
from ..zones.automatic_https_rewrites import AutomaticHTTPSRewrites
from ..zones.opportunistic_encryption import OpportunisticEncryption
from ..zones.origin_error_page_pass_thru import OriginErrorPagePassThru
from ..zones.sort_query_string_for_cache import SortQueryStringForCache

__all__ = [
    "PageRule",
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
    "ActionResolveOverrideValue",
    "ActionRespectStrongEtag",
]


class ActionBypassCacheOnCookie(BaseModel):
    id: Optional[Literal["bypass_cache_on_cookie"]] = None
    """
    Bypass cache and fetch resources from the origin server if a regular expression
    matches against a cookie name present in the request.
    """

    value: Optional[str] = None
    """The regular expression to use for matching cookie names in the request.

    Refer to
    [Bypass Cache on Cookie setting](https://developers.cloudflare.com/rules/page-rules/reference/additional-reference/#bypass-cache-on-cookie-setting)
    to learn about limited regular expression support.
    """


class ActionCacheByDeviceType(BaseModel):
    id: Optional[Literal["cache_by_device_type"]] = None
    """Separate cached content based on the visitor's device type."""

    value: Optional[Literal["on", "off"]] = None
    """The status of Cache By Device Type."""


class ActionCacheDeceptionArmor(BaseModel):
    id: Optional[Literal["cache_deception_armor"]] = None
    """
    Protect from web cache deception attacks while still allowing static assets to
    be cached. This setting verifies that the URL's extension matches the returned
    `Content-Type`.
    """

    value: Optional[Literal["on", "off"]] = None
    """The status of Cache Deception Armor."""


class ActionCacheKeyValueCookie(BaseModel):
    check_presence: Optional[List[str]] = None
    """
    A list of cookies to check for the presence of, without including their actual
    values.
    """

    include: Optional[List[str]] = None
    """A list of cookies to include."""


class ActionCacheKeyValueHeader(BaseModel):
    check_presence: Optional[List[str]] = None
    """
    A list of headers to check for the presence of, without including their actual
    values.
    """

    exclude: Optional[List[str]] = None
    """A list of headers to ignore."""

    include: Optional[List[str]] = None
    """A list of headers to include."""


class ActionCacheKeyValueHost(BaseModel):
    resolved: Optional[bool] = None
    """Whether to include the Host header in the HTTP request sent to the origin."""


class ActionCacheKeyValueQueryString(BaseModel):
    exclude: Union[Literal["*"], List[str], None] = None
    """Ignore all query string parameters."""

    include: Union[Literal["*"], List[str], None] = None
    """Include all query string parameters."""


class ActionCacheKeyValueUser(BaseModel):
    device_type: Optional[bool] = None
    """
    Classifies a request as `mobile`, `desktop`, or `tablet` based on the User
    Agent.
    """

    geo: Optional[bool] = None
    """Includes the client's country, derived from the IP address."""

    lang: Optional[bool] = None
    """
    Includes the first language code contained in the `Accept-Language` header sent
    by the client.
    """


class ActionCacheKeyValue(BaseModel):
    cookie: Optional[ActionCacheKeyValueCookie] = None
    """Controls which cookies appear in the Cache Key."""

    header: Optional[ActionCacheKeyValueHeader] = None
    """Controls which headers go into the Cache Key.

    Exactly one of `include` or `exclude` is expected.
    """

    host: Optional[ActionCacheKeyValueHost] = None
    """Determines which host header to include in the Cache Key."""

    query_string: Optional[ActionCacheKeyValueQueryString] = None
    """Controls which URL query string parameters go into the Cache Key.

    Exactly one of `include` or `exclude` is expected.
    """

    user: Optional[ActionCacheKeyValueUser] = None
    """Feature fields to add features about the end-user (client) into the Cache Key."""


class ActionCacheKey(BaseModel):
    id: Optional[Literal["cache_key"]] = None
    """
    Control specifically what variables to include when deciding which resources to
    cache. This allows customers to determine what to cache based on something other
    than just the URL.
    """

    value: Optional[ActionCacheKeyValue] = None


class ActionCacheKeyFields(BaseModel):
    id: Optional[Literal["cache_key_fields"]] = None


class ActionCacheOnCookie(BaseModel):
    id: Optional[Literal["cache_on_cookie"]] = None


class ActionCacheTTLByStatus(BaseModel):
    id: Optional[Literal["cache_ttl_by_status"]] = None


class ActionDDoSProtection(BaseModel):
    id: Optional[Literal["ddos_protection"]] = None


class ActionDisableApps(BaseModel):
    id: Optional[Literal["disable_apps"]] = None
    """
    Turn off all active
    [Cloudflare Apps](https://developers.cloudflare.com/support/more-dashboard-apps/cloudflare-apps/)
    (deprecated).
    """


class ActionDisablePerformance(BaseModel):
    id: Optional[Literal["disable_performance"]] = None
    """
    Turn off
    [Rocket Loader](https://developers.cloudflare.com/speed/optimization/content/rocket-loader/),
    [Mirage](https://developers.cloudflare.com/speed/optimization/images/mirage/),
    and [Polish](https://developers.cloudflare.com/images/polish/).
    """


class ActionDisableSecurity(BaseModel):
    id: Optional[Literal["disable_security"]] = None
    """
    Turn off
    [Email Obfuscation](https://developers.cloudflare.com/waf/tools/scrape-shield/email-address-obfuscation/),
    [Rate Limiting (previous version, deprecated)](https://developers.cloudflare.com/waf/reference/legacy/old-rate-limiting/),
    [Scrape Shield](https://developers.cloudflare.com/waf/tools/scrape-shield/),
    [URL (Zone) Lockdown](https://developers.cloudflare.com/waf/tools/zone-lockdown/),
    and
    [WAF managed rules (previous version, deprecated)](https://developers.cloudflare.com/waf/reference/legacy/old-waf-managed-rules/).
    """


class ActionDisableZaraz(BaseModel):
    id: Optional[Literal["disable_zaraz"]] = None
    """Turn off [Zaraz](https://developers.cloudflare.com/zaraz/)."""


class ActionEdgeCacheTTL(BaseModel):
    id: Optional[Literal["edge_cache_ttl"]] = None
    """Specify how long to cache a resource in the Cloudflare global network.

    _Edge Cache TTL_ is not visible in response headers.
    """

    value: Optional[int] = None


class ActionExplicitCacheControl(BaseModel):
    id: Optional[Literal["explicit_cache_control"]] = None


class ActionForwardingURLValue(BaseModel):
    status_code: Optional[Literal[301, 302]] = None
    """The status code to use for the URL redirect.

    301 is a permanent redirect. 302 is a temporary redirect.
    """

    url: Optional[str] = None
    """
    The URL to redirect the request to. Notes: ${num} refers to the position of '\\**'
    in the constraint value.
    """


class ActionForwardingURL(BaseModel):
    id: Optional[Literal["forwarding_url"]] = None
    """Redirects one URL to another using an `HTTP 301/302` redirect.

    Refer to
    [Wildcard matching and referencing](https://developers.cloudflare.com/rules/page-rules/reference/wildcard-matching/).
    """

    value: Optional[ActionForwardingURLValue] = None


class ActionHostHeaderOverride(BaseModel):
    id: Optional[Literal["host_header_override"]] = None
    """Apply a specific host header."""

    value: Optional[str] = None
    """The hostname to use in the `Host` header"""


class ActionMinify(BaseModel):
    id: Optional[Literal["minify"]] = None


class ActionPurgeByPageRule(BaseModel):
    id: Optional[Literal["purge_by_page_rule"]] = None


class ActionResolveOverrideValue(BaseModel):
    value: Optional[str] = None
    """The origin address you want to override with."""


class ActionResolveOverride(BaseModel):
    id: Optional[Literal["resolve_override"]] = None
    """Change the origin address to the value specified in this setting."""

    value: Optional[ActionResolveOverrideValue] = None


class ActionRespectStrongEtag(BaseModel):
    id: Optional[Literal["respect_strong_etag"]] = None
    """
    Turn on or off byte-for-byte equivalency checks between the Cloudflare cache and
    the origin server.
    """

    value: Optional[Literal["on", "off"]] = None
    """The status of Respect Strong ETags"""


Action: TypeAlias = Annotated[
    Union[
        AlwaysUseHTTPS,
        AutomaticHTTPSRewrites,
        BrowserCacheTTL,
        BrowserCheck,
        ActionBypassCacheOnCookie,
        ActionCacheByDeviceType,
        ActionCacheDeceptionArmor,
        ActionCacheKey,
        ActionCacheKeyFields,
        CacheLevel,
        ActionCacheOnCookie,
        ActionCacheTTLByStatus,
        ActionDDoSProtection,
        DevelopmentMode,
        ActionDisableApps,
        ActionDisablePerformance,
        ActionDisableSecurity,
        ActionDisableZaraz,
        ActionEdgeCacheTTL,
        EmailObfuscation,
        ActionExplicitCacheControl,
        ActionForwardingURL,
        ActionHostHeaderOverride,
        HotlinkProtection,
        IPGeolocation,
        ActionMinify,
        Mirage,
        OpportunisticEncryption,
        OriginErrorPagePassThru,
        Polish,
        ActionPurgeByPageRule,
        ActionResolveOverride,
        ActionRespectStrongEtag,
        ResponseBuffering,
        RocketLoader,
        SecurityLevel,
        ServerSideExcludes,
        SortQueryStringForCache,
        SSL,
        TrueClientIPHeader,
        WAF,
    ],
    PropertyInfo(discriminator="id"),
]


class PageRule(BaseModel):
    id: str
    """Identifier"""

    actions: List[Action]
    """The set of actions to perform if the targets of this rule match the request.

    Actions can redirect to another URL or override settings, but not both.
    """

    created_on: datetime
    """The timestamp of when the Page Rule was created."""

    modified_on: datetime
    """The timestamp of when the Page Rule was last modified."""

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

    targets: List[Target]
    """The rule targets to evaluate on each request."""
