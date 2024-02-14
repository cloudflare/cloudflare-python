# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["ObjectListResponse", "ObjectListResponseItem"]


class ObjectListResponseItem(BaseModel):
    id: Optional[str] = None
    """ID of the Durable Object."""

    has_stored_data: Optional[bool] = FieldInfo(alias="hasStoredData", default=None)
    """Whether the Durable Object has stored data."""


ObjectListResponse = List[ObjectListResponseItem]
