# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["LOADocumentCreateResponse"]


class LOADocumentCreateResponse(BaseModel):
    id: Optional[str] = None
    """Identifier for the uploaded LOA document."""

    account_id: Optional[str] = None
    """Identifier of a Cloudflare account."""

    created: Optional[datetime] = None

    filename: Optional[str] = None
    """Name of LOA document. Max file size 10MB, and supported filetype is pdf."""

    size_bytes: Optional[int] = None
    """File size of the uploaded LOA document."""

    verified: Optional[bool] = None
    """Whether the LOA has been verified by Cloudflare staff."""

    verified_at: Optional[datetime] = None
    """Timestamp of the moment the LOA was marked as validated."""
