# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RiskScoringGetParams"]


class RiskScoringGetParams(TypedDict, total=False):
    account_identifier: Required[str]
    """Identifier"""

    direction: Literal["desc", "asc"]

    order_by: Literal["timestamp", "risk_level"]

    page: int

    per_page: int
