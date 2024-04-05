# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel
from ...percentiles import Percentiles

__all__ = ["HTTPDetailsPercentiles"]


class HTTPDetailsPercentiles(BaseModel):
    dns_response_time_ms: Optional[Percentiles] = FieldInfo(alias="dnsResponseTimeMs", default=None)

    resource_fetch_time_ms: Optional[Percentiles] = FieldInfo(alias="resourceFetchTimeMs", default=None)

    server_response_time_ms: Optional[Percentiles] = FieldInfo(alias="serverResponseTimeMs", default=None)
