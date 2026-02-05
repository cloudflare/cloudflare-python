# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["NamespaceListResponse", "Detail"]


class Detail(BaseModel):
    """Contains namespace with metadata details."""

    namespace: List[str]
    """
    Specifies the hierarchical namespace parts as an array of strings. For example,
    ["bronze", "analytics"] represents the namespace "bronze.analytics".
    """

    namespace_uuid: str
    """Contains the UUID that persists across renames."""

    created_at: Optional[datetime] = None
    """Indicates the creation timestamp in ISO 8601 format."""

    updated_at: Optional[datetime] = None
    """Shows the last update timestamp in ISO 8601 format. Null if never updated."""


class NamespaceListResponse(BaseModel):
    """Contains the list of namespaces with optional pagination."""

    namespaces: List[List[str]]
    """Lists namespaces in the catalog."""

    details: Optional[List[Detail]] = None
    """
    Contains detailed metadata for each namespace when return_details is true. Each
    object includes the namespace, UUID, and timestamps.
    """

    namespace_uuids: Optional[List[str]] = None
    """
    Contains UUIDs for each namespace when return_uuids is true. The order
    corresponds to the namespaces array.
    """

    next_page_token: Optional[str] = None
    """
    Use this opaque token to fetch the next page of results. A null or absent value
    indicates the last page.
    """
