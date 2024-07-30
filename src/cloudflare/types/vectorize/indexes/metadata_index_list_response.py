# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["MetadataIndexListResponse", "MetadataIndex"]


class MetadataIndex(BaseModel):
    index_type: Optional[Literal["string", "number", "boolean"]] = FieldInfo(alias="indexType", default=None)
    """Specifies the type of indexed metadata property."""

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)
    """Specifies the indexed metadata property."""


class MetadataIndexListResponse(BaseModel):
    metadata_indexes: Optional[List[MetadataIndex]] = FieldInfo(alias="metadataIndexes", default=None)
    """Array of indexed metadata properties."""
