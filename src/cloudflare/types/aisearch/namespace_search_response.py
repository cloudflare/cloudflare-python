# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["NamespaceSearchResponse", "Chunk", "ChunkItem", "ChunkScoringDetails", "Error"]


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

    instance_id: str

    score: float

    text: str

    type: str

    item: Optional[ChunkItem] = None

    scoring_details: Optional[ChunkScoringDetails] = None


class Error(BaseModel):
    instance_id: str

    message: str


class NamespaceSearchResponse(BaseModel):
    chunks: List[Chunk]

    search_query: str

    errors: Optional[List[Error]] = None
