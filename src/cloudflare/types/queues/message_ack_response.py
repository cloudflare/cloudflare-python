# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MessageAckResponse"]


class MessageAckResponse(BaseModel):
    ack_count: Optional[float] = FieldInfo(alias="ackCount", default=None)
    """The number of messages that were succesfully acknowledged."""

    retry_count: Optional[float] = FieldInfo(alias="retryCount", default=None)
    """The number of messages that were succesfully retried."""

    warnings: Optional[List[str]] = None
