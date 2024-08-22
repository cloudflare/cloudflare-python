# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DomainListParams"]


class DomainListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    allowed_delivery_mode: Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"]
    """If present, the response contains only domains with the provided delivery mode."""

    direction: Literal["asc", "desc"]
    """The sorting direction."""

    domain: List[str]
    """
    Filter result by the provided domains. Allows for multiple occurrences, e.g.,
    `domain=example.com&domain=example.xyz`.
    """

    order: Literal["domain", "created_at"]
    """The field to sort by."""

    page: int
    """Page number of paginated results."""

    per_page: int
    """Number of results to display."""

    search: str
    """
    Allows searching in multiple properties of a record simultaneously. This
    parameter is intended for human users, not automation. Its exact behavior is
    intentionally left unspecified and is subject to change in the future.
    """
