# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["Message", "MessageItem", "MessageItemSource"]


class MessageItemSource(BaseModel):
    pointer: Optional[str] = None


class MessageItem(BaseModel):
    code: int

    message: str

    documentation_url: Optional[str] = None

    source: Optional[MessageItemSource] = None


Message: TypeAlias = List[MessageItem]
