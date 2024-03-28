# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .settings import (
    ZoneSettingNELParam,
    ZoneSettingSSLParam,
    ZoneSettingWAFParam,
    ZoneSetting0rttParam,
    ZoneSettingIPV6Param,
    ZoneSettingWebPParam,
    ZoneSettingHTTP2Param,
    ZoneSettingHTTP3Param,
    ZoneSettingBrotliParam,
    ZoneSettingMinifyParam,
    ZoneSettingMirageParam,
    ZoneSettingPolishParam,
    ZoneSettingTLS1_3Param,
    ZoneSettingCiphersParam,
    ZoneSettingBufferingParam,
    ZoneSettingCacheLevelParam,
    ZoneSettingEarlyHintsParam,
    ZoneSettingPseudoIPV4Param,
    ZoneSettingWebsocketsParam,
    ZoneSettingAdvancedDDoSParam,
    ZoneSettingAlwaysOnlineParam,
    ZoneSettingBrowserCheckParam,
    ZoneSettingChallengeTTLParam,
    ZoneSettingRocketLoaderParam,
    ZoneSettingImageResizingParam,
    ZoneSettingIPGeolocationParam,
    ZoneSettingMinTLSVersionParam,
    ZoneSettingSecurityLevelParam,
    ZoneSettingTLSClientAuthParam,
    ZoneSettingAlwaysUseHTTPSParam,
    ZoneSettingMobileRedirectParam,
    ZoneSettingOrangeToOrangeParam,
    ZoneSettingSecurityHeaderParam,
    ZoneSettingSSLRecommenderParam,
    ZoneSettingBrowserCacheTTLParam,
    ZoneSettingDevelopmentModeParam,
    ZoneSettingPrefetchPreloadParam,
    ZoneSettingEmailObfuscationParam,
    ZoneSettingH2PrioritizationParam,
    ZoneSettingProxyReadTimeoutParam,
    ZoneSettingHotlinkProtectionParam,
    ZoneSettingServerSideExcludeParam,
    ZoneSettingOpportunisticOnionParam,
    ZoneSettingTrueClientIPHeaderParam,
    ZoneSettingAutomaticHTTPSRewritesParam,
    ZoneSettingOpportunisticEncryptionParam,
    ZoneSettingOriginErrorPagePassThruParam,
    ZoneSettingSortQueryStringForCacheParam,
    ZoneSettingAutomaticPlatformOptimizationParam,
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

    value: Required[ZoneSettingAutomaticPlatformOptimizationParam]
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
    ZoneSetting0rttParam,
    ZoneSettingAdvancedDDoSParam,
    ZoneSettingAlwaysOnlineParam,
    ZoneSettingAlwaysUseHTTPSParam,
    ZoneSettingAutomaticHTTPSRewritesParam,
    ZoneSettingBrotliParam,
    ZoneSettingBrowserCacheTTLParam,
    ZoneSettingBrowserCheckParam,
    ZoneSettingCacheLevelParam,
    ZoneSettingChallengeTTLParam,
    ZoneSettingCiphersParam,
    ItemZonesCNAMEFlattening,
    ZoneSettingDevelopmentModeParam,
    ZoneSettingEarlyHintsParam,
    ItemZonesEdgeCacheTTL,
    ZoneSettingEmailObfuscationParam,
    ZoneSettingH2PrioritizationParam,
    ZoneSettingHotlinkProtectionParam,
    ZoneSettingHTTP2Param,
    ZoneSettingHTTP3Param,
    ZoneSettingImageResizingParam,
    ZoneSettingIPGeolocationParam,
    ZoneSettingIPV6Param,
    ItemZonesMaxUpload,
    ZoneSettingMinTLSVersionParam,
    ZoneSettingMinifyParam,
    ZoneSettingMirageParam,
    ZoneSettingMobileRedirectParam,
    ZoneSettingNELParam,
    ZoneSettingOpportunisticEncryptionParam,
    ZoneSettingOpportunisticOnionParam,
    ZoneSettingOrangeToOrangeParam,
    ZoneSettingOriginErrorPagePassThruParam,
    ZoneSettingPolishParam,
    ZoneSettingPrefetchPreloadParam,
    ZoneSettingProxyReadTimeoutParam,
    ZoneSettingPseudoIPV4Param,
    ZoneSettingBufferingParam,
    ZoneSettingRocketLoaderParam,
    ItemZonesSchemasAutomaticPlatformOptimization,
    ZoneSettingSecurityHeaderParam,
    ZoneSettingSecurityLevelParam,
    ZoneSettingServerSideExcludeParam,
    ItemZonesSha1Support,
    ZoneSettingSortQueryStringForCacheParam,
    ZoneSettingSSLParam,
    ZoneSettingSSLRecommenderParam,
    ItemZonesTLS1_2Only,
    ZoneSettingTLS1_3Param,
    ZoneSettingTLSClientAuthParam,
    ZoneSettingTrueClientIPHeaderParam,
    ZoneSettingWAFParam,
    ZoneSettingWebPParam,
    ZoneSettingWebsocketsParam,
]
