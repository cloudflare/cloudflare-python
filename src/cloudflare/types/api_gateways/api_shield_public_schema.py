# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["APIShieldPublicSchema"]


class APIShieldPublicSchema(BaseModel):
    created_at: datetime

    kind: Literal["openapi_v3"]
    """Kind of schema"""

    name: str
    """Name of the schema"""

    schema_id: str
    """UUID identifier"""

    source: Optional[str] = None
    """Source of the schema"""

    validation_enabled: Optional[bool] = None
    """Flag whether schema is enabled for validation."""
