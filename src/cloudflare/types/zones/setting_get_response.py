# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .settings import (
    ZoneSettingNEL,
    ZoneSettingSSL,
    ZoneSettingWAF,
    ZoneSetting0rtt,
    ZoneSettingIPV6,
    ZoneSettingWebP,
    ZoneSettingHTTP2,
    ZoneSettingHTTP3,
    ZoneSettingBrotli,
    ZoneSettingMinify,
    ZoneSettingMirage,
    ZoneSettingPolish,
    ZoneSettingTLS1_3,
    ZoneSettingCiphers,
    ZoneSettingBuffering,
    ZoneSettingCacheLevel,
    ZoneSettingEarlyHints,
    ZoneSettingPseudoIPV4,
    ZoneSettingWebsockets,
    ZoneSettingAdvancedDDoS,
    ZoneSettingAlwaysOnline,
    ZoneSettingBrowserCheck,
    ZoneSettingChallengeTTL,
    ZoneSettingRocketLoader,
    ZoneSettingImageResizing,
    ZoneSettingIPGeolocation,
    ZoneSettingMinTLSVersion,
    ZoneSettingSecurityLevel,
    ZoneSettingTLSClientAuth,
    ZoneSettingAlwaysUseHTTPS,
    ZoneSettingMobileRedirect,
    ZoneSettingOrangeToOrange,
    ZoneSettingSecurityHeader,
    ZoneSettingSSLRecommender,
    ZoneSettingBrowserCacheTTL,
    ZoneSettingDevelopmentMode,
    ZoneSettingPrefetchPreload,
    ZoneSettingEmailObfuscation,
    ZoneSettingH2Prioritization,
    ZoneSettingProxyReadTimeout,
    ZoneSettingHotlinkProtection,
    ZoneSettingServerSideExclude,
    ZoneSettingOpportunisticOnion,
    ZoneSettingTrueClientIPHeader,
    ZoneSettingAutomaticHTTPSRewrites,
    ZoneSettingOpportunisticEncryption,
    ZoneSettingOriginErrorPagePassThru,
    ZoneSettingSortQueryStringForCache,
    ZoneSettingAutomaticPlatformOptimization,
)
from ..._models import BaseModel

__all__ = [
    "SettingGetResponse",
    "SettingGetResponseItem",
    "SettingGetResponseItemZonesCNAMEFlattening",
    "SettingGetResponseItemZonesEdgeCacheTTL",
    "SettingGetResponseItemZonesMaxUpload",
    "SettingGetResponseItemZonesSchemasAutomaticPlatformOptimization",
    "SettingGetResponseItemZonesSha1Support",
    "SettingGetResponseItemZonesTLS1_2Only",
]


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


class SettingGetResponseItemZonesSchemasAutomaticPlatformOptimization(BaseModel):
    id: Literal["automatic_platform_optimization"]
    """ID of the zone setting."""

    value: ZoneSettingAutomaticPlatformOptimization
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


SettingGetResponseItem = Union[
    ZoneSetting0rtt,
    ZoneSettingAdvancedDDoS,
    ZoneSettingAlwaysOnline,
    ZoneSettingAlwaysUseHTTPS,
    ZoneSettingAutomaticHTTPSRewrites,
    ZoneSettingBrotli,
    ZoneSettingBrowserCacheTTL,
    ZoneSettingBrowserCheck,
    ZoneSettingCacheLevel,
    ZoneSettingChallengeTTL,
    ZoneSettingCiphers,
    SettingGetResponseItemZonesCNAMEFlattening,
    ZoneSettingDevelopmentMode,
    ZoneSettingEarlyHints,
    SettingGetResponseItemZonesEdgeCacheTTL,
    ZoneSettingEmailObfuscation,
    ZoneSettingH2Prioritization,
    ZoneSettingHotlinkProtection,
    ZoneSettingHTTP2,
    ZoneSettingHTTP3,
    ZoneSettingImageResizing,
    ZoneSettingIPGeolocation,
    ZoneSettingIPV6,
    SettingGetResponseItemZonesMaxUpload,
    ZoneSettingMinTLSVersion,
    ZoneSettingMinify,
    ZoneSettingMirage,
    ZoneSettingMobileRedirect,
    ZoneSettingNEL,
    ZoneSettingOpportunisticEncryption,
    ZoneSettingOpportunisticOnion,
    ZoneSettingOrangeToOrange,
    ZoneSettingOriginErrorPagePassThru,
    ZoneSettingPolish,
    ZoneSettingPrefetchPreload,
    ZoneSettingProxyReadTimeout,
    ZoneSettingPseudoIPV4,
    ZoneSettingBuffering,
    ZoneSettingRocketLoader,
    SettingGetResponseItemZonesSchemasAutomaticPlatformOptimization,
    ZoneSettingSecurityHeader,
    ZoneSettingSecurityLevel,
    ZoneSettingServerSideExclude,
    SettingGetResponseItemZonesSha1Support,
    ZoneSettingSortQueryStringForCache,
    ZoneSettingSSL,
    ZoneSettingSSLRecommender,
    SettingGetResponseItemZonesTLS1_2Only,
    ZoneSettingTLS1_3,
    ZoneSettingTLSClientAuth,
    ZoneSettingTrueClientIPHeader,
    ZoneSettingWAF,
    ZoneSettingWebP,
    ZoneSettingWebsockets,
]

SettingGetResponse = List[SettingGetResponseItem]
