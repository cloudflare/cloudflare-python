# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Snippet"]


class Snippet(BaseModel):
    created_on: Optional[str] = None
    """Creation time of the snippet"""

    modified_on: Optional[str] = None
    """Modification time of the snippet"""

    snippet_name: Optional[str] = None
    """Snippet identifying name"""
