# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ChallengeTTL"]


class ChallengeTTL(BaseModel):
    id: Literal["challenge_ttl"]
    """ID of the zone setting."""

    value: Literal[300, 900, 1800, 2700, 3600, 7200, 10800, 14400, 28800, 57600, 86400, 604800, 2592000, 31536000]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""
