# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["Message", "MessageItem"]


class MessageItem(BaseModel):
    code: int

    message: str


Message: TypeAlias = List[MessageItem]
