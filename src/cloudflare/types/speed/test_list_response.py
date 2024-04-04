# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..shared import UnnamedSchemaRef3248f24329456e19dfa042fff9986f72
from ..._models import BaseModel

__all__ = ["TestListResponse", "ResultInfo"]


class ResultInfo(BaseModel):
    count: Optional[int] = None

    page: Optional[int] = None

    per_page: Optional[int] = None

    total_count: Optional[int] = None


class TestListResponse(BaseModel):
    __test__ = False
    errors: List[UnnamedSchemaRef3248f24329456e19dfa042fff9986f72]

    messages: List[UnnamedSchemaRef3248f24329456e19dfa042fff9986f72]

    success: bool
    """Whether the API call was successful."""

    result_info: Optional[ResultInfo] = None
