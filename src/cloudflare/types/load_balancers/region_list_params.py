# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RegionListParams"]


class RegionListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    country_code_a2: str
    """Two-letter alpha-2 country code followed in ISO 3166-1."""

    subdivision_code: str
    """Two-letter subdivision code followed in ISO 3166-2."""

    subdivision_code_a2: str
    """Two-letter subdivision code followed in ISO 3166-2."""
