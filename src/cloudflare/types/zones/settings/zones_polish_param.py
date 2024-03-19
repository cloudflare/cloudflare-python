# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ZonesPolishParam"]


class ZonesPolishParam(TypedDict, total=False):
    id: Required[Literal["polish"]]
    """ID of the zone setting."""

    value: Required[Literal["off", "lossless", "lossy"]]
    """Current value of the zone setting."""
