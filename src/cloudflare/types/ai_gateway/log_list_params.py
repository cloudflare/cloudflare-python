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

    end_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    max_cost: float

    max_duration: float

    max_tokens: float

    min_cost: float

    min_duration: float

    min_tokens: float

    model: str

    model_type: str

    order_by: Literal["created_at", "provider", "model", "model_type", "success", "cached"]

    order_by_direction: Literal["asc", "desc"]

    page: int

    per_page: int

    provider: str

    request_content_type: str

    response_content_type: str

    search: str

    start_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    success: bool
