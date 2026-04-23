# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["StreamListParams"]


class StreamListParams(TypedDict, total=False):
    account_id: Required[str]
    """Specifies the public ID of the account."""

    page: float

    per_page: float

    pipeline_id: str
    """Specifies the public ID of the pipeline."""
