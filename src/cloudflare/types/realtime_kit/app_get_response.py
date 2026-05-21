# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["AppGetResponse", "Data", "Paging"]


class Data(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = None

    name: Optional[str] = None


class Paging(BaseModel):
    end_offset: Optional[float] = None

    start_offset: Optional[float] = None

    total_count: Optional[float] = None


class AppGetResponse(BaseModel):
    data: Optional[List[Data]] = None

    paging: Optional[Paging] = None

    success: Optional[bool] = None
