# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .automatic_platform_optimization_param import AutomaticPlatformOptimizationParam

__all__ = [
    "SettingEditParams",
    "ZeroRTT",
    "AdvancedDDoS",
    "ZonesCacheRulesAegis",
    "ZonesCacheRulesAegisValue",
    "AlwaysOnline",
    "ZonesSchemasAlwaysUseHTTPS",
    "ZonesSchemasAutomaticHTTPSRewrites",
    "Brotli",
    "ZonesSchemasBrowserCacheTTL",
    "ZonesSchemasBrowserCheck",
    "ZonesSchemasCacheLevel",
    "ChallengeTTL",
    "Ciphers",
    "ZonesCNAMEFlattening",
    "DevelopmentMode",
    "EarlyHints",
    "ZonesSchemasEdgeCacheTTL",
    "ZonesSchemasEmailObfuscation",
    "H2Prioritization",
    "HotlinkProtection",
    "HTTP2",
    "HTTP3",
    "ImageResizing",
    "ZonesSchemasIPGeolocation",
    "IPV6",
    "ZonesMaxUpload",
    "MinTLSVersion",
    "ZonesSchemasMirage",
    "NEL",
    "NELValue",
    "ZonesSchemasOpportunisticEncryption",
    "OpportunisticOnion",
    "OrangeToOrange",
    "ZonesSchemasOriginErrorPagePassThru",
    "ZonesCacheRulesOriginH2MaxStreams",
    "ZonesCacheRulesOriginMaxHTTPVersion",
    "ZonesSchemasPolish",
    "PrefetchPreload",
    "ZonesPrivacyPass",
    "ProxyReadTimeout",
    "PseudoIPV4",
    "ZonesReplaceInsecureJS",
    "ZonesSchemasResponseBuffering",
    "ZonesSchemasRocketLoader",
    "ZonesSchemasAutomaticPlatformOptimization",
    "SecurityHeaders",
    "SecurityHeadersValue",
    "SecurityHeadersValueStrictTransportSecurity",
    "ZonesSchemasSecurityLevel",
    "ServerSideExcludes",
    "ZonesSha1Support",
    "ZonesSchemasSortQueryStringForCache",
    "ZonesSchemasSSL",
    "SSLRecommender",
    "ZonesTLS1_2Only",
    "TLS1_3",
    "TLSClientAuth",
    "ZonesSchemasTrueClientIPHeader",
    "ZonesSchemasWAF",
    "WebP",
    "Websocket",
]


class ZeroRTT(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["0rtt"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class AdvancedDDoS(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["advanced_ddos"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ZonesCacheRulesAegis(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["aegis"]]
    """ID of the zone setting."""

    value: ZonesCacheRulesAegisValue
    """Value of the zone setting."""


class ZonesCacheRulesAegisValue(TypedDict, total=False):
    enabled: bool
    """Whether the feature is enabled or not."""

    pool_id: str
    """
    Egress pool id which refers to a grouping of dedicated egress IPs through which
    Cloudflare will connect to origin.
    """


class AlwaysOnline(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["always_online"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ZonesSchemasAlwaysUseHTTPS(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["always_use_https"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ZonesSchemasAutomaticHTTPSRewrites(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["automatic_https_rewrites"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class Brotli(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["brotli"]]
    """ID of the zone setting."""

    value: Required[Literal["off", "on"]]
    """Current value of the zone setting."""


class ZonesSchemasBrowserCacheTTL(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

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


class ZonesSchemasBrowserCheck(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["browser_check"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ZonesSchemasCacheLevel(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["cache_level"]]
    """ID of the zone setting."""

    value: Required[Literal["aggressive", "basic", "simplified"]]
    """Current value of the zone setting."""


class ChallengeTTL(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["challenge_ttl"]]
    """ID of the zone setting."""

    value: Required[
        Literal[300, 900, 1800, 2700, 3600, 7200, 10800, 14400, 28800, 57600, 86400, 604800, 2592000, 31536000]
    ]
    """Current value of the zone setting."""


class Ciphers(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["ciphers"]]
    """ID of the zone setting."""

    value: Required[List[str]]
    """Current value of the zone setting."""


class ZonesCNAMEFlattening(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["cname_flattening"]]
    """How to flatten the cname destination."""

    value: Required[Literal["flatten_at_root", "flatten_all"]]
    """Current value of the zone setting."""


class DevelopmentMode(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["development_mode"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class EarlyHints(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["early_hints"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ZonesSchemasEdgeCacheTTL(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

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


class ZonesSchemasEmailObfuscation(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["email_obfuscation"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class H2Prioritization(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["h2_prioritization"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off", "custom"]]
    """Current value of the zone setting."""


class HotlinkProtection(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["hotlink_protection"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class HTTP2(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["http2"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class HTTP3(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["http3"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ImageResizing(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["image_resizing"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off", "open"]]
    """Current value of the zone setting."""


class ZonesSchemasIPGeolocation(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["ip_geolocation"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class IPV6(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["ipv6"]]
    """ID of the zone setting."""

    value: Required[Literal["off", "on"]]
    """Current value of the zone setting."""


class ZonesMaxUpload(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["max_upload"]]
    """identifier of the zone setting."""

    value: Required[Literal[100, 200, 500]]
    """Current value of the zone setting."""


class MinTLSVersion(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["min_tls_version"]]
    """ID of the zone setting."""

    value: Required[Literal["1.0", "1.1", "1.2", "1.3"]]
    """Current value of the zone setting."""


class ZonesSchemasMirage(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["mirage"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class NEL(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["nel"]]
    """Zone setting identifier."""

    value: Required[NELValue]
    """Current value of the zone setting."""


class NELValue(TypedDict, total=False):
    enabled: bool


class ZonesSchemasOpportunisticEncryption(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["opportunistic_encryption"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class OpportunisticOnion(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["opportunistic_onion"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class OrangeToOrange(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["orange_to_orange"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ZonesSchemasOriginErrorPagePassThru(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["origin_error_page_pass_thru"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ZonesCacheRulesOriginH2MaxStreams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["origin_h2_max_streams"]]
    """Value of the zone setting."""

    value: int
    """Value of the Origin H2 Max Streams Setting."""


class ZonesCacheRulesOriginMaxHTTPVersion(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["origin_max_http_version"]]
    """Value of the zone setting."""

    value: Literal["2", "1"]
    """Value of the Origin Max HTTP Version Setting."""


class ZonesSchemasPolish(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["polish"]]
    """ID of the zone setting."""

    value: Required[Literal["off", "lossless", "lossy"]]
    """Current value of the zone setting."""


class PrefetchPreload(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["prefetch_preload"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ZonesPrivacyPass(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["privacy_pass"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ProxyReadTimeout(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["proxy_read_timeout"]]
    """ID of the zone setting."""

    value: Required[float]
    """Current value of the zone setting."""


class PseudoIPV4(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["pseudo_ipv4"]]
    """Value of the Pseudo IPv4 setting."""

    value: Required[Literal["off", "add_header", "overwrite_header"]]
    """Current value of the zone setting."""


class ZonesReplaceInsecureJS(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["replace_insecure_js"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ZonesSchemasResponseBuffering(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["response_buffering"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ZonesSchemasRocketLoader(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["rocket_loader"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ZonesSchemasAutomaticPlatformOptimization(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["automatic_platform_optimization"]]
    """ID of the zone setting."""

    value: Required[AutomaticPlatformOptimizationParam]
    """Current value of the zone setting."""


class SecurityHeaders(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["security_header"]]
    """ID of the zone's security header."""

    value: Required[SecurityHeadersValue]
    """Current value of the zone setting."""


class SecurityHeadersValueStrictTransportSecurity(TypedDict, total=False):
    enabled: bool
    """Whether or not strict transport security is enabled."""

    include_subdomains: bool
    """Include all subdomains for strict transport security."""

    max_age: float
    """Max age in seconds of the strict transport security."""

    nosniff: bool
    """Whether or not to include 'X-Content-Type-Options: nosniff' header."""

    preload: bool
    """Enable automatic preload of the HSTS configuration."""


class SecurityHeadersValue(TypedDict, total=False):
    strict_transport_security: SecurityHeadersValueStrictTransportSecurity
    """Strict Transport Security."""


class ZonesSchemasSecurityLevel(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["security_level"]]
    """ID of the zone setting."""

    value: Required[Literal["off", "essentially_off", "low", "medium", "high", "under_attack"]]
    """Current value of the zone setting."""


class ServerSideExcludes(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["server_side_exclude"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ZonesSha1Support(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["sha1_support"]]
    """Zone setting identifier."""

    value: Required[Literal["off", "on"]]
    """Current value of the zone setting."""


class ZonesSchemasSortQueryStringForCache(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["sort_query_string_for_cache"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ZonesSchemasSSL(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["ssl"]]
    """ID of the zone setting."""

    value: Required[Literal["off", "flexible", "full", "strict"]]
    """Current value of the zone setting."""


class SSLRecommender(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Literal["ssl_recommender"]
    """Enrollment value for SSL/TLS Recommender."""

    enabled: bool
    """ssl-recommender enrollment setting."""


class ZonesTLS1_2Only(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["tls_1_2_only"]]
    """Zone setting identifier."""

    value: Required[Literal["off", "on"]]
    """Current value of the zone setting."""


class TLS1_3(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["tls_1_3"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off", "zrt"]]
    """Current value of the zone setting."""


class TLSClientAuth(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["tls_client_auth"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ZonesSchemasTrueClientIPHeader(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["true_client_ip_header"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class ZonesSchemasWAF(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["waf"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""


class WebP(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["webp"]]
    """ID of the zone setting."""

    value: Required[Literal["off", "on"]]
    """Current value of the zone setting."""


class Websocket(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: Required[Literal["websockets"]]
    """ID of the zone setting."""

    value: Required[Literal["off", "on"]]
    """Current value of the zone setting."""


SettingEditParams: TypeAlias = Union[
    ZeroRTT,
    AdvancedDDoS,
    ZonesCacheRulesAegis,
    AlwaysOnline,
    ZonesSchemasAlwaysUseHTTPS,
    ZonesSchemasAutomaticHTTPSRewrites,
    Brotli,
    ZonesSchemasBrowserCacheTTL,
    ZonesSchemasBrowserCheck,
    ZonesSchemasCacheLevel,
    ChallengeTTL,
    Ciphers,
    ZonesCNAMEFlattening,
    DevelopmentMode,
    EarlyHints,
    ZonesSchemasEdgeCacheTTL,
    ZonesSchemasEmailObfuscation,
    H2Prioritization,
    HotlinkProtection,
    HTTP2,
    HTTP3,
    ImageResizing,
    ZonesSchemasIPGeolocation,
    IPV6,
    ZonesMaxUpload,
    MinTLSVersion,
    ZonesSchemasMirage,
    NEL,
    ZonesSchemasOpportunisticEncryption,
    OpportunisticOnion,
    OrangeToOrange,
    ZonesSchemasOriginErrorPagePassThru,
    ZonesCacheRulesOriginH2MaxStreams,
    ZonesCacheRulesOriginMaxHTTPVersion,
    ZonesSchemasPolish,
    PrefetchPreload,
    ZonesPrivacyPass,
    ProxyReadTimeout,
    PseudoIPV4,
    ZonesReplaceInsecureJS,
    ZonesSchemasResponseBuffering,
    ZonesSchemasRocketLoader,
    ZonesSchemasAutomaticPlatformOptimization,
    SecurityHeaders,
    ZonesSchemasSecurityLevel,
    ServerSideExcludes,
    ZonesSha1Support,
    ZonesSchemasSortQueryStringForCache,
    ZonesSchemasSSL,
    SSLRecommender,
    ZonesTLS1_2Only,
    TLS1_3,
    TLSClientAuth,
    ZonesSchemasTrueClientIPHeader,
    ZonesSchemasWAF,
    WebP,
    Websocket,
]
