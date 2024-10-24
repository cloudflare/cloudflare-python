# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .operation_status import OperationStatus

__all__ = ["BulkOperationGetResponse"]


class BulkOperationGetResponse(BaseModel):
    id: str
    """The unique operation ID of the asynchronous action."""

    status: OperationStatus
    """The current status of the asynchronous operation."""

    completed: Optional[str] = None
    """The RFC 3339 timestamp of when the operation was completed."""

    error: Optional[str] = None
    """A message describing the error when the status is `failed`."""
