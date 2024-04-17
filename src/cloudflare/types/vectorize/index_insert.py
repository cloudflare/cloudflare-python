# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["IndexInsert"]


class IndexInsert(BaseModel):
    count: Optional[int] = None
    """Specifies the count of the vectors successfully inserted."""

    ids: Optional[List[str]] = None
    """Array of vector identifiers of the vectors successfully inserted."""
