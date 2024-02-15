# File generated from our OpenAPI spec by Stainless.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "SettingEditResponse",
    "SettingEditResponseItem",
    "SettingEditResponseItemZones0rtt",
    "SettingEditResponseItemZonesAdvancedDDOS",
    "SettingEditResponseItemZonesAlwaysOnline",
    "SettingEditResponseItemZonesAlwaysUseHTTPS",
    "SettingEditResponseItemZonesAutomaticHTTPSRewrites",
    "SettingEditResponseItemZonesBrotli",
    "SettingEditResponseItemZonesBrowserCacheTTL",
    "SettingEditResponseItemZonesBrowserCheck",
    "SettingEditResponseItemZonesCacheLevel",
    "SettingEditResponseItemZonesChallengeTTL",
    "SettingEditResponseItemZonesCiphers",
    "SettingEditResponseItemZonesCnameFlattening",
    "SettingEditResponseItemZonesDevelopmentMode",
    "SettingEditResponseItemZonesEarlyHints",
    "SettingEditResponseItemZonesEdgeCacheTTL",
    "SettingEditResponseItemZonesEmailObfuscation",
    "SettingEditResponseItemZonesH2Prioritization",
    "SettingEditResponseItemZonesHotlinkProtection",
    "SettingEditResponseItemZonesHTTP2",
    "SettingEditResponseItemZonesHTTP3",
    "SettingEditResponseItemZonesImageResizing",
    "SettingEditResponseItemZonesIPGeolocation",
    "SettingEditResponseItemZonesIPV6",
    "SettingEditResponseItemZonesMaxUpload",
    "SettingEditResponseItemZonesMinTLSVersion",
    "SettingEditResponseItemZonesMinify",
    "SettingEditResponseItemZonesMinifyValue",
    "SettingEditResponseItemZonesMirage",
    "SettingEditResponseItemZonesMobileRedirect",
    "SettingEditResponseItemZonesMobileRedirectValue",
    "SettingEditResponseItemZonesNEL",
    "SettingEditResponseItemZonesNELValue",
    "SettingEditResponseItemZonesOpportunisticEncryption",
    "SettingEditResponseItemZonesOpportunisticOnion",
    "SettingEditResponseItemZonesOrangeToOrange",
    "SettingEditResponseItemZonesOriginErrorPagePassThru",
    "SettingEditResponseItemZonesPolish",
    "SettingEditResponseItemZonesPrefetchPreload",
    "SettingEditResponseItemZonesProxyReadTimeout",
    "SettingEditResponseItemZonesPseudoIPV4",
    "SettingEditResponseItemZonesResponseBuffering",
    "SettingEditResponseItemZonesRocketLoader",
    "SettingEditResponseItemZonesSchemasAutomaticPlatformOptimization",
    "SettingEditResponseItemZonesSchemasAutomaticPlatformOptimizationValue",
    "SettingEditResponseItemZonesSecurityHeader",
    "SettingEditResponseItemZonesSecurityHeaderValue",
    "SettingEditResponseItemZonesSecurityHeaderValueStrictTransportSecurity",
    "SettingEditResponseItemZonesSecurityLevel",
    "SettingEditResponseItemZonesServerSideExclude",
    "SettingEditResponseItemZonesSha1Support",
    "SettingEditResponseItemZonesSortQueryStringForCache",
    "SettingEditResponseItemZonesSSL",
    "SettingEditResponseItemZonesSSLRecommender",
    "SettingEditResponseItemZonesTLS1_2Only",
    "SettingEditResponseItemZonesTLS1_3",
    "SettingEditResponseItemZonesTLSClientAuth",
    "SettingEditResponseItemZonesTrueClientIPHeader",
    "SettingEditResponseItemZonesWAF",
    "SettingEditResponseItemZonesWebp",
    "SettingEditResponseItemZonesWebsockets",
]


class SettingEditResponseItemZones0rtt(BaseModel):
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


class SettingEditResponseItemZonesAdvancedDDOS(BaseModel):
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


class SettingEditResponseItemZonesAlwaysOnline(BaseModel):
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


class SettingEditResponseItemZonesAlwaysUseHTTPS(BaseModel):
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


class SettingEditResponseItemZonesAutomaticHTTPSRewrites(BaseModel):
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


class SettingEditResponseItemZonesBrotli(BaseModel):
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


class SettingEditResponseItemZonesBrowserCacheTTL(BaseModel):
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


class SettingEditResponseItemZonesBrowserCheck(BaseModel):
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


class SettingEditResponseItemZonesCacheLevel(BaseModel):
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


class SettingEditResponseItemZonesChallengeTTL(BaseModel):
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


class SettingEditResponseItemZonesCiphers(BaseModel):
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


class SettingEditResponseItemZonesCnameFlattening(BaseModel):
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


class SettingEditResponseItemZonesDevelopmentMode(BaseModel):
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


class SettingEditResponseItemZonesEarlyHints(BaseModel):
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


class SettingEditResponseItemZonesEdgeCacheTTL(BaseModel):
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


class SettingEditResponseItemZonesEmailObfuscation(BaseModel):
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


class SettingEditResponseItemZonesH2Prioritization(BaseModel):
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


class SettingEditResponseItemZonesHotlinkProtection(BaseModel):
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


class SettingEditResponseItemZonesHTTP2(BaseModel):
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


class SettingEditResponseItemZonesHTTP3(BaseModel):
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


class SettingEditResponseItemZonesImageResizing(BaseModel):
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


class SettingEditResponseItemZonesIPGeolocation(BaseModel):
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


class SettingEditResponseItemZonesIPV6(BaseModel):
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


class SettingEditResponseItemZonesMaxUpload(BaseModel):
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


class SettingEditResponseItemZonesMinTLSVersion(BaseModel):
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


class SettingEditResponseItemZonesMinifyValue(BaseModel):
    css: Optional[Literal["on", "off"]] = None
    """Automatically minify all CSS files for your website."""

    html: Optional[Literal["on", "off"]] = None
    """Automatically minify all HTML files for your website."""

    js: Optional[Literal["on", "off"]] = None
    """Automatically minify all JavaScript files for your website."""


class SettingEditResponseItemZonesMinify(BaseModel):
    id: Literal["minify"]
    """Zone setting identifier."""

    value: SettingEditResponseItemZonesMinifyValue
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingEditResponseItemZonesMirage(BaseModel):
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


class SettingEditResponseItemZonesMobileRedirectValue(BaseModel):
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


class SettingEditResponseItemZonesMobileRedirect(BaseModel):
    id: Literal["mobile_redirect"]
    """Identifier of the zone setting."""

    value: SettingEditResponseItemZonesMobileRedirectValue
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingEditResponseItemZonesNELValue(BaseModel):
    enabled: Optional[bool] = None


class SettingEditResponseItemZonesNEL(BaseModel):
    id: Literal["nel"]
    """Zone setting identifier."""

    value: SettingEditResponseItemZonesNELValue
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingEditResponseItemZonesOpportunisticEncryption(BaseModel):
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


class SettingEditResponseItemZonesOpportunisticOnion(BaseModel):
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


class SettingEditResponseItemZonesOrangeToOrange(BaseModel):
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


class SettingEditResponseItemZonesOriginErrorPagePassThru(BaseModel):
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


class SettingEditResponseItemZonesPolish(BaseModel):
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


class SettingEditResponseItemZonesPrefetchPreload(BaseModel):
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


class SettingEditResponseItemZonesProxyReadTimeout(BaseModel):
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


class SettingEditResponseItemZonesPseudoIPV4(BaseModel):
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


class SettingEditResponseItemZonesResponseBuffering(BaseModel):
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


class SettingEditResponseItemZonesRocketLoader(BaseModel):
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


class SettingEditResponseItemZonesSchemasAutomaticPlatformOptimizationValue(BaseModel):
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


class SettingEditResponseItemZonesSchemasAutomaticPlatformOptimization(BaseModel):
    id: Literal["automatic_platform_optimization"]
    """ID of the zone setting."""

    value: SettingEditResponseItemZonesSchemasAutomaticPlatformOptimizationValue
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingEditResponseItemZonesSecurityHeaderValueStrictTransportSecurity(BaseModel):
    enabled: Optional[bool] = None
    """Whether or not strict transport security is enabled."""

    include_subdomains: Optional[bool] = None
    """Include all subdomains for strict transport security."""

    max_age: Optional[float] = None
    """Max age in seconds of the strict transport security."""

    nosniff: Optional[bool] = None
    """Whether or not to include 'X-Content-Type-Options: nosniff' header."""


class SettingEditResponseItemZonesSecurityHeaderValue(BaseModel):
    strict_transport_security: Optional[SettingEditResponseItemZonesSecurityHeaderValueStrictTransportSecurity] = None
    """Strict Transport Security."""


class SettingEditResponseItemZonesSecurityHeader(BaseModel):
    id: Literal["security_header"]
    """ID of the zone's security header."""

    value: SettingEditResponseItemZonesSecurityHeaderValue
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingEditResponseItemZonesSecurityLevel(BaseModel):
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


class SettingEditResponseItemZonesServerSideExclude(BaseModel):
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


class SettingEditResponseItemZonesSha1Support(BaseModel):
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


class SettingEditResponseItemZonesSortQueryStringForCache(BaseModel):
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


class SettingEditResponseItemZonesSSL(BaseModel):
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


class SettingEditResponseItemZonesSSLRecommender(BaseModel):
    id: Optional[Literal["ssl_recommender"]] = None
    """Enrollment value for SSL/TLS Recommender."""

    enabled: Optional[bool] = None
    """ssl-recommender enrollment setting."""


class SettingEditResponseItemZonesTLS1_2Only(BaseModel):
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


class SettingEditResponseItemZonesTLS1_3(BaseModel):
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


class SettingEditResponseItemZonesTLSClientAuth(BaseModel):
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


class SettingEditResponseItemZonesTrueClientIPHeader(BaseModel):
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


class SettingEditResponseItemZonesWAF(BaseModel):
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


class SettingEditResponseItemZonesWebp(BaseModel):
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


class SettingEditResponseItemZonesWebsockets(BaseModel):
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


SettingEditResponseItem = Union[
    SettingEditResponseItemZones0rtt,
    SettingEditResponseItemZonesAdvancedDDOS,
    SettingEditResponseItemZonesAlwaysOnline,
    SettingEditResponseItemZonesAlwaysUseHTTPS,
    SettingEditResponseItemZonesAutomaticHTTPSRewrites,
    SettingEditResponseItemZonesBrotli,
    SettingEditResponseItemZonesBrowserCacheTTL,
    SettingEditResponseItemZonesBrowserCheck,
    SettingEditResponseItemZonesCacheLevel,
    SettingEditResponseItemZonesChallengeTTL,
    SettingEditResponseItemZonesCiphers,
    SettingEditResponseItemZonesCnameFlattening,
    SettingEditResponseItemZonesDevelopmentMode,
    SettingEditResponseItemZonesEarlyHints,
    SettingEditResponseItemZonesEdgeCacheTTL,
    SettingEditResponseItemZonesEmailObfuscation,
    SettingEditResponseItemZonesH2Prioritization,
    SettingEditResponseItemZonesHotlinkProtection,
    SettingEditResponseItemZonesHTTP2,
    SettingEditResponseItemZonesHTTP3,
    SettingEditResponseItemZonesImageResizing,
    SettingEditResponseItemZonesIPGeolocation,
    SettingEditResponseItemZonesIPV6,
    SettingEditResponseItemZonesMaxUpload,
    SettingEditResponseItemZonesMinTLSVersion,
    SettingEditResponseItemZonesMinify,
    SettingEditResponseItemZonesMirage,
    SettingEditResponseItemZonesMobileRedirect,
    SettingEditResponseItemZonesNEL,
    SettingEditResponseItemZonesOpportunisticEncryption,
    SettingEditResponseItemZonesOpportunisticOnion,
    SettingEditResponseItemZonesOrangeToOrange,
    SettingEditResponseItemZonesOriginErrorPagePassThru,
    SettingEditResponseItemZonesPolish,
    SettingEditResponseItemZonesPrefetchPreload,
    SettingEditResponseItemZonesProxyReadTimeout,
    SettingEditResponseItemZonesPseudoIPV4,
    SettingEditResponseItemZonesResponseBuffering,
    SettingEditResponseItemZonesRocketLoader,
    SettingEditResponseItemZonesSchemasAutomaticPlatformOptimization,
    SettingEditResponseItemZonesSecurityHeader,
    SettingEditResponseItemZonesSecurityLevel,
    SettingEditResponseItemZonesServerSideExclude,
    SettingEditResponseItemZonesSha1Support,
    SettingEditResponseItemZonesSortQueryStringForCache,
    SettingEditResponseItemZonesSSL,
    SettingEditResponseItemZonesSSLRecommender,
    SettingEditResponseItemZonesTLS1_2Only,
    SettingEditResponseItemZonesTLS1_3,
    SettingEditResponseItemZonesTLSClientAuth,
    SettingEditResponseItemZonesTrueClientIPHeader,
    SettingEditResponseItemZonesWAF,
    SettingEditResponseItemZonesWebp,
    SettingEditResponseItemZonesWebsockets,
]

SettingEditResponse = List[SettingEditResponseItem]
