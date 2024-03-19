# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChallengeTTLEditParams"]


class ChallengeTTLEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    value: Required[
        Literal[300, 900, 1800, 2700, 3600, 7200, 10800, 14400, 28800, 57600, 86400, 604800, 2592000, 31536000]
    ]
    """Value of the zone setting."""
