# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DynamicRoutingListVersionsResponse", "Data", "DataVersion"]


class DataVersion(BaseModel):
    active: Literal["true", "false"]

    created_at: str

    data: str

    version_id: str

    comment: Optional[str] = None


class Data(BaseModel):
    order_by: str

    order_by_direction: str

    page: float

    per_page: float

    versions: List[DataVersion]


class DynamicRoutingListVersionsResponse(BaseModel):
    data: Data

    success: bool
