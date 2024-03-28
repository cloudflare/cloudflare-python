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
    "SettingEditResponse",
    "SettingEditResponseItem",
    "SettingEditResponseItemZonesCNAMEFlattening",
    "SettingEditResponseItemZonesEdgeCacheTTL",
    "SettingEditResponseItemZonesMaxUpload",
    "SettingEditResponseItemZonesSchemasAutomaticPlatformOptimization",
    "SettingEditResponseItemZonesSha1Support",
    "SettingEditResponseItemZonesTLS1_2Only",
]


class SettingEditResponseItemZonesCNAMEFlattening(BaseModel):
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


class SettingEditResponseItemZonesSchemasAutomaticPlatformOptimization(BaseModel):
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


SettingEditResponseItem = Union[
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
    SettingEditResponseItemZonesCNAMEFlattening,
    ZoneSettingDevelopmentMode,
    ZoneSettingEarlyHints,
    SettingEditResponseItemZonesEdgeCacheTTL,
    ZoneSettingEmailObfuscation,
    ZoneSettingH2Prioritization,
    ZoneSettingHotlinkProtection,
    ZoneSettingHTTP2,
    ZoneSettingHTTP3,
    ZoneSettingImageResizing,
    ZoneSettingIPGeolocation,
    ZoneSettingIPV6,
    SettingEditResponseItemZonesMaxUpload,
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
    SettingEditResponseItemZonesSchemasAutomaticPlatformOptimization,
    ZoneSettingSecurityHeader,
    ZoneSettingSecurityLevel,
    ZoneSettingServerSideExclude,
    SettingEditResponseItemZonesSha1Support,
    ZoneSettingSortQueryStringForCache,
    ZoneSettingSSL,
    ZoneSettingSSLRecommender,
    SettingEditResponseItemZonesTLS1_2Only,
    ZoneSettingTLS1_3,
    ZoneSettingTLSClientAuth,
    ZoneSettingTrueClientIPHeader,
    ZoneSettingWAF,
    ZoneSettingWebP,
    ZoneSettingWebsockets,
]

SettingEditResponse = List[SettingEditResponseItem]
