# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = ["BulkOperationGetResponse", "UnionMember0", "UnionMember1", "UnionMember2"]


class UnionMember0(BaseModel):
    id: str
    """The unique operation ID of the asynchronous action."""

    completed: str
    """The RFC 3339 timestamp of when the operation was completed."""

    error: str
    """A message describing the error when the status is `failed`."""

    status: Literal["failed"]
    """The current status of the asynchronous operation."""


class UnionMember1(BaseModel):
    id: str
    """The unique operation ID of the asynchronous action."""

    status: Literal["pending", "running"]
    """The current status of the asynchronous operation."""


class UnionMember2(BaseModel):
    id: str
    """The unique operation ID of the asynchronous action."""

    completed: str
    """The RFC 3339 timestamp of when the operation was completed."""

    status: Literal["completed"]
    """The current status of the asynchronous operation."""


BulkOperationGetResponse: TypeAlias = Union[UnionMember0, UnionMember1, UnionMember2]
