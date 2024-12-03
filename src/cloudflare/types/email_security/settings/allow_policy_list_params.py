# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AllowPolicyListParams"]


class AllowPolicyListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    direction: Literal["asc", "desc"]
    """The sorting direction."""

    is_acceptable_sender: bool

    is_exempt_recipient: bool

    is_recipient: bool

    is_sender: bool

    is_spoof: bool

    is_trusted_sender: bool

    order: Literal["pattern", "created_at"]
    """The field to sort by."""

    page: int
    """The page number of paginated results."""

    pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]

    per_page: int
    """The number of results per page."""

    search: str
    """
    Allows searching in multiple properties of a record simultaneously. This
    parameter is intended for human users, not automation. Its exact behavior is
    intentionally left unspecified and is subject to change in the future.
    """

    verify_sender: bool
