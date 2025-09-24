# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SmartShieldUpdateParams", "CacheReserve", "RegionalTieredCache", "SmartRouting", "SmartTieredCache"]


class SmartShieldUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    cache_reserve: CacheReserve

    regional_tiered_cache: RegionalTieredCache

    smart_routing: SmartRouting

    smart_tiered_cache: SmartTieredCache


class CacheReserve(TypedDict, total=False):
    value: Literal["on", "off"]
    """Specifies the enablement value of Cache Reserve."""


class RegionalTieredCache(TypedDict, total=False):
    value: Literal["on", "off"]
    """Specifies the enablement value of Regional Tiered Cache."""


class SmartRouting(TypedDict, total=False):
    value: Literal["on", "off"]
    """Specifies the enablement value of Smart Routing."""


class SmartTieredCache(TypedDict, total=False):
    value: Literal["on", "off"]
    """Specifies the enablement value of Smart Tiered Cache."""
