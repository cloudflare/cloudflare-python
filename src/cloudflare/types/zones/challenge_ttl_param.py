# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChallengeTTLParam"]


class ChallengeTTLParam(TypedDict, total=False):
    id: Required[Literal["challenge_ttl"]]
    """ID of the zone setting."""

    value: Required[
        Literal[300, 900, 1800, 2700, 3600, 7200, 10800, 14400, 28800, 57600, 86400, 604800, 2592000, 31536000]
    ]
    """Current value of the zone setting."""
