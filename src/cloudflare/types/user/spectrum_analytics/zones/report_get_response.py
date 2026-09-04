# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ....._models import BaseModel

__all__ = [
    "ReportGetResponse",
    "ReportGetResponseItem",
    "ReportGetResponseItemTotals",
    "ReportGetResponseItemTotalsBandwidth",
]


class ReportGetResponseItemTotalsBandwidth(BaseModel):
    all: float
    """Sum of ingress and egress bytes transferred."""

    egress: float
    """Sum of egress bytes transferred."""

    ingress: float
    """Sum of ingress bytes transferred."""


class ReportGetResponseItemTotals(BaseModel):
    bandwidth: ReportGetResponseItemTotalsBandwidth


class ReportGetResponseItem(BaseModel):
    totals: ReportGetResponseItemTotals

    zone_id: str
    """Identifier."""


ReportGetResponse: TypeAlias = List[ReportGetResponseItem]
