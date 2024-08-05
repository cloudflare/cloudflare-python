# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["MessagePullResponse", "MessagePullResponseItem"]


class MessagePullResponseItem(BaseModel):
    id: Optional[str] = None

    attempts: Optional[float] = None

    body: Optional[str] = None

    lease_id: Optional[str] = None

    metadata: Optional[object] = None

    timestamp_ms: Optional[float] = None


MessagePullResponse: TypeAlias = List[MessagePullResponseItem]
