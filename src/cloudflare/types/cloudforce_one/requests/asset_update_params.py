# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AssetUpdateParams"]


class AssetUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    request_id: Required[str]
    """UUID."""

    source: str
    """Asset file to upload."""
