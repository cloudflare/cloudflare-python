# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["GlobalWARPOverrideGetResponse"]


class GlobalWARPOverrideGetResponse(BaseModel):
    disconnect: Optional[bool] = None
    """Disconnects all devices on the account using Global WARP override."""

    timestamp: Optional[datetime] = None
    """When the Global WARP override state was updated."""
