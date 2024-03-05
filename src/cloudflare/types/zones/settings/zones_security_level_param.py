# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ZonesSecurityLevelParam"]


class ZonesSecurityLevelParam(TypedDict, total=False):
    id: Required[Literal["security_level"]]
    """ID of the zone setting."""

    value: Required[Literal["off", "essentially_off", "low", "medium", "high", "under_attack"]]
    """Current value of the zone setting."""
