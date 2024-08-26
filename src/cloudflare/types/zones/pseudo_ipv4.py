# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PseudoIPV4"]


class PseudoIPV4(BaseModel):
    id: Literal["pseudo_ipv4"]
    """Value of the Pseudo IPv4 setting."""

    value: Literal["off", "add_header", "overwrite_header"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""
