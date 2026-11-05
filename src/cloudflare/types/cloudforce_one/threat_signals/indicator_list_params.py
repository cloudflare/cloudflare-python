# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IndicatorListParams"]


class IndicatorListParams(TypedDict, total=False):
    account_id: Required[str]

    article_id: str
    """Article UUID filter. Omit to include indicators from every article."""

    cursor: str
    """Opaque cursor from the previous response's `pagination.cursor`.

    When provided, page size, ordering, and filters come from the cursor. Sending
    `per_page`, `sort`, `include_total`, `feed_id`, `article_id`, or `search`
    alongside it returns a 400 `CursorFilterConflictError`.
    """

    feed_id: str
    """Feed UUID filter. Omit to include indicators from every account feed."""

    include_total: bool
    """When true on the first page, count matching indicators and return an exact
    total.

    Defaults to false; cursor pages do not recalculate totals.
    """

    per_page: int
    """Number of indicators per cursor page, from 1 to 100. Defaults to 20."""

    search: str
    """
    NFC-normalized and trimmed, case-insensitive literal substring search of
    indicator values. Requires 3–500 Unicode code points; the upper code-point bound
    is described here because OpenAPI string length cannot precisely express it
    without imposing UTF-16 semantics.
    """

    sort: str
    """Sort by id. Use id for ascending or -id for descending order; defaults to id."""
