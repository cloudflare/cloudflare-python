# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...unnamed_schema_ref_174 import UnnamedSchemaRef174
from ...unnamed_schema_ref_175 import UnnamedSchemaRef175

__all__ = ["SummaryTLSVersionResponse", "Meta", "MetaConfidenceInfo", "Summary0"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[UnnamedSchemaRef174]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    date_range: List[UnnamedSchemaRef175] = FieldInfo(alias="dateRange")

    last_updated: str = FieldInfo(alias="lastUpdated")

    normalization: str

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class Summary0(BaseModel):
    tls_1_0: str = FieldInfo(alias="TLS 1.0")

    tls_1_1: str = FieldInfo(alias="TLS 1.1")

    tls_1_2: str = FieldInfo(alias="TLS 1.2")

    tls_1_3: str = FieldInfo(alias="TLS 1.3")

    tls_quic: str = FieldInfo(alias="TLS QUIC")


class SummaryTLSVersionResponse(BaseModel):
    meta: Meta

    summary_0: Summary0
