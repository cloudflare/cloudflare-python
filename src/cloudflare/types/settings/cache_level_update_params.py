# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CacheLevelUpdateParams"]


class CacheLevelUpdateParams(TypedDict, total=False):
    value: Required[Literal["aggressive", "basic", "simplified"]]
    """Value of the zone setting."""
