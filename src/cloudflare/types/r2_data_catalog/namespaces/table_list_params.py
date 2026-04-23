# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TableListParams"]


class TableListParams(TypedDict, total=False):
    account_id: Required[str]
    """Use this to identify the account."""

    bucket_name: Required[str]
    """Specifies the R2 bucket name."""

    page_size: int
    """Maximum number of tables to return per page. Defaults to 100, maximum 1000."""

    page_token: str
    """
    Opaque pagination token from a previous response. Use this to fetch the next
    page of results.
    """

    return_details: bool
    """
    Whether to include additional metadata (timestamps, locations). When true,
    response includes created_at, updated_at, metadata_locations, and locations
    arrays.
    """

    return_uuids: bool
    """
    Whether to include table UUIDs in the response. Set to true to receive the
    table_uuids array.
    """
