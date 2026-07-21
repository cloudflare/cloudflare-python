# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["QueryGetParams"]


class QueryGetParams(TypedDict, total=False):
    account_id: Required[str]

    id: str

    page: int
    """Optional page number for paginated list requests.

    Defaults to 1 when only per_page is supplied. Omit page and per_page to preserve
    the legacy full-list response.
    """

    per_page: int
    """Optional number of queries per page for paginated list requests.

    Defaults to 100 when only page is supplied. Maximum 100. Omit page and per_page
    to preserve the legacy full-list response.
    """
