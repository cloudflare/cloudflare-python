# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["MessageAckResponse"]


class MessageAckResponse(BaseModel):
    ack_count: Optional[float] = FieldInfo(alias="ackCount", default=None)
    """The number of messages that were succesfully acknowledged."""

    retry_count: Optional[float] = FieldInfo(alias="retryCount", default=None)
    """The number of messages that were succesfully retried."""

    warnings: Optional[List[str]] = None
