# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NamespaceListParams"]


class NamespaceListParams(TypedDict, total=False):
    account_id: Required[str]
    """Use this to identify the account."""

    page_size: int
    """Maximum number of namespaces to return per page. Defaults to 100, maximum 1000."""

    page_token: str
    """
    Opaque pagination token from a previous response. Use this to fetch the next
    page of results.
    """

    parent: str
    """Parent namespace to filter by.

    Only returns direct children of this namespace. For nested namespaces, use %1F
    as separator (e.g., "bronze%1Fanalytics"). Omit this parameter to list top-level
    namespaces.
    """

    return_details: bool
    """
    Whether to include additional metadata (timestamps). When true, response
    includes created_at and updated_at arrays.
    """

    return_uuids: bool
    """
    Whether to include namespace UUIDs in the response. Set to true to receive the
    namespace_uuids array.
    """
