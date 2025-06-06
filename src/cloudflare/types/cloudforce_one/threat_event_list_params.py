# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ThreatEventListParams", "Search"]


class ThreatEventListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    dataset_id: Annotated[List[str], PropertyInfo(alias="datasetId")]

    force_refresh: Annotated[bool, PropertyInfo(alias="forceRefresh")]

    order: Literal["asc", "desc"]

    order_by: Annotated[str, PropertyInfo(alias="orderBy")]

    page: float

    page_size: Annotated[float, PropertyInfo(alias="pageSize")]

    search: Iterable[Search]


class Search(TypedDict, total=False):
    field: str

    op: Literal["equals", "not", "gt", "gte", "lt", "lte", "like", "contains", "startsWith", "endsWith", "in", "find"]

    value: Union[str, float, List[Union[str, float]]]
