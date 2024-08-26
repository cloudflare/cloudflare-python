# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TieredCachingEditParams"]


class TieredCachingEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    value: Required[Literal["on", "off"]]
    """Enables Tiered Caching."""
