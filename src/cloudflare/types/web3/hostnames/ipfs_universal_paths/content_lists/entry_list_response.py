# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ......_models import BaseModel
from .distributed_web_config_content_list_entry import DistributedWebConfigContentListEntry

__all__ = ["EntryListResponse"]


class EntryListResponse(BaseModel):
    entries: Optional[List[DistributedWebConfigContentListEntry]] = None
    """Content list entries."""
