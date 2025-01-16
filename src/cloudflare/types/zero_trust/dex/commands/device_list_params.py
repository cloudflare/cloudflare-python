# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DeviceListParams"]


class DeviceListParams(TypedDict, total=False):
    account_id: Required[str]

    page: Required[float]
    """Page number of paginated results"""

    per_page: Required[float]
    """Number of items per page"""

    search: str
    """Filter devices by name or email"""
