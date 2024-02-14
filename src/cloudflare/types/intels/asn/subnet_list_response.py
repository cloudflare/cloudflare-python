# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["SubnetListResponse"]


class SubnetListResponse(BaseModel):
    asn: Optional[int] = None

    count: Optional[float] = None
    """Total results returned based on your search parameters."""

    ip_count_total: Optional[int] = None

    page: Optional[float] = None
    """Current page within paginated list of results."""

    per_page: Optional[float] = None
    """Number of results per page of results."""

    subnets: Optional[List[str]] = None
