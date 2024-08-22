# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

from datetime import datetime

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["SummaryMitigationProductResponse", "Meta", "MetaDateRange", "MetaConfidenceInfo", "MetaConfidenceInfoAnnotation", "Summary0"]

class MetaDateRange(BaseModel):
    end_time: datetime = FieldInfo(alias = "endTime")
    """Adjusted end of date range."""

    start_time: datetime = FieldInfo(alias = "startTime")
    """Adjusted start of date range."""

class MetaConfidenceInfoAnnotation(BaseModel):
    data_source: str = FieldInfo(alias = "dataSource")

    description: str

    event_type: str = FieldInfo(alias = "eventType")

    is_instantaneous: bool = FieldInfo(alias = "isInstantaneous")

    end_time: Optional[datetime] = FieldInfo(alias = "endTime", default = None)

    linked_url: Optional[str] = FieldInfo(alias = "linkedUrl", default = None)

    start_time: Optional[datetime] = FieldInfo(alias = "startTime", default = None)

class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[MetaConfidenceInfoAnnotation]] = None

    level: Optional[int] = None

class Meta(BaseModel):
    date_range: List[MetaDateRange] = FieldInfo(alias = "dateRange")

    last_updated: str = FieldInfo(alias = "lastUpdated")

    normalization: str

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias = "confidenceInfo", default = None)

class Summary0(BaseModel):
    ddos: str = FieldInfo(alias = "DDOS")

    waf: str = FieldInfo(alias = "WAF")

class SummaryMitigationProductResponse(BaseModel):
    meta: Meta

    summary_0: Summary0