# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["Stat", "Count"]


class Count(BaseModel):
    allowed: Optional[float] = None
    """Cloudflare Images allowed usage."""

    current: Optional[float] = None
    """Cloudflare Images current usage."""


class Stat(BaseModel):
    count: Optional[Count] = None
