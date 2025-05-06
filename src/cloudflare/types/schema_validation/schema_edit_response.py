# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SchemaEditResponse"]


class SchemaEditResponse(BaseModel):
    created_at: datetime

    kind: Literal["openapi_v3"]
    """The kind of the schema"""

    name: str
    """A human-readable name for the schema"""

    schema_id: str
    """A unique identifier of this schema"""

    source: str
    """The raw schema, e.g., the OpenAPI schema, either as JSON or YAML"""

    validation_enabled: Optional[bool] = None
    """An indicator if this schema is enabled"""
