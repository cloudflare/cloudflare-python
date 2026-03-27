# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["MatchGetResponse", "Match", "MatchPublicScans"]


class MatchPublicScans(BaseModel):
    submission_id: str


class Match(BaseModel):
    dismissed: bool

    domain: str

    first_seen: str

    public_scans: Optional[MatchPublicScans] = None

    scan_status: str

    scan_submission_id: Optional[int] = None

    source: Optional[str] = None

    match_ids: Optional[List[int]] = None
    """All underlying match row IDs for this domain.

    Only present when multiple query_ids are requested.
    """

    matched_queries: Optional[List[int]] = None
    """List of query IDs that produced this match.

    Only present when multiple query_ids are requested.
    """


class MatchGetResponse(BaseModel):
    matches: List[Match]

    total: int
