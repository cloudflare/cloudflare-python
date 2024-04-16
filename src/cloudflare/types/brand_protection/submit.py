# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["Submit", "ExcludedURL", "SkippedURL", "SubmittedURL"]


class ExcludedURL(BaseModel):
    url: Optional[str] = None
    """URL that was excluded."""


class SkippedURL(BaseModel):
    url: Optional[str] = None
    """URL that was skipped."""

    url_id: Optional[int] = None
    """ID of the submission of that URL that is currently scanning."""


class SubmittedURL(BaseModel):
    url: Optional[str] = None
    """URL that was submitted."""

    url_id: Optional[int] = None
    """ID assigned to this URL submission. Used to retrieve scanning results."""


class Submit(BaseModel):
    excluded_urls: Optional[List[ExcludedURL]] = None
    """
    URLs that were excluded from scanning because their domain is in our no-scan
    list.
    """

    skipped_urls: Optional[List[SkippedURL]] = None
    """URLs that were skipped because the same URL is currently being scanned"""

    submitted_urls: Optional[List[SubmittedURL]] = None
    """URLs that were successfully submitted for scanning."""
