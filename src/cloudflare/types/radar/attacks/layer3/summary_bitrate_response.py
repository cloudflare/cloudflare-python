# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel
from ....unnamed_schema_ref_174 import UnnamedSchemaRef174
from ....unnamed_schema_ref_175 import UnnamedSchemaRef175

__all__ = ["SummaryBitrateResponse", "Meta", "MetaConfidenceInfo", "Summary0"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[UnnamedSchemaRef174]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    date_range: List[UnnamedSchemaRef175] = FieldInfo(alias="dateRange")

    last_updated: str = FieldInfo(alias="lastUpdated")

    normalization: str

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class Summary0(BaseModel):
    one_gbps_to_ten_gbps: str = FieldInfo(alias="_1_GBPS_TO_10_GBPS")

    ten_gbps_to_one_hundred_gbps: str = FieldInfo(alias="_10_GBPS_TO_100_GBPS")

    five_hundred_mbps_to_one_gbps: str = FieldInfo(alias="_500_MBPS_TO_1_GBPS")

    over_100_gbps: str = FieldInfo(alias="OVER_100_GBPS")

    under_500_mbps: str = FieldInfo(alias="UNDER_500_MBPS")


class SummaryBitrateResponse(BaseModel):
    meta: Meta

    summary_0: Summary0
