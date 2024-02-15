# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ....._models import BaseModel
from .....types import shared

__all__ = ["ObjectListResponse", "ObjectListResponseItem"]


class ObjectListResponseItem(BaseModel):
    id: Optional[str] = None
    """ID of the Durable Object."""

    has_stored_data: Optional[bool] = FieldInfo(alias="hasStoredData", default=None)
    """Whether the Durable Object has stored data."""


ObjectListResponse = List[ObjectListResponseItem]
