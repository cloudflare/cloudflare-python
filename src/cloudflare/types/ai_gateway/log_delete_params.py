# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["LogDeleteParams", "Filter"]


class LogDeleteParams(TypedDict, total=False):
    account_id: Required[str]

    filters: Iterable[Filter]

    limit: int

    order_by: Literal[
        "created_at",
        "provider",
        "model",
        "model_type",
        "success",
        "cached",
        "cost",
        "tokens_in",
        "tokens_out",
        "duration",
        "feedback",
    ]

    order_by_direction: Literal["asc", "desc"]


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
