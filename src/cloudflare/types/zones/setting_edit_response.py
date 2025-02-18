# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .nel import NEL
from .ipv6 import IPV6
from .webp import WebP
from .http2 import HTTP2
from .http3 import HTTP3
from .brotli import Brotli
from .ciphers import Ciphers
from .tls_1_3 import TLS1_3
from .zero_rtt import ZeroRTT
from ..._models import BaseModel
from .websocket import Websocket
from .early_hints import EarlyHints
from .pseudo_ipv4 import PseudoIPV4
from .advanced_ddos import AdvancedDDoS
from .always_online import AlwaysOnline
from .challenge_ttl import ChallengeTTL
from .image_resizing import ImageResizing
from .min_tls_version import MinTLSVersion
from .ssl_recommender import SSLRecommender
from .tls_client_auth import TLSClientAuth
from .development_mode import DevelopmentMode
from .orange_to_orange import OrangeToOrange
from .prefetch_preload import PrefetchPreload
from .security_headers import SecurityHeaders
from .h2_prioritization import H2Prioritization
from .hotlink_protection import HotlinkProtection
from .proxy_read_timeout import ProxyReadTimeout
from .opportunistic_onion import OpportunisticOnion
from .server_side_excludes import ServerSideExcludes
from .automatic_platform_optimization import AutomaticPlatformOptimization

__all__ = [
    "SettingEditResponse",
    "ZonesCacheRulesAegis",
    "ZonesCacheRulesAegisValue",
    "ZonesSchemasAlwaysUseHTTPS",
    "ZonesSchemasAutomaticHTTPSRewrites",
    "ZonesSchemasBrowserCacheTTL",
    "ZonesSchemasBrowserCheck",
    "ZonesSchemasCacheLevel",
    "ZonesCNAMEFlattening",
    "ZonesSchemasEdgeCacheTTL",
    "ZonesSchemasEmailObfuscation",
    "ZonesSchemasIPGeolocation",
    "ZonesMaxUpload",
    "ZonesSchemasMirage",
    "ZonesSchemasOpportunisticEncryption",
    "ZonesSchemasOriginErrorPagePassThru",
    "ZonesCacheRulesOriginH2MaxStreams",
    "ZonesCacheRulesOriginMaxHTTPVersion",
    "ZonesSchemasPolish",
    "ZonesPrivacyPass",
    "ZonesReplaceInsecureJS",
    "ZonesSchemasResponseBuffering",
    "ZonesSchemasRocketLoader",
    "ZonesSchemasAutomaticPlatformOptimization",
    "ZonesSchemasSecurityLevel",
    "ZonesSha1Support",
    "ZonesSchemasSortQueryStringForCache",
    "ZonesSchemasSSL",
    "ZonesTLS1_2Only",
    "ZonesSchemasTrueClientIPHeader",
    "ZonesSchemasWAF",
]


class ZonesCacheRulesAegisValue(BaseModel):
    enabled: Optional[bool] = None
    """Whether the feature is enabled or not."""

    pool_id: Optional[str] = None
    """
    Egress pool id which refers to a grouping of dedicated egress IPs through which
    Cloudflare will connect to origin.
    """


class ZonesCacheRulesAegis(BaseModel):
    id: Literal["aegis"]
    """ID of the zone setting."""

    modified_on: Optional[datetime] = None
    """Last time this setting was modified."""

    value: Optional[ZonesCacheRulesAegisValue] = None
    """Value of the zone setting."""


class ZonesSchemasAlwaysUseHTTPS(BaseModel):
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


class ZonesSchemasAutomaticHTTPSRewrites(BaseModel):
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


class ZonesSchemasBrowserCacheTTL(BaseModel):
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


class ZonesSchemasBrowserCheck(BaseModel):
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


class ZonesSchemasCacheLevel(BaseModel):
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


class ZonesCNAMEFlattening(BaseModel):
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


class ZonesSchemasEdgeCacheTTL(BaseModel):
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


class ZonesSchemasEmailObfuscation(BaseModel):
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


class ZonesSchemasIPGeolocation(BaseModel):
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


class ZonesMaxUpload(BaseModel):
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


class ZonesSchemasMirage(BaseModel):
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


class ZonesSchemasOpportunisticEncryption(BaseModel):
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


class ZonesSchemasOriginErrorPagePassThru(BaseModel):
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


class ZonesCacheRulesOriginH2MaxStreams(BaseModel):
    id: Literal["origin_h2_max_streams"]
    """Value of the zone setting."""

    modified_on: Optional[datetime] = None
    """Last time this setting was modified."""

    value: Optional[int] = None
    """Value of the Origin H2 Max Streams Setting."""


class ZonesCacheRulesOriginMaxHTTPVersion(BaseModel):
    id: Literal["origin_max_http_version"]
    """Value of the zone setting."""

    modified_on: Optional[datetime] = None
    """Last time this setting was modified."""

    value: Optional[Literal["2", "1"]] = None
    """Value of the Origin Max HTTP Version Setting."""


class ZonesSchemasPolish(BaseModel):
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


class ZonesPrivacyPass(BaseModel):
    id: Literal["privacy_pass"]
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


class ZonesReplaceInsecureJS(BaseModel):
    id: Literal["replace_insecure_js"]
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


class ZonesSchemasResponseBuffering(BaseModel):
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


class ZonesSchemasRocketLoader(BaseModel):
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


class ZonesSchemasAutomaticPlatformOptimization(BaseModel):
    id: Literal["automatic_platform_optimization"]
    """ID of the zone setting."""

    value: AutomaticPlatformOptimization
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesSchemasSecurityLevel(BaseModel):
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


class ZonesSha1Support(BaseModel):
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


class ZonesSchemasSortQueryStringForCache(BaseModel):
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


class ZonesSchemasSSL(BaseModel):
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


class ZonesTLS1_2Only(BaseModel):
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


class ZonesSchemasTrueClientIPHeader(BaseModel):
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


class ZonesSchemasWAF(BaseModel):
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


SettingEditResponse: TypeAlias = Union[
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
