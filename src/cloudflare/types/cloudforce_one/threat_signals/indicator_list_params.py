# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IndicatorListParams"]


class IndicatorListParams(TypedDict, total=False):
    account_id: Required[str]

    article_id: str

    cursor: str

    feed_id: str

    include_total: bool

    per_page: int

    search: str
    """
    NFC-normalized and trimmed, case-insensitive literal substring search of
    indicator values. Requires 3–500 Unicode code points; the upper code-point bound
    is described here because OpenAPI string length cannot precisely express it
    without imposing UTF-16 semantics.
    """

    sort: str
