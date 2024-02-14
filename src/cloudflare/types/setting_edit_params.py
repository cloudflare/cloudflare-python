# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Iterable, List, Optional, Union

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = [
    "SettingEditParams",
    "Item",
    "ItemZones0rtt",
    "ItemZonesAdvancedDDOS",
    "ItemZonesAlwaysOnline",
    "ItemZonesAlwaysUseHTTPs",
    "ItemZonesAutomaticHTTPsRewrites",
    "ItemZonesBrotli",
    "ItemZonesBrowserCacheTTL",
    "ItemZonesBrowserCheck",
    "ItemZonesCacheLevel",
    "ItemZonesChallengeTTL",
    "ItemZonesCiphers",
    "ItemZonesCnameFlattening",
    "ItemZonesDevelopmentMode",
    "ItemZonesEarlyHints",
    "ItemZonesEdgeCacheTTL",
    "ItemZonesEmailObfuscation",
    "ItemZonesH2Prioritization",
    "ItemZonesHotlinkProtection",
    "ItemZonesHTTP2",
    "ItemZonesHTTP3",
    "ItemZonesImageResizing",
    "ItemZonesIPGeolocation",
    "ItemZonesIPV6",
    "ItemZonesMaxUpload",
    "ItemZonesMinTLSVersion",
    "ItemZonesMinify",
    "ItemZonesMinifyValue",
    "ItemZonesMirage",
    "ItemZonesMobileRedirect",
    "ItemZonesMobileRedirectValue",
    "ItemZonesNEL",
    "ItemZonesNELValue",
    "ItemZonesOpportunisticEncryption",
    "ItemZonesOpportunisticOnion",
    "ItemZonesOrangeToOrange",
    "ItemZonesOriginErrorPagePassThru",
    "ItemZonesPolish",
    "ItemZonesPrefetchPreload",
    "ItemZonesProxyReadTimeout",
    "ItemZonesPseudoIPV4",
    "ItemZonesResponseBuffering",
    "ItemZonesRocketLoader",
    "ItemZonesSchemasAutomaticPlatformOptimization",
    "ItemZonesSchemasAutomaticPlatformOptimizationValue",
    "ItemZonesSecurityHeader",
    "ItemZonesSecurityHeaderValue",
    "ItemZonesSecurityHeaderValueStrictTransportSecurity",
    "ItemZonesSecurityLevel",
    "ItemZonesServerSideExclude",
    "ItemZonesSha1Support",
    "ItemZonesSortQueryStringForCache",
    "ItemZonesSSL",
    "ItemZonesSSLRecommender",
    "ItemZonesTLS1_2Only",
    "ItemZonesTLS1_3",
    "ItemZonesTLSClientAuth",
    "ItemZonesTrueClientIPHeader",
    "ItemZonesWAF",
    "ItemZonesWebp",
    "ItemZonesWebsockets",
]


class SettingEditParams(TypedDict, total=False):
    items: Required[Iterable[Item]]
    """One or more zone setting objects. Must contain an ID and a value."""


class ItemZones0rtt(TypedDict, total=False):
    id: Required[Literal["0rtt"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesAdvancedDDOS(TypedDict, total=False):
    id: Required[Literal["advanced_ddos"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesAlwaysOnline(TypedDict, total=False):
    id: Required[Literal["always_online"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesAlwaysUseHTTPs(TypedDict, total=False):
    id: Required[Literal["always_use_https"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesAutomaticHTTPsRewrites(TypedDict, total=False):
    id: Required[Literal["automatic_https_rewrites"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesBrotli(TypedDict, total=False):
    id: Required[Literal["brotli"]]
    """ID of the zone setting."""

    value: Required[Literal["off", "on"]]
    """Current value of the zone setting."""


class ItemZonesBrowserCacheTTL(TypedDict, total=False):
    id: Required[Literal["browser_cache_ttl"]]
    """ID of the zone setting."""

    value: Required[
        Literal[
            0,
            30,
            60,
            120,
            300,
            1200,
            1800,
            3600,
            7200,
            10800,
            14400,
            18000,
            28800,
            43200,
            57600,
            72000,
            86400,
            172800,
            259200,
            345600,
            432000,
            691200,
            1382400,
            2073600,
            2678400,
            5356800,
            16070400,
            31536000,
        ]
    ]
    """Current value of the zone setting."""


class ItemZonesBrowserCheck(TypedDict, total=False):
    id: Required[Literal["browser_check"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesCacheLevel(TypedDict, total=False):
    id: Required[Literal["cache_level"]]
    """ID of the zone setting."""

    value: Required[Literal["aggressive", "basic", "simplified"]]
    """Current value of the zone setting."""


class ItemZonesChallengeTTL(TypedDict, total=False):
    id: Required[Literal["challenge_ttl"]]
    """ID of the zone setting."""

    value: Required[
        Literal[300, 900, 1800, 2700, 3600, 7200, 10800, 14400, 28800, 57600, 86400, 604800, 2592000, 31536000]
    ]
    """Current value of the zone setting."""


class ItemZonesCiphers(TypedDict, total=False):
    id: Required[Literal["ciphers"]]
    """ID of the zone setting."""

    value: Required[List[str]]
    """Current value of the zone setting."""


class ItemZonesCnameFlattening(TypedDict, total=False):
    id: Required[Literal["cname_flattening"]]
    """How to flatten the cname destination."""

    value: Required[Literal["flatten_at_root", "flatten_all"]]
    """Current value of the zone setting."""


class ItemZonesDevelopmentMode(TypedDict, total=False):
    id: Required[Literal["development_mode"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesEarlyHints(TypedDict, total=False):
    id: Required[Literal["early_hints"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesEdgeCacheTTL(TypedDict, total=False):
    id: Required[Literal["edge_cache_ttl"]]
    """ID of the zone setting."""

    value: Required[
        Literal[
            30,
            60,
            300,
            1200,
            1800,
            3600,
            7200,
            10800,
            14400,
            18000,
            28800,
            43200,
            57600,
            72000,
            86400,
            172800,
            259200,
            345600,
            432000,
            518400,
            604800,
        ]
    ]
    """Current value of the zone setting."""


class ItemZonesEmailObfuscation(TypedDict, total=False):
    id: Required[Literal["email_obfuscation"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesH2Prioritization(TypedDict, total=False):
    id: Required[Literal["h2_prioritization"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off", "custom"]]
    """Current value of the zone setting."""


class ItemZonesHotlinkProtection(TypedDict, total=False):
    id: Required[Literal["hotlink_protection"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesHTTP2(TypedDict, total=False):
    id: Required[Literal["http2"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesHTTP3(TypedDict, total=False):
    id: Required[Literal["http3"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesImageResizing(TypedDict, total=False):
    id: Required[Literal["image_resizing"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off", "open"]]
    """Current value of the zone setting."""


class ItemZonesIPGeolocation(TypedDict, total=False):
    id: Required[Literal["ip_geolocation"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesIPV6(TypedDict, total=False):
    id: Required[Literal["ipv6"]]
    """ID of the zone setting."""

    value: Required[Literal["off", "on"]]
    """Current value of the zone setting."""


class ItemZonesMaxUpload(TypedDict, total=False):
    id: Required[Literal["max_upload"]]
    """identifier of the zone setting."""

    value: Required[Literal[100, 200, 500]]
    """Current value of the zone setting."""


class ItemZonesMinTLSVersion(TypedDict, total=False):
    id: Required[Literal["min_tls_version"]]
    """ID of the zone setting."""

    value: Required[Literal["1.0", "1.1", "1.2", "1.3"]]
    """Current value of the zone setting."""


class ItemZonesMinifyValue(TypedDict, total=False):
    css: Literal["on", "off"]
    """Automatically minify all CSS files for your website."""

    html: Literal["on", "off"]
    """Automatically minify all HTML files for your website."""

    js: Literal["on", "off"]
    """Automatically minify all JavaScript files for your website."""


class ItemZonesMinify(TypedDict, total=False):
    id: Required[Literal["minify"]]
    """Zone setting identifier."""

    value: Required[ItemZonesMinifyValue]
    """Current value of the zone setting."""


class ItemZonesMirage(TypedDict, total=False):
    id: Required[Literal["mirage"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesMobileRedirectValue(TypedDict, total=False):
    mobile_subdomain: Optional[str]
    """
    Which subdomain prefix you wish to redirect visitors on mobile devices to
    (subdomain must already exist).
    """

    status: Literal["on", "off"]
    """Whether or not mobile redirect is enabled."""

    strip_uri: bool
    """
    Whether to drop the current page path and redirect to the mobile subdomain URL
    root, or keep the path and redirect to the same page on the mobile subdomain.
    """


class ItemZonesMobileRedirect(TypedDict, total=False):
    id: Required[Literal["mobile_redirect"]]
    """Identifier of the zone setting."""

    value: Required[ItemZonesMobileRedirectValue]
    """Current value of the zone setting."""


class ItemZonesNELValue(TypedDict, total=False):
    enabled: bool


class ItemZonesNEL(TypedDict, total=False):
    id: Required[Literal["nel"]]
    """Zone setting identifier."""

    value: Required[ItemZonesNELValue]
    """Current value of the zone setting."""


class ItemZonesOpportunisticEncryption(TypedDict, total=False):
    id: Required[Literal["opportunistic_encryption"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesOpportunisticOnion(TypedDict, total=False):
    id: Required[Literal["opportunistic_onion"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesOrangeToOrange(TypedDict, total=False):
    id: Required[Literal["orange_to_orange"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesOriginErrorPagePassThru(TypedDict, total=False):
    id: Required[Literal["origin_error_page_pass_thru"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesPolish(TypedDict, total=False):
    id: Required[Literal["polish"]]
    """ID of the zone setting."""

    value: Required[Literal["off", "lossless", "lossy"]]
    """Current value of the zone setting."""


class ItemZonesPrefetchPreload(TypedDict, total=False):
    id: Required[Literal["prefetch_preload"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesProxyReadTimeout(TypedDict, total=False):
    id: Required[Literal["proxy_read_timeout"]]
    """ID of the zone setting."""

    value: Required[float]
    """Current value of the zone setting."""


class ItemZonesPseudoIPV4(TypedDict, total=False):
    id: Required[Literal["pseudo_ipv4"]]
    """Value of the Pseudo IPv4 setting."""

    value: Required[Literal["off", "add_header", "overwrite_header"]]
    """Current value of the zone setting."""


class ItemZonesResponseBuffering(TypedDict, total=False):
    id: Required[Literal["response_buffering"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesRocketLoader(TypedDict, total=False):
    id: Required[Literal["rocket_loader"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesSchemasAutomaticPlatformOptimizationValue(TypedDict, total=False):
    cache_by_device_type: Required[bool]
    """
    Indicates whether or not
    [cache by device type](https://developers.cloudflare.com/automatic-platform-optimization/reference/cache-device-type/)
    is enabled.
    """

    cf: Required[bool]
    """Indicates whether or not Cloudflare proxy is enabled."""

    enabled: Required[bool]
    """Indicates whether or not Automatic Platform Optimization is enabled."""

    hostnames: Required[List[str]]
    """
    An array of hostnames where Automatic Platform Optimization for WordPress is
    activated.
    """

    wordpress: Required[bool]
    """Indicates whether or not site is powered by WordPress."""

    wp_plugin: Required[bool]
    """
    Indicates whether or not
    [Cloudflare for WordPress plugin](https://wordpress.org/plugins/cloudflare/) is
    installed.
    """


class ItemZonesSchemasAutomaticPlatformOptimization(TypedDict, total=False):
    id: Required[Literal["automatic_platform_optimization"]]
    """ID of the zone setting."""

    value: Required[ItemZonesSchemasAutomaticPlatformOptimizationValue]
    """Current value of the zone setting."""


class ItemZonesSecurityHeaderValueStrictTransportSecurity(TypedDict, total=False):
    enabled: bool
    """Whether or not strict transport security is enabled."""

    include_subdomains: bool
    """Include all subdomains for strict transport security."""

    max_age: float
    """Max age in seconds of the strict transport security."""

    nosniff: bool
    """Whether or not to include 'X-Content-Type-Options: nosniff' header."""


class ItemZonesSecurityHeaderValue(TypedDict, total=False):
    strict_transport_security: ItemZonesSecurityHeaderValueStrictTransportSecurity
    """Strict Transport Security."""


class ItemZonesSecurityHeader(TypedDict, total=False):
    id: Required[Literal["security_header"]]
    """ID of the zone's security header."""

    value: Required[ItemZonesSecurityHeaderValue]
    """Current value of the zone setting."""


class ItemZonesSecurityLevel(TypedDict, total=False):
    id: Required[Literal["security_level"]]
    """ID of the zone setting."""

    value: Required[Literal["off", "essentially_off", "low", "medium", "high", "under_attack"]]
    """Current value of the zone setting."""


class ItemZonesServerSideExclude(TypedDict, total=False):
    id: Required[Literal["server_side_exclude"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesSha1Support(TypedDict, total=False):
    id: Required[Literal["sha1_support"]]
    """Zone setting identifier."""

    value: Required[Literal["off", "on"]]
    """Current value of the zone setting."""


class ItemZonesSortQueryStringForCache(TypedDict, total=False):
    id: Required[Literal["sort_query_string_for_cache"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesSSL(TypedDict, total=False):
    id: Required[Literal["ssl"]]
    """ID of the zone setting."""

    value: Required[Literal["off", "flexible", "full", "strict"]]
    """Current value of the zone setting."""


class ItemZonesSSLRecommender(TypedDict, total=False):
    id: Literal["ssl_recommender"]
    """Enrollment value for SSL/TLS Recommender."""

    enabled: bool
    """ssl-recommender enrollment setting."""


class ItemZonesTLS1_2Only(TypedDict, total=False):
    id: Required[Literal["tls_1_2_only"]]
    """Zone setting identifier."""

    value: Required[Literal["off", "on"]]
    """Current value of the zone setting."""


class ItemZonesTLS1_3(TypedDict, total=False):
    id: Required[Literal["tls_1_3"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off", "zrt"]]
    """Current value of the zone setting."""


class ItemZonesTLSClientAuth(TypedDict, total=False):
    id: Required[Literal["tls_client_auth"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesTrueClientIPHeader(TypedDict, total=False):
    id: Required[Literal["true_client_ip_header"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesWAF(TypedDict, total=False):
    id: Required[Literal["waf"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ItemZonesWebp(TypedDict, total=False):
    id: Required[Literal["webp"]]
    """ID of the zone setting."""

    value: Required[Literal["off", "on"]]
    """Current value of the zone setting."""


class ItemZonesWebsockets(TypedDict, total=False):
    id: Required[Literal["websockets"]]
    """ID of the zone setting."""

    value: Required[Literal["off", "on"]]
    """Current value of the zone setting."""


Item = Union[
    ItemZones0rtt,
    ItemZonesAdvancedDDOS,
    ItemZonesAlwaysOnline,
    ItemZonesAlwaysUseHTTPs,
    ItemZonesAutomaticHTTPsRewrites,
    ItemZonesBrotli,
    ItemZonesBrowserCacheTTL,
    ItemZonesBrowserCheck,
    ItemZonesCacheLevel,
    ItemZonesChallengeTTL,
    ItemZonesCiphers,
    ItemZonesCnameFlattening,
    ItemZonesDevelopmentMode,
    ItemZonesEarlyHints,
    ItemZonesEdgeCacheTTL,
    ItemZonesEmailObfuscation,
    ItemZonesH2Prioritization,
    ItemZonesHotlinkProtection,
    ItemZonesHTTP2,
    ItemZonesHTTP3,
    ItemZonesImageResizing,
    ItemZonesIPGeolocation,
    ItemZonesIPV6,
    ItemZonesMaxUpload,
    ItemZonesMinTLSVersion,
    ItemZonesMinify,
    ItemZonesMirage,
    ItemZonesMobileRedirect,
    ItemZonesNEL,
    ItemZonesOpportunisticEncryption,
    ItemZonesOpportunisticOnion,
    ItemZonesOrangeToOrange,
    ItemZonesOriginErrorPagePassThru,
    ItemZonesPolish,
    ItemZonesPrefetchPreload,
    ItemZonesProxyReadTimeout,
    ItemZonesPseudoIPV4,
    ItemZonesResponseBuffering,
    ItemZonesRocketLoader,
    ItemZonesSchemasAutomaticPlatformOptimization,
    ItemZonesSecurityHeader,
    ItemZonesSecurityLevel,
    ItemZonesServerSideExclude,
    ItemZonesSha1Support,
    ItemZonesSortQueryStringForCache,
    ItemZonesSSL,
    ItemZonesSSLRecommender,
    ItemZonesTLS1_2Only,
    ItemZonesTLS1_3,
    ItemZonesTLSClientAuth,
    ItemZonesTrueClientIPHeader,
    ItemZonesWAF,
    ItemZonesWebp,
    ItemZonesWebsockets,
]
