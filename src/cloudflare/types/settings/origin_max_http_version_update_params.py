# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OriginMaxHTTPVersionUpdateParams"]


class OriginMaxHTTPVersionUpdateParams(TypedDict, total=False):
    value: Required[Literal["2", "1"]]
    """Value of the Origin Max HTTP Version Setting."""
