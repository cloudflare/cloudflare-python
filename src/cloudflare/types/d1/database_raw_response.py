# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from ..._models import BaseModel

__all__ = ["DatabaseRawResponse", "Meta", "Results"]


class Meta(BaseModel):
    changed_db: Optional[bool] = None

    changes: Optional[float] = None

    duration: Optional[float] = None

    last_row_id: Optional[float] = None

    rows_read: Optional[float] = None

    rows_written: Optional[float] = None

    size_after: Optional[float] = None


class Results(BaseModel):
    columns: Optional[List[str]] = None

    rows: Optional[List[List[Union[float, str, object]]]] = None


class DatabaseRawResponse(BaseModel):
    meta: Optional[Meta] = None

    results: Optional[Results] = None

    success: Optional[bool] = None
