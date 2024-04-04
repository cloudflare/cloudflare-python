# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..shared import UnnamedSchemaRef172
from ..._models import BaseModel

__all__ = ["TestListResponse", "ResultInfo"]


class ResultInfo(BaseModel):
    count: Optional[int] = None

    page: Optional[int] = None

    per_page: Optional[int] = None

    total_count: Optional[int] = None


class TestListResponse(BaseModel):
    __test__ = False
    errors: List[UnnamedSchemaRef172]

    messages: List[UnnamedSchemaRef172]

    success: bool
    """Whether the API call was successful."""

    result_info: Optional[ResultInfo] = None
