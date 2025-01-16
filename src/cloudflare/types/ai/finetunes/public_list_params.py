# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PublicListParams"]


class PublicListParams(TypedDict, total=False):
    account_id: Required[str]

    limit: float
    """Pagination Limit"""

    offset: float
    """Pagination Offset"""

    order_by: Annotated[str, PropertyInfo(alias="orderBy")]
    """Order By Column Name"""
