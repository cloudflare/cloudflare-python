# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ListsList"]


class ListsList(BaseModel):
    id: Optional[str] = None
    """The unique ID of the list."""

    created_on: Optional[str] = None
    """The RFC 3339 timestamp of when the list was created."""

    description: Optional[str] = None
    """An informative summary of the list."""

    kind: Optional[Literal["ip", "redirect", "hostname", "asn"]] = None
    """The type of the list.

    Each type supports specific list items (IP addresses, ASNs, hostnames or
    redirects).
    """

    modified_on: Optional[str] = None
    """The RFC 3339 timestamp of when the list was last modified."""

    name: Optional[str] = None
    """An informative name for the list. Use this name in filter and rule expressions."""

    num_items: Optional[float] = None
    """The number of items in the list."""

    num_referencing_filters: Optional[float] = None
    """The number of [filters](/operations/filters-list-filters) referencing the list."""
