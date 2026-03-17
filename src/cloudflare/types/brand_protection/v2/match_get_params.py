# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["MatchGetParams"]


class MatchGetParams(TypedDict, total=False):
    account_id: Required[str]

    query_id: Required[str]

    include_dismissed: str

    include_domain_id: str

    limit: str

    offset: str

    order: Literal["asc", "desc"]
    """Sort order. Options: 'asc' (ascending) or 'desc' (descending)"""

    order_by: Annotated[Literal["domain", "first_seen"], PropertyInfo(alias="orderBy")]
    """Column to sort by. Options: 'domain' or 'first_seen'"""
