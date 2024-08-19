# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BrowserCacheTTL"]


class BrowserCacheTTL(BaseModel):
    id: Literal["browser_cache_ttl"]
    """ID of the zone setting."""

    value: Literal[
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
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""
