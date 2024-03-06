# File generated from our OpenAPI spec by Stainless.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "SettingGetResponse",
    "SettingGetResponseItem",
    "SettingGetResponseItemZones0rtt",
    "SettingGetResponseItemZonesAdvancedDDOS",
    "SettingGetResponseItemZonesAlwaysOnline",
    "SettingGetResponseItemZonesAlwaysUseHTTPS",
    "SettingGetResponseItemZonesAutomaticHTTPSRewrites",
    "SettingGetResponseItemZonesBrotli",
    "SettingGetResponseItemZonesBrowserCacheTTL",
    "SettingGetResponseItemZonesBrowserCheck",
    "SettingGetResponseItemZonesCacheLevel",
    "SettingGetResponseItemZonesChallengeTTL",
    "SettingGetResponseItemZonesCiphers",
    "SettingGetResponseItemZonesCNAMEFlattening",
    "SettingGetResponseItemZonesDevelopmentMode",
    "SettingGetResponseItemZonesEarlyHints",
    "SettingGetResponseItemZonesEdgeCacheTTL",
    "SettingGetResponseItemZonesEmailObfuscation",
    "SettingGetResponseItemZonesH2Prioritization",
    "SettingGetResponseItemZonesHotlinkProtection",
    "SettingGetResponseItemZonesHTTP2",
    "SettingGetResponseItemZonesHTTP3",
    "SettingGetResponseItemZonesImageResizing",
    "SettingGetResponseItemZonesIPGeolocation",
    "SettingGetResponseItemZonesIPV6",
    "SettingGetResponseItemZonesMaxUpload",
    "SettingGetResponseItemZonesMinTLSVersion",
    "SettingGetResponseItemZonesMinify",
    "SettingGetResponseItemZonesMinifyValue",
    "SettingGetResponseItemZonesMirage",
    "SettingGetResponseItemZonesMobileRedirect",
    "SettingGetResponseItemZonesMobileRedirectValue",
    "SettingGetResponseItemZonesNEL",
    "SettingGetResponseItemZonesNELValue",
    "SettingGetResponseItemZonesOpportunisticEncryption",
    "SettingGetResponseItemZonesOpportunisticOnion",
    "SettingGetResponseItemZonesOrangeToOrange",
    "SettingGetResponseItemZonesOriginErrorPagePassThru",
    "SettingGetResponseItemZonesPolish",
    "SettingGetResponseItemZonesPrefetchPreload",
    "SettingGetResponseItemZonesProxyReadTimeout",
    "SettingGetResponseItemZonesPseudoIPV4",
    "SettingGetResponseItemZonesResponseBuffering",
    "SettingGetResponseItemZonesRocketLoader",
    "SettingGetResponseItemZonesSchemasAutomaticPlatformOptimization",
    "SettingGetResponseItemZonesSchemasAutomaticPlatformOptimizationValue",
    "SettingGetResponseItemZonesSecurityHeader",
    "SettingGetResponseItemZonesSecurityHeaderValue",
    "SettingGetResponseItemZonesSecurityHeaderValueStrictTransportSecurity",
    "SettingGetResponseItemZonesSecurityLevel",
    "SettingGetResponseItemZonesServerSideExclude",
    "SettingGetResponseItemZonesSha1Support",
    "SettingGetResponseItemZonesSortQueryStringForCache",
    "SettingGetResponseItemZonesSSL",
    "SettingGetResponseItemZonesSSLRecommender",
    "SettingGetResponseItemZonesTLS1_2Only",
    "SettingGetResponseItemZonesTLS1_3",
    "SettingGetResponseItemZonesTLSClientAuth",
    "SettingGetResponseItemZonesTrueClientIPHeader",
    "SettingGetResponseItemZonesWAF",
    "SettingGetResponseItemZonesWebp",
    "SettingGetResponseItemZonesWebsockets",
]


class SettingGetResponseItemZones0rtt(BaseModel):
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


class SettingGetResponseItemZonesAdvancedDDOS(BaseModel):
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


class SettingGetResponseItemZonesAlwaysOnline(BaseModel):
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


class SettingGetResponseItemZonesAlwaysUseHTTPS(BaseModel):
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


class SettingGetResponseItemZonesAutomaticHTTPSRewrites(BaseModel):
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


class SettingGetResponseItemZonesBrotli(BaseModel):
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


class SettingGetResponseItemZonesBrowserCacheTTL(BaseModel):
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


class SettingGetResponseItemZonesBrowserCheck(BaseModel):
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


class SettingGetResponseItemZonesCacheLevel(BaseModel):
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


class SettingGetResponseItemZonesChallengeTTL(BaseModel):
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


class SettingGetResponseItemZonesCiphers(BaseModel):
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


class SettingGetResponseItemZonesCNAMEFlattening(BaseModel):
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


class SettingGetResponseItemZonesDevelopmentMode(BaseModel):
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


class SettingGetResponseItemZonesEarlyHints(BaseModel):
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


class SettingGetResponseItemZonesEdgeCacheTTL(BaseModel):
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


class SettingGetResponseItemZonesEmailObfuscation(BaseModel):
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


class SettingGetResponseItemZonesH2Prioritization(BaseModel):
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


class SettingGetResponseItemZonesHotlinkProtection(BaseModel):
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


class SettingGetResponseItemZonesHTTP2(BaseModel):
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


class SettingGetResponseItemZonesHTTP3(BaseModel):
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


class SettingGetResponseItemZonesImageResizing(BaseModel):
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


class SettingGetResponseItemZonesIPGeolocation(BaseModel):
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


class SettingGetResponseItemZonesIPV6(BaseModel):
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


class SettingGetResponseItemZonesMaxUpload(BaseModel):
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


class SettingGetResponseItemZonesMinTLSVersion(BaseModel):
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


class SettingGetResponseItemZonesMinifyValue(BaseModel):
    css: Optional[Literal["on", "off"]] = None
    """Automatically minify all CSS files for your website."""

    html: Optional[Literal["on", "off"]] = None
    """Automatically minify all HTML files for your website."""

    js: Optional[Literal["on", "off"]] = None
    """Automatically minify all JavaScript files for your website."""


class SettingGetResponseItemZonesMinify(BaseModel):
    id: Literal["minify"]
    """Zone setting identifier."""

    value: SettingGetResponseItemZonesMinifyValue
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingGetResponseItemZonesMirage(BaseModel):
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


class SettingGetResponseItemZonesMobileRedirectValue(BaseModel):
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


class SettingGetResponseItemZonesMobileRedirect(BaseModel):
    id: Literal["mobile_redirect"]
    """Identifier of the zone setting."""

    value: SettingGetResponseItemZonesMobileRedirectValue
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingGetResponseItemZonesNELValue(BaseModel):
    enabled: Optional[bool] = None


class SettingGetResponseItemZonesNEL(BaseModel):
    id: Literal["nel"]
    """Zone setting identifier."""

    value: SettingGetResponseItemZonesNELValue
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingGetResponseItemZonesOpportunisticEncryption(BaseModel):
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


class SettingGetResponseItemZonesOpportunisticOnion(BaseModel):
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


class SettingGetResponseItemZonesOrangeToOrange(BaseModel):
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


class SettingGetResponseItemZonesOriginErrorPagePassThru(BaseModel):
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


class SettingGetResponseItemZonesPolish(BaseModel):
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


class SettingGetResponseItemZonesPrefetchPreload(BaseModel):
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


class SettingGetResponseItemZonesProxyReadTimeout(BaseModel):
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


class SettingGetResponseItemZonesPseudoIPV4(BaseModel):
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


class SettingGetResponseItemZonesResponseBuffering(BaseModel):
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


class SettingGetResponseItemZonesRocketLoader(BaseModel):
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


class SettingGetResponseItemZonesSchemasAutomaticPlatformOptimizationValue(BaseModel):
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


class SettingGetResponseItemZonesSchemasAutomaticPlatformOptimization(BaseModel):
    id: Literal["automatic_platform_optimization"]
    """ID of the zone setting."""

    value: SettingGetResponseItemZonesSchemasAutomaticPlatformOptimizationValue
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingGetResponseItemZonesSecurityHeaderValueStrictTransportSecurity(BaseModel):
    enabled: Optional[bool] = None
    """Whether or not strict transport security is enabled."""

    include_subdomains: Optional[bool] = None
    """Include all subdomains for strict transport security."""

    max_age: Optional[float] = None
    """Max age in seconds of the strict transport security."""

    nosniff: Optional[bool] = None
    """Whether or not to include 'X-Content-Type-Options: nosniff' header."""


class SettingGetResponseItemZonesSecurityHeaderValue(BaseModel):
    strict_transport_security: Optional[SettingGetResponseItemZonesSecurityHeaderValueStrictTransportSecurity] = None
    """Strict Transport Security."""


class SettingGetResponseItemZonesSecurityHeader(BaseModel):
    id: Literal["security_header"]
    """ID of the zone's security header."""

    value: SettingGetResponseItemZonesSecurityHeaderValue
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class SettingGetResponseItemZonesSecurityLevel(BaseModel):
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


class SettingGetResponseItemZonesServerSideExclude(BaseModel):
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


class SettingGetResponseItemZonesSha1Support(BaseModel):
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


class SettingGetResponseItemZonesSortQueryStringForCache(BaseModel):
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


class SettingGetResponseItemZonesSSL(BaseModel):
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


class SettingGetResponseItemZonesSSLRecommender(BaseModel):
    id: Optional[Literal["ssl_recommender"]] = None
    """Enrollment value for SSL/TLS Recommender."""

    enabled: Optional[bool] = None
    """ssl-recommender enrollment setting."""


class SettingGetResponseItemZonesTLS1_2Only(BaseModel):
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


class SettingGetResponseItemZonesTLS1_3(BaseModel):
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


class SettingGetResponseItemZonesTLSClientAuth(BaseModel):
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


class SettingGetResponseItemZonesTrueClientIPHeader(BaseModel):
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


class SettingGetResponseItemZonesWAF(BaseModel):
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


class SettingGetResponseItemZonesWebp(BaseModel):
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


class SettingGetResponseItemZonesWebsockets(BaseModel):
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


SettingGetResponseItem = Union[
    SettingGetResponseItemZones0rtt,
    SettingGetResponseItemZonesAdvancedDDOS,
    SettingGetResponseItemZonesAlwaysOnline,
    SettingGetResponseItemZonesAlwaysUseHTTPS,
    SettingGetResponseItemZonesAutomaticHTTPSRewrites,
    SettingGetResponseItemZonesBrotli,
    SettingGetResponseItemZonesBrowserCacheTTL,
    SettingGetResponseItemZonesBrowserCheck,
    SettingGetResponseItemZonesCacheLevel,
    SettingGetResponseItemZonesChallengeTTL,
    SettingGetResponseItemZonesCiphers,
    SettingGetResponseItemZonesCNAMEFlattening,
    SettingGetResponseItemZonesDevelopmentMode,
    SettingGetResponseItemZonesEarlyHints,
    SettingGetResponseItemZonesEdgeCacheTTL,
    SettingGetResponseItemZonesEmailObfuscation,
    SettingGetResponseItemZonesH2Prioritization,
    SettingGetResponseItemZonesHotlinkProtection,
    SettingGetResponseItemZonesHTTP2,
    SettingGetResponseItemZonesHTTP3,
    SettingGetResponseItemZonesImageResizing,
    SettingGetResponseItemZonesIPGeolocation,
    SettingGetResponseItemZonesIPV6,
    SettingGetResponseItemZonesMaxUpload,
    SettingGetResponseItemZonesMinTLSVersion,
    SettingGetResponseItemZonesMinify,
    SettingGetResponseItemZonesMirage,
    SettingGetResponseItemZonesMobileRedirect,
    SettingGetResponseItemZonesNEL,
    SettingGetResponseItemZonesOpportunisticEncryption,
    SettingGetResponseItemZonesOpportunisticOnion,
    SettingGetResponseItemZonesOrangeToOrange,
    SettingGetResponseItemZonesOriginErrorPagePassThru,
    SettingGetResponseItemZonesPolish,
    SettingGetResponseItemZonesPrefetchPreload,
    SettingGetResponseItemZonesProxyReadTimeout,
    SettingGetResponseItemZonesPseudoIPV4,
    SettingGetResponseItemZonesResponseBuffering,
    SettingGetResponseItemZonesRocketLoader,
    SettingGetResponseItemZonesSchemasAutomaticPlatformOptimization,
    SettingGetResponseItemZonesSecurityHeader,
    SettingGetResponseItemZonesSecurityLevel,
    SettingGetResponseItemZonesServerSideExclude,
    SettingGetResponseItemZonesSha1Support,
    SettingGetResponseItemZonesSortQueryStringForCache,
    SettingGetResponseItemZonesSSL,
    SettingGetResponseItemZonesSSLRecommender,
    SettingGetResponseItemZonesTLS1_2Only,
    SettingGetResponseItemZonesTLS1_3,
    SettingGetResponseItemZonesTLSClientAuth,
    SettingGetResponseItemZonesTrueClientIPHeader,
    SettingGetResponseItemZonesWAF,
    SettingGetResponseItemZonesWebp,
    SettingGetResponseItemZonesWebsockets,
]

SettingGetResponse = List[SettingGetResponseItem]
