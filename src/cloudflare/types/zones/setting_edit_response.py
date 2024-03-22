# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .settings import (
    ZonesNEL,
    ZonesSSL,
    ZonesWAF,
    Zones0rtt,
    ZonesIPV6,
    ZonesWebP,
    ZonesHTTP2,
    ZonesHTTP3,
    ZonesBrotli,
    ZonesMinify,
    ZonesMirage,
    ZonesPolish,
    ZonesTLS1_3,
    ZonesCiphers,
    ZonesBuffering,
    ZonesCacheLevel,
    ZonesEarlyHints,
    ZonesPseudoIPV4,
    ZonesWebsockets,
    ZonesAdvancedDDOS,
    ZonesAlwaysOnline,
    ZonesBrowserCheck,
    ZonesChallengeTTL,
    ZonesRocketLoader,
    ZonesImageResizing,
    ZonesIPGeolocation,
    ZonesMinTLSVersion,
    ZonesSecurityLevel,
    ZonesTLSClientAuth,
    ZonesAlwaysUseHTTPS,
    ZonesMobileRedirect,
    ZonesOrangeToOrange,
    ZonesSecurityHeader,
    ZonesSSLRecommender,
    ZonesBrowserCacheTTL,
    ZonesDevelopmentMode,
    ZonesPrefetchPreload,
    ZonesEmailObfuscation,
    ZonesH2Prioritization,
    ZonesProxyReadTimeout,
    ZonesHotlinkProtection,
    ZonesServerSideExclude,
    ZonesOpportunisticOnion,
    ZonesTrueClientIPHeader,
    ZonesAutomaticHTTPSRewrites,
    ZonesOpportunisticEncryption,
    ZonesOriginErrorPagePassThru,
    ZonesSortQueryStringForCache,
    ZonesAutomaticPlatformOptimization,
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

    value: ZonesAutomaticPlatformOptimization
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
    Zones0rtt,
    ZonesAdvancedDDOS,
    ZonesAlwaysOnline,
    ZonesAlwaysUseHTTPS,
    ZonesAutomaticHTTPSRewrites,
    ZonesBrotli,
    ZonesBrowserCacheTTL,
    ZonesBrowserCheck,
    ZonesCacheLevel,
    ZonesChallengeTTL,
    ZonesCiphers,
    SettingEditResponseItemZonesCNAMEFlattening,
    ZonesDevelopmentMode,
    ZonesEarlyHints,
    SettingEditResponseItemZonesEdgeCacheTTL,
    ZonesEmailObfuscation,
    ZonesH2Prioritization,
    ZonesHotlinkProtection,
    ZonesHTTP2,
    ZonesHTTP3,
    ZonesImageResizing,
    ZonesIPGeolocation,
    ZonesIPV6,
    SettingEditResponseItemZonesMaxUpload,
    ZonesMinTLSVersion,
    ZonesMinify,
    ZonesMirage,
    ZonesMobileRedirect,
    ZonesNEL,
    ZonesOpportunisticEncryption,
    ZonesOpportunisticOnion,
    ZonesOrangeToOrange,
    ZonesOriginErrorPagePassThru,
    ZonesPolish,
    ZonesPrefetchPreload,
    ZonesProxyReadTimeout,
    ZonesPseudoIPV4,
    ZonesBuffering,
    ZonesRocketLoader,
    SettingEditResponseItemZonesSchemasAutomaticPlatformOptimization,
    ZonesSecurityHeader,
    ZonesSecurityLevel,
    ZonesServerSideExclude,
    SettingEditResponseItemZonesSha1Support,
    ZonesSortQueryStringForCache,
    ZonesSSL,
    ZonesSSLRecommender,
    SettingEditResponseItemZonesTLS1_2Only,
    ZonesTLS1_3,
    ZonesTLSClientAuth,
    ZonesTrueClientIPHeader,
    ZonesWAF,
    ZonesWebP,
    ZonesWebsockets,
]

SettingEditResponse = List[SettingEditResponseItem]
