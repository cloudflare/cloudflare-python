# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["BasicAuthSecret"]


class BasicAuthSecret(BaseModel):
    id: str
    """Server-assigned UUID"""

    created_at: datetime

    expires_at: Optional[datetime] = None
    """Optional RFC 3339 expiration time. Omit for no expiration."""
