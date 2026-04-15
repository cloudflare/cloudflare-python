# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProviderConfigListParams"]


class ProviderConfigListParams(TypedDict, total=False):
    account_id: str

    page: int

    per_page: int
