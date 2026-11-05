# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["StreamListParams"]


class StreamListParams(TypedDict, total=False):
    account_id: Required[str]
    """Specifies the public ID of the account."""

    direction: Literal["asc", "desc"]
    """Sort direction."""

    name: str
    """Filters streams by name (case-insensitive substring)."""

    order_by: Literal["name", "created_at"]
    """Sorts streams by this field. Defaults to `created_at`."""

    page: float

    per_page: float

    pipeline_id: str
    """Specifies the public ID of the pipeline."""
