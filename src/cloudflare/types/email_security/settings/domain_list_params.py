# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DomainListParams"]


class DomainListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    active_delivery_mode: Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"]
    """Filters response to domains with the currently active delivery mode."""

    allowed_delivery_mode: Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"]
    """Filters response to domains with the provided delivery mode."""

    direction: Literal["asc", "desc"]
    """The sorting direction."""

    domain: List[str]
    """Filters results by the provided domains, allowing for multiple occurrences."""

    order: Literal["domain", "created_at"]
    """The field to sort by."""

    page: int
    """The page number of paginated results."""

    per_page: int
    """The number of results per page."""

    search: str
    """
    Allows searching in multiple properties of a record simultaneously. This
    parameter is intended for human users, not automation. Its exact behavior is
    intentionally left unspecified and is subject to change in the future.
    """
