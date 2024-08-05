# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .nel import NEL
from .ssl import SSL
from .waf import WAF
from .ipv6 import IPV6
from .webp import WebP
from .http2 import HTTP2
from .http3 import HTTP3
from .brotli import Brotli
from .minify import Minify
from .mirage import Mirage
from .polish import Polish
from .ciphers import Ciphers
from .tls_1_3 import TLS1_3
from .zero_rtt import ZeroRTT
from ..._models import BaseModel
from .websocket import Websocket
from .cache_level import CacheLevel
from .early_hints import EarlyHints
from .pseudo_ipv4 import PseudoIPV4
from .advanced_ddos import AdvancedDDoS
from .always_online import AlwaysOnline
from .browser_check import BrowserCheck
from .challenge_ttl import ChallengeTTL
from .rocket_loader import RocketLoader
from .image_resizing import ImageResizing
from .ip_geolocation import IPGeolocation
from .security_level import SecurityLevel
from .min_tls_version import MinTLSVersion
from .mobile_redirect import MobileRedirect
from .ssl_recommender import SSLRecommender
from .tls_client_auth import TLSClientAuth
from .always_use_https import AlwaysUseHTTPS
from .development_mode import DevelopmentMode
from .orange_to_orange import OrangeToOrange
from .prefetch_preload import PrefetchPreload
from .security_headers import SecurityHeaders
from .browser_cache_ttl import BrowserCacheTTL
from .email_obfuscation import EmailObfuscation
from .h2_prioritization import H2Prioritization
from .hotlink_protection import HotlinkProtection
from .proxy_read_timeout import ProxyReadTimeout
from .response_buffering import ResponseBuffering
from .opportunistic_onion import OpportunisticOnion
from .server_side_excludes import ServerSideExcludes
from .true_client_ip_header import TrueClientIPHeader
from .automatic_https_rewrites import AutomaticHTTPSRewrites
from .opportunistic_encryption import OpportunisticEncryption
from .origin_error_page_pass_thru import OriginErrorPagePassThru
from .sort_query_string_for_cache import SortQueryStringForCache
from .automatic_platform_optimization import AutomaticPlatformOptimization

__all__ = [
    "SettingGetResponse",
    "ZonesCNAMEFlattening",
    "ZonesEdgeCacheTTL",
    "ZonesMaxUpload",
    "ZonesReplaceInsecureJS",
    "ZonesSchemasAutomaticPlatformOptimization",
    "ZonesSha1Support",
    "ZonesTLS1_2Only",
]


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


class ZonesEdgeCacheTTL(BaseModel):
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


SettingGetResponse: TypeAlias = Union[
    ZeroRTT,
    AdvancedDDoS,
    AlwaysOnline,
    AlwaysUseHTTPS,
    AutomaticHTTPSRewrites,
    Brotli,
    BrowserCacheTTL,
    BrowserCheck,
    CacheLevel,
    ChallengeTTL,
    Ciphers,
    ZonesCNAMEFlattening,
    DevelopmentMode,
    EarlyHints,
    ZonesEdgeCacheTTL,
    EmailObfuscation,
    H2Prioritization,
    HotlinkProtection,
    HTTP2,
    HTTP3,
    ImageResizing,
    IPGeolocation,
    IPV6,
    ZonesMaxUpload,
    MinTLSVersion,
    Minify,
    Mirage,
    MobileRedirect,
    NEL,
    OpportunisticEncryption,
    OpportunisticOnion,
    OrangeToOrange,
    OriginErrorPagePassThru,
    Polish,
    PrefetchPreload,
    ProxyReadTimeout,
    PseudoIPV4,
    ZonesReplaceInsecureJS,
    ResponseBuffering,
    RocketLoader,
    ZonesSchemasAutomaticPlatformOptimization,
    SecurityHeaders,
    SecurityLevel,
    ServerSideExcludes,
    ZonesSha1Support,
    SortQueryStringForCache,
    SSL,
    SSLRecommender,
    ZonesTLS1_2Only,
    TLS1_3,
    TLSClientAuth,
    TrueClientIPHeader,
    WAF,
    WebP,
    Websocket,
]
