# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["CategoryCreateResponse", "Schema", "SchemaAnnotations", "SchemaNumberConstraint"]


class SchemaAnnotations(BaseModel):
    confidence: Optional[bool] = None

    tlp: Optional[bool] = None


class SchemaNumberConstraint(BaseModel):
    integer: Optional[bool] = None

    max: Optional[float] = None

    min: Optional[float] = None


class Schema(BaseModel):
    key: str

    kind: Literal["string", "number", "enum", "date", "array", "object"]

    allowed_values: Optional[List[str]] = FieldInfo(alias="allowedValues", default=None)

    annotations: Optional[SchemaAnnotations] = None

    element: Optional[object] = None

    enforcement: Optional[Literal["error", "warn", "off"]] = None

    format: Optional[Literal["date", "url", "duration", "country"]] = None

    label: Optional[str] = None

    max_length: Optional[int] = FieldInfo(alias="maxLength", default=None)

    number_constraint: Optional[SchemaNumberConstraint] = FieldInfo(alias="numberConstraint", default=None)

    properties: Optional[Dict[str, object]] = None
    """Map of property key to FieldDefinition for object fields.

    Required when kind is 'object'. See FieldDefinition (recursive).
    """

    required: Optional[bool] = None


class CategoryCreateResponse(BaseModel):
    name: str

    uuid: str

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    schema_: Optional[List[Schema]] = FieldInfo(alias="schema", default=None)
    """
    Parsed FieldDefinition[] defining custom fields for this category, or null if
    none.
    """

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)
