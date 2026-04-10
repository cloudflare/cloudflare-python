# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["MatchGetParams"]


class MatchGetParams(TypedDict, total=False):
    account_id: Required[str]

    query_id: Required[SequenceNotStr[str]]
    """Query ID or comma-separated list of Query IDs.

    When multiple IDs are provided, matches are deduplicated across queries and each
    match includes matched_queries and match_ids arrays.
    """

    domain_search: str
    """Filter matches by domain name (substring match)"""

    include_dismissed: str

    include_domain_id: str

    limit: str

    offset: str

    order: Literal["asc", "desc"]
    """Sort order. Options: 'asc' (ascending) or 'desc' (descending)"""

    order_by: Annotated[Literal["domain", "first_seen", "registrar"], PropertyInfo(alias="orderBy")]
    """Column to sort by. Options: 'domain', 'first_seen', or 'registrar'"""
