# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ......_models import BaseModel
from .content_list_item import ContentListItem

__all__ = ["EntryListResponse"]


class EntryListResponse(BaseModel):
    entries: Optional[List[ContentListItem]] = None
    """Content list entries."""
