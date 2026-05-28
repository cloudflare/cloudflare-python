# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PrefixBindingListParams"]


class PrefixBindingListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier of a Cloudflare account."""

    cursor: str
    """Opaque token for cursor-based pagination.

    Omit for the first page. Pass the value from a previous response to fetch the
    next page.
    """

    per_page: int
