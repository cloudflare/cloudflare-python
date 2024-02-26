# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ASNGetParams"]


class ASNGetParams(TypedDict, total=False):
    format: Literal["JSON", "CSV"]
    """Format results are returned in."""
