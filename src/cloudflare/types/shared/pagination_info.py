# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PaginationInfo"]


class PaginationInfo(BaseModel):
    count: Optional[float] = None
    """Total number of results for the requested service"""

    page: Optional[float] = None
    """Current page within paginated list of results"""

    per_page: Optional[float] = None
    """Number of results per page of results"""

    total_count: Optional[float] = None
    """Total results available without any search parameters"""
