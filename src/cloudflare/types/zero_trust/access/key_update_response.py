# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["KeyUpdateResponse"]


class KeyUpdateResponse(BaseModel):
    days_until_next_rotation: Optional[float] = None
    """The number of days until the next key rotation."""

    key_rotation_interval_days: Optional[float] = None
    """The number of days between key rotations."""

    last_key_rotation_at: Optional[datetime] = None
    """The timestamp of the previous key rotation."""
