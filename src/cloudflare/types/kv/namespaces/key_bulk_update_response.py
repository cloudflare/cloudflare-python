# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["KeyBulkUpdateResponse"]


class KeyBulkUpdateResponse(BaseModel):
    successful_key_count: Optional[float] = None
    """Number of keys successfully written or deleted by the bulk operation."""

    unsuccessful_keys: Optional[List[str]] = None
    """Names of keys that failed to be written or deleted.

    Retry the operation for these keys.
    """
