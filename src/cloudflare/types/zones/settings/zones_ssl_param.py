# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ZonesSSLParam"]


class ZonesSSLParam(TypedDict, total=False):
    id: Required[Literal["ssl"]]
    """ID of the zone setting."""

    value: Required[Literal["off", "flexible", "full", "strict"]]
    """Current value of the zone setting."""
