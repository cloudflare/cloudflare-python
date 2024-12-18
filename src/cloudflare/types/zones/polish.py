# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Polish"]


class Polish(BaseModel):
    id: Optional[Literal["polish"]] = None
    """Apply options from the Polish feature of the Cloudflare Speed app."""

    value: Optional[Literal["off", "lossless", "lossy"]] = None
    """The level of Polish you want applied to your origin."""
