# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["Submit"]


class Submit(BaseModel):
    excluded_urls: Optional[List[object]] = None
    """
    URLs that were excluded from scanning because their domain is in our no-scan
    list.
    """

    skipped_urls: Optional[List[object]] = None
    """URLs that were skipped because the same URL is currently being scanned"""

    submitted_urls: Optional[List[object]] = None
    """URLs that were successfully submitted for scanning."""
