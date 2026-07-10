# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DatasetListParams"]


class DatasetListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    include_deleted: Annotated[bool, PropertyInfo(alias="includeDeleted")]
    """When true, include soft-deleted datasets in the response.

    Each item includes a `deletedAt` field (ISO 8601 or null). Default: false.
    """
