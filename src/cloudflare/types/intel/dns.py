# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .unnamed_schema_ref_b5e16cee4f32382c294201aedb9fc050 import UnnamedSchemaRefB5e16cee4f32382c294201aedb9fc050

__all__ = ["DNS"]


class DNS(BaseModel):
    count: Optional[float] = None
    """Total results returned based on your search parameters."""

    page: Optional[float] = None
    """Current page within paginated list of results."""

    per_page: Optional[float] = None
    """Number of results per page of results."""

    reverse_records: Optional[List[UnnamedSchemaRefB5e16cee4f32382c294201aedb9fc050]] = None
    """Reverse DNS look-ups observed during the time period."""
