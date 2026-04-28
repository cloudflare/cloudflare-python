# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["ReleaseBulkResponse"]


class ReleaseBulkResponse(BaseModel):
    id: str
    """Unique identifier for a message retrieved from investigation"""

    delivered: Optional[List[str]] = None

    failed: Optional[List[str]] = None

    postfix_id: Optional[str] = None
    """Deprecated, use `id` instead. End of life: November 1, 2026."""

    undelivered: Optional[List[str]] = None
