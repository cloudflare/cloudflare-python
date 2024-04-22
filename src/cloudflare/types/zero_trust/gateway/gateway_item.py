# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["GatewayItem"]


class GatewayItem(BaseModel):
    created_at: Optional[datetime] = None

    value: Optional[str] = None
    """The value of the item in a list."""
