# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

from typing import Optional

from ...percentiles import Percentiles

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["HTTPDetailsPercentiles"]


class HTTPDetailsPercentiles(BaseModel):
    dns_response_time_ms: Optional[Percentiles] = FieldInfo(alias="dnsResponseTimeMs", default=None)

    resource_fetch_time_ms: Optional[Percentiles] = FieldInfo(alias="resourceFetchTimeMs", default=None)

    server_response_time_ms: Optional[Percentiles] = FieldInfo(alias="serverResponseTimeMs", default=None)
