# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SmartShieldGetResponse", "CacheReserve", "RegionalTieredCache", "SmartRouting", "SmartTieredCache"]


class CacheReserve(BaseModel):
    id: Optional[str] = None
    """The id of the Cache Reserve setting."""

    editable: Optional[bool] = None
    """Whether the setting is editable."""

    value: Optional[Literal["on", "off"]] = None
    """Specifies the enablement value of Cache Reserve."""


class RegionalTieredCache(BaseModel):
    id: Optional[str] = None
    """The id of the Regional Tiered Cache setting."""

    editable: Optional[bool] = None
    """Whether the setting is editable."""

    value: Optional[Literal["on", "off"]] = None
    """Specifies the enablement value of Cache Reserve."""


class SmartRouting(BaseModel):
    id: Optional[str] = None
    """The id of the Smart Routing setting."""

    editable: Optional[bool] = None
    """Whether the setting is editable."""

    value: Optional[Literal["on", "off"]] = None
    """Specifies the enablement value of Argo Smart Routing."""


class SmartTieredCache(BaseModel):
    id: Optional[str] = None
    """The id of the Smart Tiered Cache setting."""

    editable: Optional[bool] = None
    """Whether the setting is editable."""

    modified_on: Optional[str] = None
    """The last time the setting was modified."""

    value: Optional[Literal["on", "off"]] = None
    """Specifies the enablement value of Tiered Cache."""


class SmartShieldGetResponse(BaseModel):
    cache_reserve: Optional[CacheReserve] = None

    healthchecks_count: Optional[int] = None
    """The total number of health checks associated with the zone."""

    regional_tiered_cache: Optional[RegionalTieredCache] = None

    smart_routing: Optional[SmartRouting] = None

    smart_tiered_cache: Optional[SmartTieredCache] = None
