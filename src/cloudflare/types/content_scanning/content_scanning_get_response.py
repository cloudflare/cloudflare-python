# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ContentScanningGetResponse"]


class ContentScanningGetResponse(BaseModel):
    """Defines the status for Content Scanning."""

    modified: Optional[str] = None
    """Defines the last modification date (ISO 8601) of the Content Scanning status."""

    value: Optional[str] = None
    """Defines the status of Content Scanning."""
