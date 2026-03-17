# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["LogoMatchGetResponse", "Match"]


class Match(BaseModel):
    id: int

    matched_at: Optional[str] = None

    query_id: int

    similarity_score: float

    url_scan_id: Optional[str] = None

    content_type: Optional[str] = None

    domain: Optional[str] = None

    image_data: Optional[str] = None


class LogoMatchGetResponse(BaseModel):
    matches: List[Match]

    total: int
