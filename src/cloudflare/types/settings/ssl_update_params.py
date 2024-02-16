# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SSLUpdateParams"]


class SSLUpdateParams(TypedDict, total=False):
    value: Required[Literal["off", "flexible", "full", "strict"]]
    """Value of the zone setting. Notes: Depends on the zone's plan level"""
