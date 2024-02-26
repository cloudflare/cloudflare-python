# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebpEditParams"]


class WebpEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    value: Required[Literal["off", "on"]]
    """Value of the zone setting."""
