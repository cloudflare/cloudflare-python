# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["MoveCreateResponse", "MoveCreateResponseItem"]


class MoveCreateResponseItem(BaseModel):
    completed_timestamp: datetime

    destination: str

    item_count: int

    message_id: str

    operation: str

    recipient: str

    status: str


MoveCreateResponse: TypeAlias = List[MoveCreateResponseItem]
