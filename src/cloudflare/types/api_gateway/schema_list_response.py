# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["SchemaListResponse"]


class SchemaListResponse(BaseModel):
    schemas: Optional[List[object]] = None

    timestamp: Optional[str] = None
