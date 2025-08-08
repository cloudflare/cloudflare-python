# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from ..hostname import Hostname
from ..redirect import Redirect
from ...._models import BaseModel

__all__ = [
    "ItemListResponse",
    "ListsListItemIPFull",
    "ListsListItemHostnameFull",
    "ListsListItemRedirectFull",
    "ListsListItemASNFull",
]


class ListsListItemIPFull(BaseModel):
    id: str
    """The unique ID of the list."""

    created_on: str
    """The RFC 3339 timestamp of when the list was created."""

    ip: str
    """An IPv4 address, an IPv4 CIDR, an IPv6 address, or an IPv6 CIDR."""

    modified_on: str
    """The RFC 3339 timestamp of when the list was last modified."""

    comment: Optional[str] = None
    """Defines an informative summary of the list item."""


class ListsListItemHostnameFull(BaseModel):
    id: str
    """The unique ID of the list."""

    created_on: str
    """The RFC 3339 timestamp of when the list was created."""

    hostname: Hostname
    """
    Valid characters for hostnames are ASCII(7) letters from a to z, the digits from
    0 to 9, wildcards (\\**), and the hyphen (-).
    """

    modified_on: str
    """The RFC 3339 timestamp of when the list was last modified."""

    comment: Optional[str] = None
    """Defines an informative summary of the list item."""


class ListsListItemRedirectFull(BaseModel):
    id: str
    """The unique ID of the list."""

    created_on: str
    """The RFC 3339 timestamp of when the list was created."""

    modified_on: str
    """The RFC 3339 timestamp of when the list was last modified."""

    redirect: Redirect
    """The definition of the redirect."""

    comment: Optional[str] = None
    """Defines an informative summary of the list item."""


class ListsListItemASNFull(BaseModel):
    id: str
    """The unique ID of the list."""

    asn: int
    """Defines a non-negative 32 bit integer."""

    created_on: str
    """The RFC 3339 timestamp of when the list was created."""

    modified_on: str
    """The RFC 3339 timestamp of when the list was last modified."""

    comment: Optional[str] = None
    """Defines an informative summary of the list item."""


ItemListResponse: TypeAlias = Union[
    ListsListItemIPFull, ListsListItemHostnameFull, ListsListItemRedirectFull, ListsListItemASNFull
]
