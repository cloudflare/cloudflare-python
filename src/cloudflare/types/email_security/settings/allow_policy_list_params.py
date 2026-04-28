# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AllowPolicyListParams"]


class AllowPolicyListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    direction: Literal["asc", "desc"]
    """The sorting direction."""

    is_acceptable_sender: bool
    """
    Filter to show only policies where messages from the sender are exempted from
    Spam, Spoof, and Bulk dispositions (not Malicious or Suspicious).
    """

    is_exempt_recipient: bool
    """
    Filter to show only policies where messages to the recipient bypass all
    detections.
    """

    is_trusted_sender: bool
    """
    Filter to show only policies where messages from the sender bypass all
    detections and link following.
    """

    order: Literal["pattern", "created_at"]
    """Field to sort by."""

    page: int
    """Current page within paginated list of results."""

    pattern: str

    pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]
    """
    Type of pattern matching. Note: UNKNOWN is deprecated and cannot be used when
    creating or updating policies, but may be returned for existing entries.
    """

    per_page: int
    """The number of results per page. Maximum value is 1000."""

    search: str
    """Search term for filtering records. Behavior may change."""

    verify_sender: bool
    """Filter to show only policies that enforce DMARC, SPF, or DKIM authentication."""
