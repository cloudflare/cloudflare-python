# File generated from our OpenAPI spec by Stainless.

from datetime import datetime

from typing_extensions import Literal

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

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
