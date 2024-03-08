# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ZonesTLS1_3Param"]


class ZonesTLS1_3Param(TypedDict, total=False):
    id: Required[Literal["tls_1_3"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off", "zrt"]]
    """Current value of the zone setting."""
