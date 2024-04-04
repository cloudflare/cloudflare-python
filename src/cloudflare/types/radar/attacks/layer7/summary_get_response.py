# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel
from ....unnamed_schema_ref_174 import UnnamedSchemaRef174
from ....unnamed_schema_ref_175 import UnnamedSchemaRef175

__all__ = ["SummaryGetResponse", "Meta", "MetaConfidenceInfo", "Summary0"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[UnnamedSchemaRef174]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    date_range: List[UnnamedSchemaRef175] = FieldInfo(alias="dateRange")

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class Summary0(BaseModel):
    access_rules: str = FieldInfo(alias="ACCESS_RULES")

    api_shield: str = FieldInfo(alias="API_SHIELD")

    bot_management: str = FieldInfo(alias="BOT_MANAGEMENT")

    data_loss_prevention: str = FieldInfo(alias="DATA_LOSS_PREVENTION")

    ddos: str = FieldInfo(alias="DDOS")

    ip_reputation: str = FieldInfo(alias="IP_REPUTATION")

    waf: str = FieldInfo(alias="WAF")


class SummaryGetResponse(BaseModel):
    meta: Meta

    summary_0: Summary0
