# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["LogoMatchGetResponse", "Match"]


class Match(BaseModel):
    id: int

    domain: Optional[str] = None

    matched_at: Optional[str] = None

    query_id: int

    registrar: Optional[str] = None

    similarity_score: float

    url_scan_id: Optional[str] = None

    content_type: Optional[str] = None

    image_data: Optional[str] = None


class LogoMatchGetResponse(BaseModel):
    matches: List[Match]

    total: int
