# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal, TypeAlias

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

    media_end_ms: Optional[int] = None
    """
    Audio/video transcript chunks only: end, in milliseconds from the start of the
    media (whole seconds), of the last transcript section the chunk covers.
    """

    media_start_ms: Optional[int] = None
    """
    Audio/video transcript chunks only: start, in milliseconds from the start of the
    media (whole seconds), of the transcript section the chunk begins in.
    """

    source_media_type: Optional[Literal["audio", "video"]] = None
    """Audio/video transcript chunks only: type of the source media file.

    Omitted for all other chunks.
    """

    start_byte: Optional[float] = None


ItemChunksResponse: TypeAlias = List[ItemChunksResponseItem]
