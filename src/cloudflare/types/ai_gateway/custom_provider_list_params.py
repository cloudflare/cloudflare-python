# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CustomProviderListParams"]


class CustomProviderListParams(TypedDict, total=False):
    account_id: Required[str]

    beta: bool

    enable: bool

    page: int

    per_page: int

    search: str
    """Search by id, name, slug"""
