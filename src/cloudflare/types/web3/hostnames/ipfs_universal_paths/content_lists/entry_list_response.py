# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ......_models import BaseModel

__all__ = ["EntryListResponse", "Entry"]


class Entry(BaseModel):
    id: Optional[str] = None
    """Specify the identifier of the hostname."""

    content: Optional[str] = None
    """Specify the CID or content path of content to block."""

    created_on: Optional[datetime] = None

    description: Optional[str] = None
    """Specify an optional description of the content list entry."""

    modified_on: Optional[datetime] = None

    type: Optional[Literal["cid", "content_path"]] = None
    """Specify the type of content list entry to block."""


class EntryListResponse(BaseModel):
    entries: Optional[List[Entry]] = None
    """Provides content list entries."""
