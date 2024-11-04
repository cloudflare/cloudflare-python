# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CacheReserveEditParams"]


class CacheReserveEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    value: Required[Literal["on", "off"]]
    """Value of the Cache Reserve zone setting."""
