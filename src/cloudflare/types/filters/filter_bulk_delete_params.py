# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["FilterBulkDeleteParams"]


class FilterBulkDeleteParams(TypedDict, total=False):
    zone_id: Required[str]
    """Defines an identifier."""

    id: Required[List[str]]
