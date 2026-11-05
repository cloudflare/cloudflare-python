# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["StreamListParams"]


class StreamListParams(TypedDict, total=False):
    account_id: Required[str]
    """Specifies the public ID of the account."""

    name: str
    """Filters K2 streams by name using a case-insensitive substring."""

    page: int

    per_page: int
