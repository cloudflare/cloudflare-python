# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DatasetDeleteResponse", "Filter"]


class Filter(BaseModel):
    key: Literal[
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

    operator: Literal["eq", "contains", "lt", "gt"]

    value: List[Union[str, float, bool]]


class DatasetDeleteResponse(BaseModel):
    id: str

    account_id: str

    account_tag: str

    created_at: datetime

    enable: bool

    filters: List[Filter]

    gateway_id: str
    """gateway id"""

    modified_at: datetime

    name: str
