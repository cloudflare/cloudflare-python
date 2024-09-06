# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["QueryResult", "Meta"]


class Meta(BaseModel):
    changed_db: Optional[bool] = None

    changes: Optional[float] = None

    duration: Optional[float] = None

    last_row_id: Optional[float] = None

    rows_read: Optional[float] = None

    rows_written: Optional[float] = None

    size_after: Optional[float] = None


class QueryResult(BaseModel):
    meta: Optional[Meta] = None

    results: Optional[List[object]] = None

    success: Optional[bool] = None
