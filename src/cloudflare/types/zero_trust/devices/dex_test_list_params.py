# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DEXTestListParams"]


class DEXTestListParams(TypedDict, total=False):
    account_id: Required[str]

    kind: Literal["http", "traceroute"]
    """Filter by test type"""

    page: float
    """Page number of paginated results"""

    per_page: float
    """Number of items per page"""

    test_name: Annotated[str, PropertyInfo(alias="testName")]
    """Filter by test name"""
