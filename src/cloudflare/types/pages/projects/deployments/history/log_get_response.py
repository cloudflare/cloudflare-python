# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ......_models import BaseModel

__all__ = ["LogGetResponse", "Data"]


class Data(BaseModel):
    line: str

    ts: str


class LogGetResponse(BaseModel):
    data: List[Data]

    includes_container_logs: bool

    total: int
