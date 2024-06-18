# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RegionalHostnameEditParams"]


class RegionalHostnameEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    region_key: Required[str]
    """Identifying key for the region"""
