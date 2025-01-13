# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ViewListParams", "Name"]


class ViewListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    direction: Literal["asc", "desc"]
    """Direction to order DNS views in."""

    match: Literal["any", "all"]
    """Whether to match all search requirements or at least one (any).

    If set to `all`, acts like a logical AND between filters. If set to `any`, acts
    like a logical OR instead.
    """

    name: Name

    order: Literal["name", "created_on", "modified_on"]
    """Field to order DNS views by."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of DNS views per page."""

    zone_id: str
    """A zone ID that exists in the zones list for the view."""

    zone_name: str
    """A zone name that exists in the zones list for the view."""


class Name(TypedDict, total=False):
    contains: str
    """Substring of the DNS view name."""

    endswith: str
    """Suffix of the DNS view name."""

    exact: str
    """Exact value of the DNS view name."""

    startswith: str
    """Prefix of the DNS view name."""
