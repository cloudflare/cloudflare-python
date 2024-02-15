# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ResponseBufferingUpdateParams"]


class ResponseBufferingUpdateParams(TypedDict, total=False):
    value: Required[Literal["on", "off"]]
    """Value of the zone setting."""
