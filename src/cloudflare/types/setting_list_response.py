# File generated from our OpenAPI spec by Stainless.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "SettingListResponse",
    "SettingListResponseItem",
    "SettingListResponseItemZones0rtt",
    "SettingListResponseItemZonesAdvancedDDOS",
    "SettingListResponseItemZonesAlwaysOnline",
    "SettingListResponseItemZonesAlwaysUseHTTPS",
    "SettingListResponseItemZonesAutomaticHTTPSRewrites",
    "SettingListResponseItemZonesBrotli",
    "SettingListResponseItemZonesBrowserCacheTTL",
    "SettingListResponseItemZonesBrowserCheck",
    "SettingListResponseItemZonesCacheLevel",
    "SettingListResponseItemZonesChallengeTTL",
    "SettingListResponseItemZonesCiphers",
    "SettingListResponseItemZonesCnameFlattening",
    "SettingListResponseItemZonesDevelopmentMode",
    "SettingListResponseItemZonesEarlyHints",
    "SettingListResponseItemZonesEdgeCacheTTL",
    "SettingListResponseItemZonesEmailObfuscation",
    "SettingListResponseItemZonesH2Prioritization",
    "SettingListResponseItemZonesHotlinkProtection",
    "SettingListResponseItemZonesHTTP2",
    "SettingListResponseItemZonesHTTP3",
    "SettingListResponseItemZonesImageResizing",
    "SettingListResponseItemZonesIPGeolocation",
    "SettingListResponseItemZonesIPV6",
    "SettingListResponseItemZonesMaxUpload",
    "SettingListResponseItemZonesMinTLSVersion",
    "SettingListResponseItemZonesMinify",
    "SettingListResponseItemZonesMinifyValue",
    "SettingListResponseItemZonesMirage",
    "SettingListResponseItemZonesMobileRedirect",
    "SettingListResponseItemZonesMobileRedirectValue",
    "SettingListResponseItemZonesNEL",
    "SettingListResponseItemZonesNELValue",
    "SettingListResponseItemZonesOpportunisticEncryption",
    "SettingListResponseItemZonesOpportunisticOnion",
    "SettingListResponseItemZonesOrangeToOrange",
    "SettingListResponseItemZonesOriginErrorPagePassThru",
    "SettingListResponseItemZonesPolish",
    "SettingListResponseItemZonesPrefetchPreload",
    "SettingListResponseItemZonesProxyReadTimeout",
    "SettingListResponseItemZonesPseudoIPV4",
    "SettingListResponseItemZonesResponseBuffering",
    "SettingListResponseItemZonesRocketLoader",
    "SettingListResponseItemZonesSchemasAutomaticPlatformOptimization",
    "SettingListResponseItemZonesSchemasAutomaticPlatformOptimizationValue",
    "SettingListResponseItemZonesSecurityHeader",
    "SettingListResponseItemZonesSecurityHeaderValue",
    "SettingListResponseItemZonesSecurityHeaderValueStrictTransportSecurity",
    "SettingListResponseItemZonesSecurityLevel",
    "SettingListResponseItemZonesServerSideExclude",
    "SettingListResponseItemZonesSha1Support",
    "SettingListResponseItemZonesSortQueryStringForCache",
    "SettingListResponseItemZonesSSL",
    "SettingListResponseItemZonesSSLRecommender",
    "SettingListResponseItemZonesTLS1_2Only",
    "SettingListResponseItemZonesTLS1_3",
    "SettingListResponseItemZonesTLSClientAuth",
    "SettingListResponseItemZonesTrueClientIPHeader",
    "SettingListResponseItemZonesWAF",
    "SettingListResponseItemZonesWebp",
    "SettingListResponseItemZonesWebsockets",
]


class SettingListResponseItemZones0rtt(BaseModel):
    id: Literal["0rtt"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesAdvancedDDOS(BaseModel):
    id: Literal["advanced_ddos"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesAlwaysOnline(BaseModel):
    id: Literal["always_online"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesAlwaysUseHTTPS(BaseModel):
    id: Literal["always_use_https"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesAutomaticHTTPSRewrites(BaseModel):
    id: Literal["automatic_https_rewrites"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesBrotli(BaseModel):
    id: Literal["brotli"]
    """ID of the zone setting."""

    value: Literal["off", "on"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesBrowserCacheTTL(BaseModel):
    id: Literal["browser_cache_ttl"]
    """ID of the zone setting."""

    value: Literal[
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
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesBrowserCheck(BaseModel):
    id: Literal["browser_check"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesCacheLevel(BaseModel):
    id: Literal["cache_level"]
    """ID of the zone setting."""

    value: Literal["aggressive", "basic", "simplified"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesChallengeTTL(BaseModel):
    id: Literal["challenge_ttl"]
    """ID of the zone setting."""

    value: Literal[300, 900, 1800, 2700, 3600, 7200, 10800, 14400, 28800, 57600, 86400, 604800, 2592000, 31536000]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesCiphers(BaseModel):
    id: Literal["ciphers"]
    """ID of the zone setting."""

    value: List[str]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesCnameFlattening(BaseModel):
    id: Literal["cname_flattening"]
    """How to flatten the cname destination."""

    value: Literal["flatten_at_root", "flatten_all"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesDevelopmentMode(BaseModel):
    id: Literal["development_mode"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""

    time_remaining: Optional[float] = None
    """
    Value of the zone setting. Notes: The interval (in seconds) from when
    development mode expires (positive integer) or last expired (negative integer)
    for the domain. If development mode has never been enabled, this value is false.
    """


class SettingListResponseItemZonesEarlyHints(BaseModel):
    id: Literal["early_hints"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesEdgeCacheTTL(BaseModel):
    id: Literal["edge_cache_ttl"]
    """ID of the zone setting."""

    value: Literal[
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
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesEmailObfuscation(BaseModel):
    id: Literal["email_obfuscation"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesH2Prioritization(BaseModel):
    id: Literal["h2_prioritization"]
    """ID of the zone setting."""

    value: Literal["on", "off", "custom"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesHotlinkProtection(BaseModel):
    id: Literal["hotlink_protection"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesHTTP2(BaseModel):
    id: Literal["http2"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesHTTP3(BaseModel):
    id: Literal["http3"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesImageResizing(BaseModel):
    id: Literal["image_resizing"]
    """ID of the zone setting."""

    value: Literal["on", "off", "open"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesIPGeolocation(BaseModel):
    id: Literal["ip_geolocation"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesIPV6(BaseModel):
    id: Literal["ipv6"]
    """ID of the zone setting."""

    value: Literal["off", "on"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesMaxUpload(BaseModel):
    id: Literal["max_upload"]
    """identifier of the zone setting."""

    value: Literal[100, 200, 500]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesMinTLSVersion(BaseModel):
    id: Literal["min_tls_version"]
    """ID of the zone setting."""

    value: Literal["1.0", "1.1", "1.2", "1.3"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesMinifyValue(BaseModel):
    css: Optional[Literal["on", "off"]] = None
    """Automatically minify all CSS files for your website."""

    html: Optional[Literal["on", "off"]] = None
    """Automatically minify all HTML files for your website."""

    js: Optional[Literal["on", "off"]] = None
    """Automatically minify all JavaScript files for your website."""


class SettingListResponseItemZonesMinify(BaseModel):
    id: Literal["minify"]
    """Zone setting identifier."""

    value: SettingListResponseItemZonesMinifyValue
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesMirage(BaseModel):
    id: Literal["mirage"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesMobileRedirectValue(BaseModel):
    mobile_subdomain: Optional[str] = None
    """
    Which subdomain prefix you wish to redirect visitors on mobile devices to
    (subdomain must already exist).
    """

    status: Optional[Literal["on", "off"]] = None
    """Whether or not mobile redirect is enabled."""

    strip_uri: Optional[bool] = None
    """
    Whether to drop the current page path and redirect to the mobile subdomain URL
    root, or keep the path and redirect to the same page on the mobile subdomain.
    """


class SettingListResponseItemZonesMobileRedirect(BaseModel):
    id: Literal["mobile_redirect"]
    """Identifier of the zone setting."""

    value: SettingListResponseItemZonesMobileRedirectValue
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesNELValue(BaseModel):
    enabled: Optional[bool] = None


class SettingListResponseItemZonesNEL(BaseModel):
    id: Literal["nel"]
    """Zone setting identifier."""

    value: SettingListResponseItemZonesNELValue
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesOpportunisticEncryption(BaseModel):
    id: Literal["opportunistic_encryption"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesOpportunisticOnion(BaseModel):
    id: Literal["opportunistic_onion"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesOrangeToOrange(BaseModel):
    id: Literal["orange_to_orange"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesOriginErrorPagePassThru(BaseModel):
    id: Literal["origin_error_page_pass_thru"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesPolish(BaseModel):
    id: Literal["polish"]
    """ID of the zone setting."""

    value: Literal["off", "lossless", "lossy"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesPrefetchPreload(BaseModel):
    id: Literal["prefetch_preload"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesProxyReadTimeout(BaseModel):
    id: Literal["proxy_read_timeout"]
    """ID of the zone setting."""

    value: float
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesPseudoIPV4(BaseModel):
    id: Literal["pseudo_ipv4"]
    """Value of the Pseudo IPv4 setting."""

    value: Literal["off", "add_header", "overwrite_header"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesResponseBuffering(BaseModel):
    id: Literal["response_buffering"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesRocketLoader(BaseModel):
    id: Literal["rocket_loader"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesSchemasAutomaticPlatformOptimizationValue(BaseModel):
    cache_by_device_type: bool
    """
    Indicates whether or not
    [cache by device type](https://developers.cloudflare.com/automatic-platform-optimization/reference/cache-device-type/)
    is enabled.
    """

    cf: bool
    """Indicates whether or not Cloudflare proxy is enabled."""

    enabled: bool
    """Indicates whether or not Automatic Platform Optimization is enabled."""

    hostnames: List[str]
    """
    An array of hostnames where Automatic Platform Optimization for WordPress is
    activated.
    """

    wordpress: bool
    """Indicates whether or not site is powered by WordPress."""

    wp_plugin: bool
    """
    Indicates whether or not
    [Cloudflare for WordPress plugin](https://wordpress.org/plugins/cloudflare/) is
    installed.
    """


class SettingListResponseItemZonesSchemasAutomaticPlatformOptimization(BaseModel):
    id: Literal["automatic_platform_optimization"]
    """ID of the zone setting."""

    value: SettingListResponseItemZonesSchemasAutomaticPlatformOptimizationValue
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesSecurityHeaderValueStrictTransportSecurity(BaseModel):
    enabled: Optional[bool] = None
    """Whether or not strict transport security is enabled."""

    include_subdomains: Optional[bool] = None
    """Include all subdomains for strict transport security."""

    max_age: Optional[float] = None
    """Max age in seconds of the strict transport security."""

    nosniff: Optional[bool] = None
    """Whether or not to include 'X-Content-Type-Options: nosniff' header."""


class SettingListResponseItemZonesSecurityHeaderValue(BaseModel):
    strict_transport_security: Optional[SettingListResponseItemZonesSecurityHeaderValueStrictTransportSecurity] = None
    """Strict Transport Security."""


class SettingListResponseItemZonesSecurityHeader(BaseModel):
    id: Literal["security_header"]
    """ID of the zone's security header."""

    value: SettingListResponseItemZonesSecurityHeaderValue
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesSecurityLevel(BaseModel):
    id: Literal["security_level"]
    """ID of the zone setting."""

    value: Literal["off", "essentially_off", "low", "medium", "high", "under_attack"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesServerSideExclude(BaseModel):
    id: Literal["server_side_exclude"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesSha1Support(BaseModel):
    id: Literal["sha1_support"]
    """Zone setting identifier."""

    value: Literal["off", "on"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesSortQueryStringForCache(BaseModel):
    id: Literal["sort_query_string_for_cache"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesSSL(BaseModel):
    id: Literal["ssl"]
    """ID of the zone setting."""

    value: Literal["off", "flexible", "full", "strict"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesSSLRecommender(BaseModel):
    id: Optional[Literal["ssl_recommender"]] = None
    """Enrollment value for SSL/TLS Recommender."""

    enabled: Optional[bool] = None
    """ssl-recommender enrollment setting."""


class SettingListResponseItemZonesTLS1_2Only(BaseModel):
    id: Literal["tls_1_2_only"]
    """Zone setting identifier."""

    value: Literal["off", "on"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesTLS1_3(BaseModel):
    id: Literal["tls_1_3"]
    """ID of the zone setting."""

    value: Literal["on", "off", "zrt"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesTLSClientAuth(BaseModel):
    id: Literal["tls_client_auth"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesTrueClientIPHeader(BaseModel):
    id: Literal["true_client_ip_header"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesWAF(BaseModel):
    id: Literal["waf"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesWebp(BaseModel):
    id: Literal["webp"]
    """ID of the zone setting."""

    value: Literal["off", "on"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingListResponseItemZonesWebsockets(BaseModel):
    id: Literal["websockets"]
    """ID of the zone setting."""

    value: Literal["off", "on"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


SettingListResponseItem = Union[
    SettingListResponseItemZones0rtt,
    SettingListResponseItemZonesAdvancedDDOS,
    SettingListResponseItemZonesAlwaysOnline,
    SettingListResponseItemZonesAlwaysUseHTTPS,
    SettingListResponseItemZonesAutomaticHTTPSRewrites,
    SettingListResponseItemZonesBrotli,
    SettingListResponseItemZonesBrowserCacheTTL,
    SettingListResponseItemZonesBrowserCheck,
    SettingListResponseItemZonesCacheLevel,
    SettingListResponseItemZonesChallengeTTL,
    SettingListResponseItemZonesCiphers,
    SettingListResponseItemZonesCnameFlattening,
    SettingListResponseItemZonesDevelopmentMode,
    SettingListResponseItemZonesEarlyHints,
    SettingListResponseItemZonesEdgeCacheTTL,
    SettingListResponseItemZonesEmailObfuscation,
    SettingListResponseItemZonesH2Prioritization,
    SettingListResponseItemZonesHotlinkProtection,
    SettingListResponseItemZonesHTTP2,
    SettingListResponseItemZonesHTTP3,
    SettingListResponseItemZonesImageResizing,
    SettingListResponseItemZonesIPGeolocation,
    SettingListResponseItemZonesIPV6,
    SettingListResponseItemZonesMaxUpload,
    SettingListResponseItemZonesMinTLSVersion,
    SettingListResponseItemZonesMinify,
    SettingListResponseItemZonesMirage,
    SettingListResponseItemZonesMobileRedirect,
    SettingListResponseItemZonesNEL,
    SettingListResponseItemZonesOpportunisticEncryption,
    SettingListResponseItemZonesOpportunisticOnion,
    SettingListResponseItemZonesOrangeToOrange,
    SettingListResponseItemZonesOriginErrorPagePassThru,
    SettingListResponseItemZonesPolish,
    SettingListResponseItemZonesPrefetchPreload,
    SettingListResponseItemZonesProxyReadTimeout,
    SettingListResponseItemZonesPseudoIPV4,
    SettingListResponseItemZonesResponseBuffering,
    SettingListResponseItemZonesRocketLoader,
    SettingListResponseItemZonesSchemasAutomaticPlatformOptimization,
    SettingListResponseItemZonesSecurityHeader,
    SettingListResponseItemZonesSecurityLevel,
    SettingListResponseItemZonesServerSideExclude,
    SettingListResponseItemZonesSha1Support,
    SettingListResponseItemZonesSortQueryStringForCache,
    SettingListResponseItemZonesSSL,
    SettingListResponseItemZonesSSLRecommender,
    SettingListResponseItemZonesTLS1_2Only,
    SettingListResponseItemZonesTLS1_3,
    SettingListResponseItemZonesTLSClientAuth,
    SettingListResponseItemZonesTrueClientIPHeader,
    SettingListResponseItemZonesWAF,
    SettingListResponseItemZonesWebp,
    SettingListResponseItemZonesWebsockets,
]

SettingListResponse = List[SettingListResponseItem]
