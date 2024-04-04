# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["VersionListResponse", "Item"]


class Item(BaseModel):
    id: Optional[str] = None

    metadata: Optional[object] = None

    number: Optional[float] = None


class VersionListResponse(BaseModel):
    items: Optional[List[Item]] = None
