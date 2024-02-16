# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MinTLSVersionUpdateParams"]


class MinTLSVersionUpdateParams(TypedDict, total=False):
    value: Required[Literal["1.0", "1.1", "1.2", "1.3"]]
    """Value of the zone setting."""
