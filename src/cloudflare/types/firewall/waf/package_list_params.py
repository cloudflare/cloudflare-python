# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PackageListParams"]


class PackageListParams(TypedDict, total=False):
    direction: Literal["asc", "desc"]
    """The direction used to sort returned packages."""

    match: Literal["any", "all"]
    """When set to `all`, all the search requirements must match.

    When set to `any`, only one of the search requirements has to match.
    """

    order: Literal["name"]
    """The field used to sort returned packages."""

    page: float
    """The page number of paginated results."""

    per_page: float
    """The number of packages per page."""
