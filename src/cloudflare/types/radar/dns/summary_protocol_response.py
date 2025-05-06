# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SummaryProtocolResponse", "Meta", "MetaConfidenceInfo", "Summary0"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[object]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    date_range: List[object] = FieldInfo(alias="dateRange")

    last_updated: str = FieldInfo(alias="lastUpdated")

    normalization: str

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class Summary0(BaseModel):
    https: str = FieldInfo(alias="HTTPS")

    tcp: str = FieldInfo(alias="TCP")

    tls: str = FieldInfo(alias="TLS")

    udp: str = FieldInfo(alias="UDP")


class SummaryProtocolResponse(BaseModel):
    meta: Meta

    summary_0: Summary0
