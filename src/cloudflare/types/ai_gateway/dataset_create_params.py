# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DatasetCreateParams", "Filter"]


class DatasetCreateParams(TypedDict, total=False):
    account_id: Required[str]

    enable: Required[bool]

    filters: Required[Iterable[Filter]]

    name: Required[str]


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
