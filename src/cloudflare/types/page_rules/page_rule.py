# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
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
from ..zones.browser_cache_ttl import BrowserCacheTTL
from ..zones.email_obfuscation import EmailObfuscation
from ..zones.response_buffering import ResponseBuffering
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


class ActionCacheKeyFieldsValueCookie(BaseModel):
    check_presence: Optional[List[str]] = None
    """
    A list of cookies to check for the presence of, without including their actual
    values.
    """

    include: Optional[List[str]] = None
    """A list of cookies to include."""


class ActionCacheKeyFieldsValueHeader(BaseModel):
    check_presence: Optional[List[str]] = None
    """
    A list of headers to check for the presence of, without including their actual
    values.
    """

    exclude: Optional[List[str]] = None
    """A list of headers to ignore."""

    include: Optional[List[str]] = None
    """A list of headers to include."""


class ActionCacheKeyFieldsValueHost(BaseModel):
    resolved: Optional[bool] = None
    """Whether to include the Host header in the HTTP request sent to the origin."""


class ActionCacheKeyFieldsValueQueryString(BaseModel):
    exclude: Union[Literal["*"], List[str], None] = None
    """Ignore all query string parameters."""

    include: Union[Literal["*"], List[str], None] = None
    """Include all query string parameters."""


class ActionCacheKeyFieldsValueUser(BaseModel):
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


class ActionCacheKeyFieldsValue(BaseModel):
    cookie: Optional[ActionCacheKeyFieldsValueCookie] = None
    """Controls which cookies appear in the Cache Key."""

    header: Optional[ActionCacheKeyFieldsValueHeader] = None
    """Controls which headers go into the Cache Key.

    Exactly one of `include` or `exclude` is expected.
    """

    host: Optional[ActionCacheKeyFieldsValueHost] = None
    """Determines which host header to include in the Cache Key."""

    query_string: Optional[ActionCacheKeyFieldsValueQueryString] = None
    """Controls which URL query string parameters go into the Cache Key.

    Exactly one of `include` or `exclude` is expected.
    """

    user: Optional[ActionCacheKeyFieldsValueUser] = None
    """Feature fields to add features about the end-user (client) into the Cache Key."""


class ActionCacheKeyFields(BaseModel):
    id: Optional[Literal["cache_key_fields"]] = None
    """
    Control specifically what variables to include when deciding which resources to
    cache. This allows customers to determine what to cache based on something other
    than just the URL.
    """

    value: Optional[ActionCacheKeyFieldsValue] = None


class ActionCacheOnCookie(BaseModel):
    id: Optional[Literal["cache_on_cookie"]] = None
    """
    Apply the Cache Everything option (Cache Level setting) based on a regular
    expression match against a cookie name.
    """

    value: Optional[str] = None
    """The regular expression to use for matching cookie names in the request."""


class ActionCacheTTLByStatus(BaseModel):
    id: Optional[Literal["cache_ttl_by_status"]] = None
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

    value: Optional[Dict[str, Union[Literal["no-cache", "no-store"], int]]] = None
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
    """
    Origin Cache Control is enabled by default for Free, Pro, and Business domains
    and disabled by default for Enterprise domains.
    """

    value: Optional[Literal["on", "off"]] = None
    """The status of Origin Cache Control."""


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


class ActionResolveOverride(BaseModel):
    id: Optional[Literal["resolve_override"]] = None
    """Change the origin address to the value specified in this setting."""

    value: Optional[str] = None
    """The origin address you want to override with."""


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
        ActionCacheKeyFields,
        CacheLevel,
        ActionCacheOnCookie,
        ActionCacheTTLByStatus,
        ActionDisableApps,
        ActionDisablePerformance,
        ActionDisableSecurity,
        ActionDisableZaraz,
        ActionEdgeCacheTTL,
        EmailObfuscation,
        ActionExplicitCacheControl,
        ActionForwardingURL,
        ActionHostHeaderOverride,
        IPGeolocation,
        Mirage,
        OpportunisticEncryption,
        OriginErrorPagePassThru,
        Polish,
        ActionResolveOverride,
        ActionRespectStrongEtag,
        ResponseBuffering,
        RocketLoader,
        SecurityLevel,
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
