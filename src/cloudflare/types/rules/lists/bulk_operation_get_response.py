# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = ["BulkOperationGetResponse", "UnionMember0", "UnionMember1"]


class UnionMember0(BaseModel):
    id: Optional[str] = None
    """The unique operation ID of the asynchronous action."""

    completed: Optional[str] = None
    """The RFC 3339 timestamp of when the operation was completed."""

    error: Optional[str] = None
    """A message describing the error when the status is `failed`."""

    status: Optional[Literal["pending", "running", "completed", "failed"]] = None
    """The current status of the asynchronous operation."""


class UnionMember1(BaseModel):
    id: Optional[str] = None
    """The unique operation ID of the asynchronous action."""

    completed: Optional[str] = None
    """The RFC 3339 timestamp of when the operation was completed."""

    error: Optional[str] = None
    """A message describing the error when the status is `failed`."""

    status: Optional[Literal["pending", "running", "completed", "failed"]] = None
    """The current status of the asynchronous operation."""


BulkOperationGetResponse: TypeAlias = Union[UnionMember0, UnionMember1]
