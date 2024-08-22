# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing_extensions import TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["MessagePullResponse", "MessagePullResponseItem"]

class MessagePullResponseItem(BaseModel):
    id: Optional[str] = None

    attempts: Optional[float] = None

    body: Optional[str] = None

    lease_id: Optional[str] = None

    metadata: Optional[object] = None

    timestamp_ms: Optional[float] = None

MessagePullResponse: TypeAlias = List[MessagePullResponseItem]