# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..cache.cache_variant_identifier import CacheVariantIdentifier

__all__ = ["OriginPostQuantumEncryptionUpdateParams"]


class OriginPostQuantumEncryptionUpdateParams(TypedDict, total=False):
    zone_id: Required[CacheVariantIdentifier]
    """Identifier"""

    value: Required[Literal["preferred", "supported", "off"]]
    """Value of the Origin Post Quantum Encryption Setting."""
