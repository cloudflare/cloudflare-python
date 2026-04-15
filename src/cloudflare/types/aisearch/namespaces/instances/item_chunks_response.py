# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import TypeAlias

from ....._models import BaseModel

__all__ = ["ItemChunksResponse", "ItemChunksResponseItem", "ItemChunksResponseItemItem"]


class ItemChunksResponseItemItem(BaseModel):
    key: str

    metadata: Optional[Dict[str, object]] = None

    timestamp: Optional[float] = None


class ItemChunksResponseItem(BaseModel):
    id: str

    item: ItemChunksResponseItemItem

    text: str

    end_byte: Optional[float] = None

    start_byte: Optional[float] = None


ItemChunksResponse: TypeAlias = List[ItemChunksResponseItem]
