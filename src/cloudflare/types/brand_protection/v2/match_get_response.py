# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["MatchGetResponse", "Match", "MatchPublicScans", "MatchMatchDetail"]


class MatchPublicScans(BaseModel):
    submission_id: str


class MatchMatchDetail(BaseModel):
    dismissed: bool
    """Individual dismissed state for this specific match."""

    match_id: int

    query_id: int

    query_tag: Optional[str] = None
    """Tag associated with the query, if one exists."""


class Match(BaseModel):
    domain: str

    first_seen: str

    public_scans: Optional[MatchPublicScans] = None

    registrar: Optional[str] = None

    scan_status: str

    scan_submission_id: Optional[int] = None

    source: Optional[str] = None

    dismissed: Optional[bool] = None
    """Whether the match is dismissed.

    Only present for single-query requests. For multi-query requests, use the
    dismissed field in each match_details entry.
    """

    match_details: Optional[List[MatchMatchDetail]] = None
    """Per-match detail objects with query metadata and individual dismissed state.

    Only present when multiple query_ids are requested.
    """


class MatchGetResponse(BaseModel):
    matches: List[Match]

    total: int
