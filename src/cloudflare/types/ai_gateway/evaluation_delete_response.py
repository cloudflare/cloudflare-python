# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EvaluationDeleteResponse", "Dataset", "DatasetFilter", "Result"]


class DatasetFilter(BaseModel):
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


class Dataset(BaseModel):
    id: str

    account_id: str

    account_tag: str

    created_at: datetime

    enable: bool

    filters: List[DatasetFilter]

    gateway_id: str
    """gateway id"""

    modified_at: datetime

    name: str


class Result(BaseModel):
    id: str

    created_at: datetime

    evaluation_id: str

    evaluation_type_id: str

    modified_at: datetime

    result: str

    status: float

    status_description: str

    total_logs: float


class EvaluationDeleteResponse(BaseModel):
    id: str

    account_id: str

    account_tag: str

    created_at: datetime

    datasets: List[Dataset]

    gateway_id: str
    """gateway id"""

    modified_at: datetime

    name: str

    processed: bool

    results: List[Result]

    total_logs: float
