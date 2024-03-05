# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ZonesAlwaysOnlineParam"]


class ZonesAlwaysOnlineParam(TypedDict, total=False):
    id: Required[Literal["always_online"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""
