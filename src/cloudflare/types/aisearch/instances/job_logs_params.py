# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["JobLogsParams"]


class JobLogsParams(TypedDict, total=False):
    account_id: Required[str]

    id: Required[str]
    """Use your AI Search ID."""

    page: int

    per_page: int
