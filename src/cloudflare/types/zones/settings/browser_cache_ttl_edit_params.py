# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BrowserCacheTTLEditParams"]


class BrowserCacheTTLEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

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
    """
    Value of the zone setting. Notes: Setting a TTL of 0 is equivalent to selecting
    `Respect Existing Headers`
    """
