# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ItemListParams"]


class ItemListParams(TypedDict, total=False):
    account_id: Required[str]

    page: int

    per_page: int

    search: str

    status: Literal["queued", "running", "completed", "error", "skipped"]
