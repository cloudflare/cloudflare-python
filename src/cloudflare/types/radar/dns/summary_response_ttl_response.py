# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SummaryResponseTTLResponse", "Meta", "MetaConfidenceInfo", "Summary0"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[object]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    date_range: List[object] = FieldInfo(alias="dateRange")

    last_updated: str = FieldInfo(alias="lastUpdated")

    normalization: str

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class Summary0(BaseModel):
    gt_15m_lte_1h: str

    gt_1d_lte_1w: str

    gt_1h_lte_1d: str

    gt_1m_lte_5m: str

    gt_1w: str

    gt_5m_lte_15m: str

    lte_1m: str


class SummaryResponseTTLResponse(BaseModel):
    meta: Meta

    summary_0: Summary0
