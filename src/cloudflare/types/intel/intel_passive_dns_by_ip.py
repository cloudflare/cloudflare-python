# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..shared import UnnamedSchemaRef35
from ..._models import BaseModel

__all__ = ["IntelPassiveDNSByIP"]


class IntelPassiveDNSByIP(BaseModel):
    count: Optional[float] = None
    """Total results returned based on your search parameters."""

    page: Optional[float] = None
    """Current page within paginated list of results."""

    per_page: Optional[float] = None
    """Number of results per page of results."""

    reverse_records: Optional[List[UnnamedSchemaRef35]] = None
    """Reverse DNS look-ups observed during the time period."""
