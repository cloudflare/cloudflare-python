# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ZoneListParams", "Account"]


class ZoneListParams(TypedDict, total=False):
    account: Account

    direction: Literal["asc", "desc"]
    """Direction to order zones."""

    match: Literal["any", "all"]
    """Whether to match all search requirements or at least one (any)."""

    name: str
    """A domain name.

    Optional filter operators can be provided to extend refine the search:

    - `equal` (default)
    - `not_equal`
    - `starts_with`
    - `ends_with`
    - `contains`
    - `starts_with_case_sensitive`
    - `ends_with_case_sensitive`
    - `contains_case_sensitive`
    """

    order: Literal["name", "status", "account.id", "account.name"]
    """Field to order zones by."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of zones per page."""

    status: Literal["initializing", "pending", "active", "moved"]
    """A zone status"""


class Account(TypedDict, total=False):
    id: str
    """An account ID"""

    name: str
    """An account Name.

    Optional filter operators can be provided to extend refine the search:

    - `equal` (default)
    - `not_equal`
    - `starts_with`
    - `ends_with`
    - `contains`
    - `starts_with_case_sensitive`
    - `ends_with_case_sensitive`
    - `contains_case_sensitive`
    """
