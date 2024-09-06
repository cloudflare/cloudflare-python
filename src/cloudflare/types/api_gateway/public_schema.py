# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from datetime import datetime

from typing_extensions import Literal

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["PublicSchema"]


class PublicSchema(BaseModel):
    created_at: datetime

    kind: Literal["openapi_v3"]
    """Kind of schema"""

    name: str
    """Name of the schema"""

    schema_id: str
    """UUID"""

    source: Optional[str] = None
    """Source of the schema"""

    validation_enabled: Optional[bool] = None
    """Flag whether schema is enabled for validation."""
