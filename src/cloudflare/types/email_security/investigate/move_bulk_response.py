# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["MoveBulkResponse"]


class MoveBulkResponse(BaseModel):
    completed_timestamp: datetime

    destination: str

    item_count: int

    message_id: str

    operation: str

    recipient: str

    status: str
