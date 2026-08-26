# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["CategoryEditParams", "Schema", "SchemaAnnotations", "SchemaNumberConstraint"]


class CategoryEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    description: str

    name: str

    schema: Iterable[Schema]
    """Optional array of FieldDefinition objects.

    When provided, replaces the existing field schema. When omitted, the existing
    schema is preserved.
    """


class SchemaAnnotations(TypedDict, total=False):
    confidence: bool

    tlp: bool


class SchemaNumberConstraint(TypedDict, total=False):
    integer: bool

    max: float

    min: float


class Schema(TypedDict, total=False):
    key: Required[str]

    kind: Required[Literal["string", "number", "enum", "date", "array", "object"]]

    allowed_values: Annotated[SequenceNotStr[str], PropertyInfo(alias="allowedValues")]

    annotations: SchemaAnnotations

    element: object

    enforcement: Literal["error", "warn", "off"]

    format: Literal["date", "url", "duration", "country"]

    label: str

    max_length: Annotated[int, PropertyInfo(alias="maxLength")]

    number_constraint: Annotated[SchemaNumberConstraint, PropertyInfo(alias="numberConstraint")]

    properties: Dict[str, object]
    """Map of property key to FieldDefinition for object fields.

    Required when kind is 'object'. See FieldDefinition (recursive).
    """

    required: bool
