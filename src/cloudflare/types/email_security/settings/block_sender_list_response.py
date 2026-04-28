# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["BlockSenderListResponse"]


class BlockSenderListResponse(BaseModel):
    """A blocked sender pattern"""

    id: Optional[str] = None
    """Blocked sender pattern identifier"""

    comments: Optional[str] = None

    created_at: Optional[datetime] = None

    is_regex: Optional[bool] = None

    last_modified: Optional[datetime] = None
    """Deprecated, use `modified_at` instead. End of life: November 1, 2026."""

    modified_at: Optional[datetime] = None

    pattern: Optional[str] = None

    pattern_type: Optional[Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]] = None
    """
    Type of pattern matching. Note: UNKNOWN is deprecated and cannot be used when
    creating or updating policies, but may be returned for existing entries.
    """
