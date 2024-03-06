# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["SnippetListResponse", "SnippetListResponseItem"]


class SnippetListResponseItem(BaseModel):
    created_on: Optional[str] = None
    """Creation time of the snippet"""

    modified_on: Optional[str] = None
    """Modification time of the snippet"""

    snippet_name: Optional[str] = None
    """Snippet identifying name"""


SnippetListResponse = List[SnippetListResponseItem]
