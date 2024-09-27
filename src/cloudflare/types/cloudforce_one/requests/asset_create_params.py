# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AssetCreateParams"]


class AssetCreateParams(TypedDict, total=False):
    account_identifier: Required[str]
    """Identifier"""

    page: Required[int]
    """Page number of results"""

    per_page: Required[int]
    """Number of results per page"""
