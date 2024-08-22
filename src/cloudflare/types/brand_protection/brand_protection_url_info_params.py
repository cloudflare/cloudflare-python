# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["BrandProtectionURLInfoParams"]


class BrandProtectionURLInfoParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    url: List[str]
    """Submission URL(s) to filter submission results by."""

    url_id: Iterable[int]
    """Submission ID(s) to filter submission results by."""
