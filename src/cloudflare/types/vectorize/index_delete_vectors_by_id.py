# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["IndexDeleteVectorsByID"]


class IndexDeleteVectorsByID(BaseModel):
    count: Optional[int] = None
    """The count of the vectors successfully deleted."""

    ids: Optional[List[str]] = None
    """
    Array of vector identifiers of the vectors that were successfully processed for
    deletion.
    """
