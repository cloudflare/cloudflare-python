# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BrandProtectionSubmitParams"]


class BrandProtectionSubmitParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    url: str
    """URL(s) to filter submissions results by"""
