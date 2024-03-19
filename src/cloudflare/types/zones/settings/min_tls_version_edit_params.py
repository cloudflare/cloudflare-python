# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MinTLSVersionEditParams"]


class MinTLSVersionEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    value: Required[Literal["1.0", "1.1", "1.2", "1.3"]]
    """Value of the zone setting."""
