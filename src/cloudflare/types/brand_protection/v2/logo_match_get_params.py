# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["LogoMatchGetParams"]


class LogoMatchGetParams(TypedDict, total=False):
    account_id: Required[str]

    query_id: Required[str]

    download: str

    limit: str

    offset: str

    order: Literal["asc", "desc"]
    """Sort order. Options: 'asc' (ascending) or 'desc' (descending)"""

    order_by: Annotated[Literal["matchedAt", "domain", "similarityScore"], PropertyInfo(alias="orderBy")]
    """Column to sort by. Options: 'matchedAt', 'domain', or 'similarityScore'"""
