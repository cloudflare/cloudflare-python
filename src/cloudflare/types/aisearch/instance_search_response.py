# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["InstanceSearchResponse", "Chunk", "ChunkItem", "ChunkScoringDetails"]


class ChunkItem(BaseModel):
    key: str

    metadata: Optional[Dict[str, object]] = None

    timestamp: Optional[float] = None


class ChunkScoringDetails(BaseModel):
    keyword_rank: Optional[float] = None

    keyword_score: Optional[float] = None

    vector_rank: Optional[float] = None

    vector_score: Optional[float] = None


class Chunk(BaseModel):
    id: str

    score: float

    text: str

    type: str

    item: Optional[ChunkItem] = None

    scoring_details: Optional[ChunkScoringDetails] = None


class InstanceSearchResponse(BaseModel):
    chunks: List[Chunk]

    search_query: str
