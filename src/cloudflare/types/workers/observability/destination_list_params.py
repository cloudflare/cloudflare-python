# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DestinationListParams"]


class DestinationListParams(TypedDict, total=False):
    account_id: str

    order: Literal["asc", "desc"]

    order_by: Annotated[Literal["created", "updated"], PropertyInfo(alias="orderBy")]

    page: float

    per_page: Annotated[float, PropertyInfo(alias="perPage")]
