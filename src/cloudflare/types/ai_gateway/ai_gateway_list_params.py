# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AIGatewayListParams"]


class AIGatewayListParams(TypedDict, total=False):
    id: str

    order_by: str
    """Order By Column Name"""

    page: int

    per_page: int
