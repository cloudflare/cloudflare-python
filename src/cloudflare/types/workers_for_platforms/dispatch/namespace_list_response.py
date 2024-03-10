# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["NamespaceListResponse", "NamespaceListResponseItem"]


class NamespaceListResponseItem(BaseModel):
    created_by: Optional[str] = None
    """Identifier"""

    created_on: Optional[datetime] = None
    """When the script was created."""

    modified_by: Optional[str] = None
    """Identifier"""

    modified_on: Optional[datetime] = None
    """When the script was last modified."""

    namespace_id: Optional[str] = None
    """API Resource UUID tag."""

    namespace_name: Optional[str] = None
    """Name of the Workers for Platforms dispatch namespace."""


NamespaceListResponse = List[NamespaceListResponseItem]
