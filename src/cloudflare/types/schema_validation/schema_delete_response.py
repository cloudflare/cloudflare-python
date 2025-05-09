# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["SchemaDeleteResponse"]


class SchemaDeleteResponse(BaseModel):
    schema_id: str
    """The ID of the schema that was just deleted"""
