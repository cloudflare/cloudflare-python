# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = [
    "ManagedTransformEditResponse",
    "UnionMember0",
    "UnionMember0ManagedRequestHeader",
    "UnionMember0ManagedResponseHeader",
    "UnionMember1",
    "UnionMember1ManagedRequestHeader",
    "UnionMember1ManagedResponseHeader",
    "UnionMember2",
    "UnionMember2ManagedRequestHeader",
    "UnionMember2ManagedResponseHeader",
    "UnionMember3",
    "UnionMember3ManagedRequestHeader",
    "UnionMember3ManagedResponseHeader",
    "UnionMember4",
    "UnionMember4ManagedRequestHeader",
    "UnionMember4ManagedResponseHeader",
]


class UnionMember0ManagedRequestHeader(BaseModel):
    """A Managed Transform object."""

    id: str
    """The human-readable identifier of the Managed Transform."""

    enabled: bool
    """Whether the Managed Transform is enabled."""

    has_conflict: bool
    """
    Whether the Managed Transform conflicts with the currently-enabled Managed
    Transforms.
    """

    conflicts_with: Optional[List[str]] = None
    """The Managed Transforms that this Managed Transform conflicts with."""


class UnionMember0ManagedResponseHeader(BaseModel):
    """A Managed Transform object."""

    id: str
    """The human-readable identifier of the Managed Transform."""

    enabled: bool
    """Whether the Managed Transform is enabled."""

    has_conflict: bool
    """
    Whether the Managed Transform conflicts with the currently-enabled Managed
    Transforms.
    """

    conflicts_with: Optional[List[str]] = None
    """The Managed Transforms that this Managed Transform conflicts with."""


class UnionMember0(BaseModel):
    managed_request_headers: Optional[List[UnionMember0ManagedRequestHeader]] = None
    """The list of Managed Request Transforms."""

    managed_response_headers: Optional[List[UnionMember0ManagedResponseHeader]] = None
    """The list of Managed Response Transforms."""


class UnionMember1ManagedRequestHeader(BaseModel):
    """A Managed Transform object."""

    id: str
    """The human-readable identifier of the Managed Transform."""

    enabled: bool
    """Whether the Managed Transform is enabled."""

    has_conflict: bool
    """
    Whether the Managed Transform conflicts with the currently-enabled Managed
    Transforms.
    """

    conflicts_with: Optional[List[str]] = None
    """The Managed Transforms that this Managed Transform conflicts with."""


class UnionMember1ManagedResponseHeader(BaseModel):
    """A Managed Transform object."""

    id: str
    """The human-readable identifier of the Managed Transform."""

    enabled: bool
    """Whether the Managed Transform is enabled."""

    has_conflict: bool
    """
    Whether the Managed Transform conflicts with the currently-enabled Managed
    Transforms.
    """

    conflicts_with: Optional[List[str]] = None
    """The Managed Transforms that this Managed Transform conflicts with."""


class UnionMember1(BaseModel):
    managed_request_headers: Optional[List[UnionMember1ManagedRequestHeader]] = None
    """The list of Managed Request Transforms."""

    managed_response_headers: Optional[List[UnionMember1ManagedResponseHeader]] = None
    """The list of Managed Response Transforms."""


class UnionMember2ManagedRequestHeader(BaseModel):
    """A Managed Transform object."""

    id: str
    """The human-readable identifier of the Managed Transform."""

    enabled: bool
    """Whether the Managed Transform is enabled."""

    has_conflict: bool
    """
    Whether the Managed Transform conflicts with the currently-enabled Managed
    Transforms.
    """

    conflicts_with: Optional[List[str]] = None
    """The Managed Transforms that this Managed Transform conflicts with."""


class UnionMember2ManagedResponseHeader(BaseModel):
    """A Managed Transform object."""

    id: str
    """The human-readable identifier of the Managed Transform."""

    enabled: bool
    """Whether the Managed Transform is enabled."""

    has_conflict: bool
    """
    Whether the Managed Transform conflicts with the currently-enabled Managed
    Transforms.
    """

    conflicts_with: Optional[List[str]] = None
    """The Managed Transforms that this Managed Transform conflicts with."""


class UnionMember2(BaseModel):
    managed_request_headers: Optional[List[UnionMember2ManagedRequestHeader]] = None
    """The list of Managed Request Transforms."""

    managed_response_headers: Optional[List[UnionMember2ManagedResponseHeader]] = None
    """The list of Managed Response Transforms."""


class UnionMember3ManagedRequestHeader(BaseModel):
    """A Managed Transform object."""

    id: str
    """The human-readable identifier of the Managed Transform."""

    enabled: bool
    """Whether the Managed Transform is enabled."""

    has_conflict: bool
    """
    Whether the Managed Transform conflicts with the currently-enabled Managed
    Transforms.
    """

    conflicts_with: Optional[List[str]] = None
    """The Managed Transforms that this Managed Transform conflicts with."""


class UnionMember3ManagedResponseHeader(BaseModel):
    """A Managed Transform object."""

    id: str
    """The human-readable identifier of the Managed Transform."""

    enabled: bool
    """Whether the Managed Transform is enabled."""

    has_conflict: bool
    """
    Whether the Managed Transform conflicts with the currently-enabled Managed
    Transforms.
    """

    conflicts_with: Optional[List[str]] = None
    """The Managed Transforms that this Managed Transform conflicts with."""


class UnionMember3(BaseModel):
    managed_request_headers: Optional[List[UnionMember3ManagedRequestHeader]] = None
    """The list of Managed Request Transforms."""

    managed_response_headers: Optional[List[UnionMember3ManagedResponseHeader]] = None
    """The list of Managed Response Transforms."""


class UnionMember4ManagedRequestHeader(BaseModel):
    """A Managed Transform object."""

    id: str
    """The human-readable identifier of the Managed Transform."""

    enabled: bool
    """Whether the Managed Transform is enabled."""

    has_conflict: bool
    """
    Whether the Managed Transform conflicts with the currently-enabled Managed
    Transforms.
    """

    conflicts_with: Optional[List[str]] = None
    """The Managed Transforms that this Managed Transform conflicts with."""


class UnionMember4ManagedResponseHeader(BaseModel):
    """A Managed Transform object."""

    id: str
    """The human-readable identifier of the Managed Transform."""

    enabled: bool
    """Whether the Managed Transform is enabled."""

    has_conflict: bool
    """
    Whether the Managed Transform conflicts with the currently-enabled Managed
    Transforms.
    """

    conflicts_with: Optional[List[str]] = None
    """The Managed Transforms that this Managed Transform conflicts with."""


class UnionMember4(BaseModel):
    managed_request_headers: Optional[List[UnionMember4ManagedRequestHeader]] = None
    """The list of Managed Request Transforms."""

    managed_response_headers: Optional[List[UnionMember4ManagedResponseHeader]] = None
    """The list of Managed Response Transforms."""


ManagedTransformEditResponse: TypeAlias = Union[
    Optional[UnionMember0], UnionMember1, UnionMember2, UnionMember3, UnionMember4
]
