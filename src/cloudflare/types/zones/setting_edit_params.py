# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .settings import (
    ZonesNELParam,
    ZonesSSLParam,
    ZonesWAFParam,
    Zones0rttParam,
    ZonesIPV6Param,
    ZonesWebPParam,
    ZonesHTTP2Param,
    ZonesHTTP3Param,
    ZonesBrotliParam,
    ZonesMinifyParam,
    ZonesMirageParam,
    ZonesPolishParam,
    ZonesTLS1_3Param,
    ZonesCiphersParam,
    ZonesBufferingParam,
    ZonesCacheLevelParam,
    ZonesEarlyHintsParam,
    ZonesPseudoIPV4Param,
    ZonesWebsocketsParam,
    ZonesAdvancedDDOSParam,
    ZonesAlwaysOnlineParam,
    ZonesBrowserCheckParam,
    ZonesChallengeTTLParam,
    ZonesRocketLoaderParam,
    ZonesImageResizingParam,
    ZonesIPGeolocationParam,
    ZonesMinTLSVersionParam,
    ZonesSecurityLevelParam,
    ZonesTLSClientAuthParam,
    ZonesAlwaysUseHTTPSParam,
    ZonesMobileRedirectParam,
    ZonesOrangeToOrangeParam,
    ZonesSecurityHeaderParam,
    ZonesSSLRecommenderParam,
    ZonesBrowserCacheTTLParam,
    ZonesDevelopmentModeParam,
    ZonesPrefetchPreloadParam,
    ZonesEmailObfuscationParam,
    ZonesH2PrioritizationParam,
    ZonesProxyReadTimeoutParam,
    ZonesHotlinkProtectionParam,
    ZonesServerSideExcludeParam,
    ZonesOpportunisticOnionParam,
    ZonesTrueClientIPHeaderParam,
    ZonesAutomaticHTTPSRewritesParam,
    ZonesOpportunisticEncryptionParam,
    ZonesOriginErrorPagePassThruParam,
    ZonesSortQueryStringForCacheParam,
    ZonesAutomaticPlatformOptimizationParam,
)

__all__ = [
    "SettingEditParams",
    "Item",
    "ItemZonesCNAMEFlattening",
    "ItemZonesEdgeCacheTTL",
    "ItemZonesMaxUpload",
    "ItemZonesSchemasAutomaticPlatformOptimization",
    "ItemZonesSha1Support",
    "ItemZonesTLS1_2Only",
]


class SettingEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    items: Required[Iterable[Item]]
    """One or more zone setting objects. Must contain an ID and a value."""


class ItemZonesCNAMEFlattening(TypedDict, total=False):
    id: Required[Literal["cname_flattening"]]
    """How to flatten the cname destination."""

    value: Required[Literal["flatten_at_root", "flatten_all"]]
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


class ItemZonesMaxUpload(TypedDict, total=False):
    id: Required[Literal["max_upload"]]
    """identifier of the zone setting."""

    value: Required[Literal[100, 200, 500]]
    """Current value of the zone setting."""


class ItemZonesSchemasAutomaticPlatformOptimization(TypedDict, total=False):
    id: Required[Literal["automatic_platform_optimization"]]
    """ID of the zone setting."""

    value: Required[ZonesAutomaticPlatformOptimizationParam]
    """Current value of the zone setting."""


class ItemZonesSha1Support(TypedDict, total=False):
    id: Required[Literal["sha1_support"]]
    """Zone setting identifier."""

    value: Required[Literal["off", "on"]]
    """Current value of the zone setting."""


class ItemZonesTLS1_2Only(TypedDict, total=False):
    id: Required[Literal["tls_1_2_only"]]
    """Zone setting identifier."""

    value: Required[Literal["off", "on"]]
    """Current value of the zone setting."""


Item = Union[
    Zones0rttParam,
    ZonesAdvancedDDOSParam,
    ZonesAlwaysOnlineParam,
    ZonesAlwaysUseHTTPSParam,
    ZonesAutomaticHTTPSRewritesParam,
    ZonesBrotliParam,
    ZonesBrowserCacheTTLParam,
    ZonesBrowserCheckParam,
    ZonesCacheLevelParam,
    ZonesChallengeTTLParam,
    ZonesCiphersParam,
    ItemZonesCNAMEFlattening,
    ZonesDevelopmentModeParam,
    ZonesEarlyHintsParam,
    ItemZonesEdgeCacheTTL,
    ZonesEmailObfuscationParam,
    ZonesH2PrioritizationParam,
    ZonesHotlinkProtectionParam,
    ZonesHTTP2Param,
    ZonesHTTP3Param,
    ZonesImageResizingParam,
    ZonesIPGeolocationParam,
    ZonesIPV6Param,
    ItemZonesMaxUpload,
    ZonesMinTLSVersionParam,
    ZonesMinifyParam,
    ZonesMirageParam,
    ZonesMobileRedirectParam,
    ZonesNELParam,
    ZonesOpportunisticEncryptionParam,
    ZonesOpportunisticOnionParam,
    ZonesOrangeToOrangeParam,
    ZonesOriginErrorPagePassThruParam,
    ZonesPolishParam,
    ZonesPrefetchPreloadParam,
    ZonesProxyReadTimeoutParam,
    ZonesPseudoIPV4Param,
    ZonesBufferingParam,
    ZonesRocketLoaderParam,
    ItemZonesSchemasAutomaticPlatformOptimization,
    ZonesSecurityHeaderParam,
    ZonesSecurityLevelParam,
    ZonesServerSideExcludeParam,
    ItemZonesSha1Support,
    ZonesSortQueryStringForCacheParam,
    ZonesSSLParam,
    ZonesSSLRecommenderParam,
    ItemZonesTLS1_2Only,
    ZonesTLS1_3Param,
    ZonesTLSClientAuthParam,
    ZonesTrueClientIPHeaderParam,
    ZonesWAFParam,
    ZonesWebPParam,
    ZonesWebsocketsParam,
]
