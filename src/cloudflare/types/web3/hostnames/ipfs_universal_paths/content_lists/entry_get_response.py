# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ......_models import BaseModel

__all__ = ["EntryGetResponse"]


class EntryGetResponse(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    content: Optional[str] = None
    """CID or content path of content to block."""

    created_on: Optional[datetime] = None

    description: Optional[str] = None
    """An optional description of the content list entry."""

    modified_on: Optional[datetime] = None

    type: Optional[Literal["cid", "content_path"]] = None
    """Type of content list entry to block."""
