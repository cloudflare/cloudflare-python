# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = [
    "DatabaseRawResponse",
    "DatabaseRawResponseItem",
    "DatabaseRawResponseItemMeta",
    "DatabaseRawResponseItemResults",
]


class DatabaseRawResponseItemMeta(BaseModel):
    changed_db: Optional[bool] = None

    changes: Optional[float] = None

    duration: Optional[float] = None

    last_row_id: Optional[float] = None

    rows_read: Optional[float] = None

    rows_written: Optional[float] = None

    size_after: Optional[float] = None


class DatabaseRawResponseItemResults(BaseModel):
    columns: Optional[List[str]] = None

    rows: Optional[List[List[Union[float, str, object]]]] = None


class DatabaseRawResponseItem(BaseModel):
    meta: Optional[DatabaseRawResponseItemMeta] = None

    results: Optional[DatabaseRawResponseItemResults] = None

    success: Optional[bool] = None


DatabaseRawResponse: TypeAlias = List[DatabaseRawResponseItem]
