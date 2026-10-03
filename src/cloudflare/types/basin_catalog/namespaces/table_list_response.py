# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["TableListResponse", "Identifier", "Detail", "DetailIdentifier"]


class Identifier(BaseModel):
    """Specifies a unique table identifier within a catalog."""

    name: str
    """Specifies the table name."""

    namespace: List[str]
    """
    Specifies the hierarchical namespace parts as an array of strings. For example,
    ["bronze", "analytics"] represents the namespace "bronze.analytics".
    """


class DetailIdentifier(BaseModel):
    """Specifies a unique table identifier within a catalog."""

    name: str
    """Specifies the table name."""

    namespace: List[str]
    """
    Specifies the hierarchical namespace parts as an array of strings. For example,
    ["bronze", "analytics"] represents the namespace "bronze.analytics".
    """


class Detail(BaseModel):
    """Contains table with metadata."""

    identifier: DetailIdentifier
    """Specifies a unique table identifier within a catalog."""

    table_uuid: str
    """Contains the UUID that persists across renames."""

    created_at: Optional[datetime] = None
    """Indicates the creation timestamp in ISO 8601 format."""

    location: Optional[str] = None
    """Specifies the base S3 URI for table storage location."""

    metadata_location: Optional[str] = None
    """Contains the S3 URI to table metadata file. Null for staged tables."""

    updated_at: Optional[datetime] = None
    """Shows the last update timestamp in ISO 8601 format. Null if never updated."""


class TableListResponse(BaseModel):
    """Contains the list of tables with optional pagination."""

    identifiers: List[Identifier]
    """Lists tables in the namespace."""

    details: Optional[List[Detail]] = None
    """
    Contains detailed metadata for each table when return_details is true. Each
    object includes identifier, UUID, timestamps, and locations.
    """

    next_page_token: Optional[str] = None
    """
    Use this opaque token to fetch the next page of results. A null or absent value
    indicates the last page.
    """

    table_uuids: Optional[List[str]] = None
    """
    Contains UUIDs for each table when return_uuids is true. The order corresponds
    to the identifiers array.
    """
