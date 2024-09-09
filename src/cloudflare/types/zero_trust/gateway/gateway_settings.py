# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["GatewaySettings"]


class GatewaySettings(BaseModel):
    created_at: Optional[datetime] = None

    public_key: Optional[str] = None
    """SSH encryption public key"""

    seed_id: Optional[str] = None
    """Seed ID"""

    updated_at: Optional[datetime] = None
