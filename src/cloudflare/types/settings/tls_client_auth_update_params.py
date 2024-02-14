# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TLSClientAuthUpdateParams"]


class TLSClientAuthUpdateParams(TypedDict, total=False):
    value: Required[Literal["on", "off"]]
    """value of the zone setting."""
