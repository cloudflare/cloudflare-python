# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["NamespaceBulkDeleteResponse"]


class NamespaceBulkDeleteResponse(BaseModel):
    successful_key_count: Optional[float] = None
    """Number of keys successfully updated"""

    unsuccessful_keys: Optional[List[str]] = None
    """Name of the keys that failed to be fully updated. They should be retried."""
