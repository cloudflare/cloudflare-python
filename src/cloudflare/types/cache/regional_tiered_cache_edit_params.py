# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .cache_variant_identifier import CacheVariantIdentifier

__all__ = ["RegionalTieredCacheEditParams"]


class RegionalTieredCacheEditParams(TypedDict, total=False):
    zone_id: Required[CacheVariantIdentifier]
    """Identifier"""

    value: Required[Literal["on", "off"]]
    """Value of the Regional Tiered Cache zone setting."""
