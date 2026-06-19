# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BulkListParams"]


class BulkListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    action_type: Literal["MOVE", "RELEASE"]

    page: int
    """Current page within paginated list of results."""

    per_page: int
    """The number of results per page. Maximum value is 1000."""

    status: Literal["PENDING", "DISCOVERING", "PROCESSING", "COMPLETED", "FAILED", "CANCELLED", "SKIPPED"]
