# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel
from .available_dataset import AvailableDataset
from ....shared.response_info import ResponseInfo

__all__ = ["AvailableList"]


class AvailableList(BaseModel):
    errors: List[ResponseInfo]

    messages: List[str]

    success: bool

    result: Optional[List[AvailableDataset]] = None
