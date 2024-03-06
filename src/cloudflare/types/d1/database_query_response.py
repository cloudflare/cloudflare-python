# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["DatabaseQueryResponse", "DatabaseQueryResponseItem", "DatabaseQueryResponseItemMeta"]


class DatabaseQueryResponseItemMeta(BaseModel):
    changed_db: Optional[bool] = None

    changes: Optional[float] = None

    duration: Optional[float] = None

    last_row_id: Optional[float] = None

    rows_read: Optional[float] = None

    rows_written: Optional[float] = None

    size_after: Optional[float] = None


class DatabaseQueryResponseItem(BaseModel):
    meta: Optional[DatabaseQueryResponseItemMeta] = None

    results: Optional[List[object]] = None

    success: Optional[bool] = None


DatabaseQueryResponse = List[DatabaseQueryResponseItem]
