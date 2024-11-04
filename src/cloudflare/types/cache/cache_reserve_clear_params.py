# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .cache_variant_identifier import CacheVariantIdentifier

__all__ = ["CacheReserveClearParams"]


class CacheReserveClearParams(TypedDict, total=False):
    zone_id: Required[CacheVariantIdentifier]
    """Identifier"""

    body: Required[object]
