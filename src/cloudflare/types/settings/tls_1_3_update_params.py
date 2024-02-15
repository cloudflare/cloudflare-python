# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TLS1_3UpdateParams"]


class TLS1_3UpdateParams(TypedDict, total=False):
    value: Required[Literal["on", "off", "zrt"]]
    """
    Value of the zone setting. Notes: Default value depends on the zone's plan
    level.
    """
