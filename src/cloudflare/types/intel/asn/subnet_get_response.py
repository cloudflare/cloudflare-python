# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ...shared.asn import ASN

__all__ = ["SubnetGetResponse"]


class SubnetGetResponse(BaseModel):
    asn: Optional[ASN] = None

    count: Optional[float] = None
    """Total results returned based on your search parameters."""

    ip_count_total: Optional[int] = None

    page: Optional[float] = None
    """Current page within paginated list of results."""

    per_page: Optional[float] = None
    """Number of results per page of results."""

    subnets: Optional[List[str]] = None
