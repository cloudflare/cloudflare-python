# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LogListParams", "Filter"]


class LogListParams(TypedDict, total=False):
    account_id: Required[str]

    cached: bool

    direction: Literal["asc", "desc"]

    end_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    feedback: Literal[0, 1]

    filters: Iterable[Filter]

    max_cost: float

    max_duration: float

    max_tokens_in: float

    max_tokens_out: float

    max_total_tokens: float

    meta_info: bool

    min_cost: float

    min_duration: float

    min_tokens_in: float

    min_tokens_out: float

    min_total_tokens: float

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


class Filter(TypedDict, total=False):
    key: Required[
        Literal[
            "id",
            "created_at",
            "request_content_type",
            "response_content_type",
            "success",
            "cached",
            "provider",
            "model",
            "model_type",
            "cost",
            "tokens",
            "tokens_in",
            "tokens_out",
            "duration",
            "feedback",
            "event_id",
            "request_type",
            "metadata.key",
            "metadata.value",
            "prompts.prompt_id",
            "prompts.version_id",
        ]
    ]

    operator: Required[Literal["eq", "neq", "contains", "lt", "gt"]]

    value: Required[List[Union[Optional[str], float, bool]]]
