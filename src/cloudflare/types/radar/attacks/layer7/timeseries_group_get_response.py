# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ....._models import BaseModel
from ....unnamed_schema_ref_b5f3bd1840490bc487ffef84567807b1 import UnnamedSchemaRefB5f3bd1840490bc487ffef84567807b1
from ....unnamed_schema_ref_baac9d7da12de53e99142f8ecd3982e5 import UnnamedSchemaRefBaac9d7da12de53e99142f8ecd3982e5

__all__ = ["TimeseriesGroupGetResponse", "Meta", "MetaConfidenceInfo", "Serie0"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[UnnamedSchemaRefB5f3bd1840490bc487ffef84567807b1]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    agg_interval: str = FieldInfo(alias="aggInterval")

    date_range: List[UnnamedSchemaRefBaac9d7da12de53e99142f8ecd3982e5] = FieldInfo(alias="dateRange")

    last_updated: datetime = FieldInfo(alias="lastUpdated")

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class Serie0(BaseModel):
    access_rules: List[str] = FieldInfo(alias="ACCESS_RULES")

    api_shield: List[str] = FieldInfo(alias="API_SHIELD")

    bot_management: List[str] = FieldInfo(alias="BOT_MANAGEMENT")

    data_loss_prevention: List[str] = FieldInfo(alias="DATA_LOSS_PREVENTION")

    ddos: List[str] = FieldInfo(alias="DDOS")

    ip_reputation: List[str] = FieldInfo(alias="IP_REPUTATION")

    timestamps: List[datetime]

    waf: List[str] = FieldInfo(alias="WAF")


class TimeseriesGroupGetResponse(BaseModel):
    meta: Meta

    serie_0: Serie0
