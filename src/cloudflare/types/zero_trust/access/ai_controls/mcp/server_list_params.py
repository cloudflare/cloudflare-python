# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ServerListParams"]


class ServerListParams(TypedDict, total=False):
    account_id: str

    page: int

    per_page: int

    search: str
    """Search by id, name"""
