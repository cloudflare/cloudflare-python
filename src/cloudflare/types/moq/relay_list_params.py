# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RelayListParams"]


class RelayListParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account identifier."""

    asc: bool
    """Sort order by `created`.

    When true, results are returned oldest-first (ascending); otherwise newest-first
    (descending, the default).
    """

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Cursor for pagination.

    Returns relays created strictly after this RFC 3339 timestamp (typically the
    `created` value of the last item on the current page, to fetch the next page).
    """

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Cursor for pagination.

    Returns relays created strictly before this RFC 3339 timestamp (typically the
    `created` value of the first item on the current page, to fetch the previous
    page).
    """

    per_page: int
    """Maximum number of relays to return per page."""
