# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TokenListParams"]


class TokenListParams(TypedDict, total=False):
    account_id: Required[str]

    order_by: Literal["created_at"]
    """Order By Column Name"""

    order_by_direction: Literal["asc", "desc"]
    """Order By Direction"""

    page: int

    per_page: int
