# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["SchemaAPIShieldEndpointManagementGetOperationsAndFeaturesAsOpenAPISchemasResponse"]


class SchemaAPIShieldEndpointManagementGetOperationsAndFeaturesAsOpenAPISchemasResponse(BaseModel):
    schemas: Optional[List[object]] = None

    timestamp: Optional[str] = None
