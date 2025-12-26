# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["PresetGetResponse", "Data", "Paging"]


class Data(BaseModel):
    """Returned by Get All Presets route"""

    id: Optional[str] = None
    """ID of the preset"""

    created_at: Optional[datetime] = None
    """Timestamp this preset was created at"""

    name: Optional[str] = None
    """Name of the preset"""

    updated_at: Optional[datetime] = None
    """Timestamp this preset was last updated"""


class Paging(BaseModel):
    end_offset: float

    start_offset: float

    total_count: float


class PresetGetResponse(BaseModel):
    data: List[Data]

    paging: Paging

    success: bool
