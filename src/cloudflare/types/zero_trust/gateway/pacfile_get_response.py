# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["PacfileGetResponse"]


class PacfileGetResponse(BaseModel):
    id: Optional[str] = None

    contents: Optional[str] = None
    """Actual contents of the PAC file"""

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """Detailed description of the PAC file."""

    name: Optional[str] = None
    """Name of the PAC file."""

    slug: Optional[str] = None
    """URL-friendly version of the PAC file name."""

    updated_at: Optional[datetime] = None

    url: Optional[str] = None
    """Unique URL to download the PAC file."""
