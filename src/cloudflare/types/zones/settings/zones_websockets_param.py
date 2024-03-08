# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ZonesWebsocketsParam"]


class ZonesWebsocketsParam(TypedDict, total=False):
    id: Required[Literal["websockets"]]
    """ID of the zone setting."""

    value: Required[Literal["off", "on"]]
    """Current value of the zone setting."""
