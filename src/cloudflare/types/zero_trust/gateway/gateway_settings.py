# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["GatewaySettings"]

class GatewaySettings(BaseModel):
    created_at: Optional[datetime] = None

    public_key: Optional[str] = None
    """SSH encryption public key"""

    seed_id: Optional[str] = None
    """Seed ID"""

    updated_at: Optional[datetime] = None