# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["SummaryDurationResponse", "Meta", "MetaConfidenceInfo", "Summary0"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[object]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    date_range: List[object] = FieldInfo(alias="dateRange")

    last_updated: str = FieldInfo(alias="lastUpdated")

    normalization: str

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class Summary0(BaseModel):
    one_hour_to_three_hours: str = FieldInfo(alias="_1_HOUR_TO_3_HOURS")

    ten_mins_to_twenty_mins: str = FieldInfo(alias="_10_MINS_TO_20_MINS")

    twenty_mins_to_forty_mins: str = FieldInfo(alias="_20_MINS_TO_40_MINS")

    forty_mins_to_one_hour: str = FieldInfo(alias="_40_MINS_TO_1_HOUR")

    over_3_hours: str = FieldInfo(alias="OVER_3_HOURS")

    under_10_mins: str = FieldInfo(alias="UNDER_10_MINS")


class SummaryDurationResponse(BaseModel):
    meta: Meta

    summary_0: Summary0
