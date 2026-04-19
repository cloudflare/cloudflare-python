# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["IndexListVectorsResponse", "Vector"]


class Vector(BaseModel):
    id: str
    """Identifier for a Vector"""


class IndexListVectorsResponse(BaseModel):
    count: int
    """Number of vectors returned in this response"""

    is_truncated: bool = FieldInfo(alias="isTruncated")
    """Whether there are more vectors available beyond this response"""

    total_count: int = FieldInfo(alias="totalCount")
    """Total number of vectors in the index"""

    vectors: List[Vector]
    """Array of vector items"""

    cursor_expiration_timestamp: Optional[datetime] = FieldInfo(alias="cursorExpirationTimestamp", default=None)
    """When the cursor expires as an ISO8601 string"""

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """Cursor for the next page of results"""
