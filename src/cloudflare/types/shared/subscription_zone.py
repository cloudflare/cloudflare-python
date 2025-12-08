# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SubscriptionZone"]


class SubscriptionZone(BaseModel):
    """A simple zone object. May have null properties if not a zone subscription."""

    id: Optional[str] = None
    """Identifier"""

    name: Optional[str] = None
    """The domain name"""
