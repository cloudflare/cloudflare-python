# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AIGatewayListParams"]


class AIGatewayListParams(TypedDict, total=False):
    account_id: Required[str]

    id: str
    """gateway id"""

    order_by: str
    """Order By Column Name"""

    order_by_direction: Literal["asc", "desc"]
    """Order By Direction"""

    page: int

    per_page: int
