# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["InstanceSearchResponse", "Chunk", "ChunkItem", "ChunkScoringDetails"]


class ChunkItem(BaseModel):
    key: str

    metadata: Optional[Dict[str, object]] = None

    timestamp: Optional[float] = None


class ChunkScoringDetails(BaseModel):
    fusion_method: Optional[Literal["rrf", "max"]] = None

    keyword_rank: Optional[float] = None

    keyword_score: Optional[float] = None

    reranking_score: Optional[float] = None

    vector_rank: Optional[float] = None

    vector_score: Optional[float] = None


class Chunk(BaseModel):
    id: str

    score: float

    text: str

    type: str

    item: Optional[ChunkItem] = None

    media_end_ms: Optional[int] = None
    """
    Audio/video transcript chunks only: end, in milliseconds from the start of the
    media (whole seconds), of the last transcript section the matched chunk covers.
    Describes the matched chunk before any context expansion, not the expanded
    `text`.
    """

    media_start_ms: Optional[int] = None
    """
    Audio/video transcript chunks only: start, in milliseconds from the start of the
    media (whole seconds), of the transcript section the matched chunk begins in.
    Describes the matched chunk before any context expansion, not the expanded
    `text`.
    """

    scoring_details: Optional[ChunkScoringDetails] = None

    source_media_type: Optional[Literal["audio", "video"]] = None
    """Audio/video transcript chunks only: type of the source media file.

    Omitted for all other chunks.
    """


class InstanceSearchResponse(BaseModel):
    chunks: List[Chunk]

    query_kind: Literal["text", "image", "multimodal"]

    search_query: Optional[str] = None
