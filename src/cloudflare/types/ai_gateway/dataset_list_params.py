# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DatasetListParams", "Filter"]


class DatasetListParams(TypedDict, total=False):
    account_id: Required[str]

    id: str

    enable: bool

    filters: Iterable[Filter]

    name: str

    order_by: str
    """Order By Column Name"""

    order_by_direction: Literal["asc", "desc"]
    """Order By Direction"""

    page: int

    per_page: int

    search: str
    """Search by id, name, filters"""


class Filter(TypedDict, total=False):
    key: Required[
        Literal[
            "created_at",
            "request_content_type",
            "response_content_type",
            "success",
            "cached",
            "provider",
            "model",
            "cost",
            "tokens",
            "tokens_in",
            "tokens_out",
            "duration",
            "feedback",
        ]
    ]

    operator: Required[Literal["eq", "contains", "lt", "gt"]]

    value: Required[List[Union[str, float, bool]]]
