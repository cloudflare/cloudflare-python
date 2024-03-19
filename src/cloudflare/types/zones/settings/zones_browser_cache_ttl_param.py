# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ZonesBrowserCacheTTLParam"]


class ZonesBrowserCacheTTLParam(TypedDict, total=False):
    id: Required[Literal["browser_cache_ttl"]]
    """ID of the zone setting."""

    value: Required[
        Literal[
            0,
            30,
            60,
            120,
            300,
            1200,
            1800,
            3600,
            7200,
            10800,
            14400,
            18000,
            28800,
            43200,
            57600,
            72000,
            86400,
            172800,
            259200,
            345600,
            432000,
            691200,
            1382400,
            2073600,
            2678400,
            5356800,
            16070400,
            31536000,
        ]
    ]
    """Current value of the zone setting."""
