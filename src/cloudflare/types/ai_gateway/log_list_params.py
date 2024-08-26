# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal, Annotated

from typing import Union

from datetime import datetime

from ..._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["LogListParams"]

class LogListParams(TypedDict, total=False):
    account_id: Required[str]

    cached: bool

    direction: Literal["asc", "desc"]

    end_date: Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]

    order_by: Literal["created_at", "provider"]

    page: int

    per_page: int

    search: str

    start_date: Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]

    success: bool