# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ......_models import BaseModel
from .dweb_config_content_list_entry import DwebConfigContentListEntry

__all__ = ["EntryListResponse"]


class EntryListResponse(BaseModel):
    entries: Optional[List[DwebConfigContentListEntry]] = None
    """Content list entries."""
