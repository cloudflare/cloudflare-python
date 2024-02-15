# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["DatabaseListResponse", "DatabaseListResponseItem"]


class DatabaseListResponseItem(BaseModel):
    created_at: Optional[object] = None
    """Specifies the timestamp the resource was created as an ISO8601 string."""

    name: Optional[str] = None

    uuid: Optional[str] = None

    version: Optional[str] = None


DatabaseListResponse = List[DatabaseListResponseItem]
