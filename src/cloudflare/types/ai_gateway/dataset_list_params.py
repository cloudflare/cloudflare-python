# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DatasetListParams"]


class DatasetListParams(TypedDict, total=False):
    account_id: Required[str]

    enable: bool

    name: str

    page: int

    per_page: int

    search: str
    """Search by id, name, filters"""
