# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ThreatEventCreateParams", "Search"]


class ThreatEventCreateParams(TypedDict, total=False):
    account_id: Required[float]
    """Account ID"""

    dataset_id: Annotated[List[str], PropertyInfo(alias="datasetId")]

    order: Literal["asc", "desc"]

    order_by: Annotated[str, PropertyInfo(alias="orderBy")]

    page: float

    page_size: Annotated[float, PropertyInfo(alias="pageSize")]

    search: Iterable[Search]


class Search(TypedDict, total=False):
    field: str

    op: str

    value: Union[str, float, List[Union[str, float]]]
