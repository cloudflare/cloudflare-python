# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ItemListParams"]


class ItemListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    cursor: str
    """The pagination cursor.

    An opaque string token indicating the position from which to continue when
    requesting the next/previous set of records. Cursor values are provided under
    `result_info.cursors` in the response. You should make no assumptions about a
    cursor's content or length.
    """

    per_page: int
    """Amount of results to include in each paginated response.

    A non-negative 32 bit integer.
    """

    search: str
    """A search query to filter returned items.

    Its meaning depends on the list type: IP addresses must start with the provided
    string, hostnames and bulk redirects must contain the string, and ASNs must
    match the string exactly.
    """
