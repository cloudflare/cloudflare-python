# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OriginMaxHTTPVersionEditParams"]


class OriginMaxHTTPVersionEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    value: Required[Literal["2", "1"]]
    """Value of the Origin Max HTTP Version Setting."""
