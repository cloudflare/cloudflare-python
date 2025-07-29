# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = [
    "BulkOperationGetResponse",
    "ListsBulkOperationPendingOrRunning",
    "ListsBulkOperationCompleted",
    "ListsBulkOperationFailed",
]


class ListsBulkOperationPendingOrRunning(BaseModel):
    id: str
    """The unique operation ID of the asynchronous action."""

    status: Literal["pending", "running"]
    """The current status of the asynchronous operation."""


class ListsBulkOperationCompleted(BaseModel):
    id: str
    """The unique operation ID of the asynchronous action."""

    completed: str
    """The RFC 3339 timestamp of when the operation was completed."""

    status: Literal["completed"]
    """The current status of the asynchronous operation."""


class ListsBulkOperationFailed(BaseModel):
    id: str
    """The unique operation ID of the asynchronous action."""

    completed: str
    """The RFC 3339 timestamp of when the operation was completed."""

    error: str
    """A message describing the error when the status is `failed`."""

    status: Literal["failed"]
    """The current status of the asynchronous operation."""


BulkOperationGetResponse: TypeAlias = Union[
    ListsBulkOperationPendingOrRunning, ListsBulkOperationCompleted, ListsBulkOperationFailed
]
