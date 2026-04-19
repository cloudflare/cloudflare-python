# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["JobLogsResponse", "JobLogsResponseItem"]


class JobLogsResponseItem(BaseModel):
    id: int

    created_at: float

    message: str

    message_type: int


JobLogsResponse: TypeAlias = List[JobLogsResponseItem]
