# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TrustedDomainListParams"]


class TrustedDomainListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    direction: Literal["asc", "desc"]
    """The sorting direction."""

    is_recent: bool
    """
    Filter to show only recently registered domains that are trusted to prevent
    triggering Suspicious or Malicious dispositions.
    """

    is_similarity: bool
    """
    Filter to show only proximity domains (partner or approved domains with similar
    spelling to connected domains) that prevent Spoof dispositions.
    """

    order: Literal["pattern", "created_at"]
    """Field to sort by."""

    page: int
    """Current page within paginated list of results."""

    pattern: str

    per_page: int
    """The number of results per page. Maximum value is 1000."""

    search: str
    """Search term for filtering records. Behavior may change."""
