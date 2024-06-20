# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LogListParams"]


class LogListParams(TypedDict, total=False):
    account_id: Required[str]

    cached: bool

    direction: Literal["asc", "desc"]

    end_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    order_by: Literal["created_at", "provider"]

    page: int

    per_page: int

    search: str

    start_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    success: bool
