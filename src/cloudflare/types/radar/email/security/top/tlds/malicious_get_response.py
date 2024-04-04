# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ......shared import UnnamedSchemaRef2173d81a0b2d332c9e2ac46900fe8bb9
from ......._models import BaseModel
from ......unnamed_schema_ref_b5f3bd1840490bc487ffef84567807b1 import UnnamedSchemaRefB5f3bd1840490bc487ffef84567807b1
from ......unnamed_schema_ref_baac9d7da12de53e99142f8ecd3982e5 import UnnamedSchemaRefBaac9d7da12de53e99142f8ecd3982e5

__all__ = ["MaliciousGetResponse", "Meta", "MetaConfidenceInfo"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[UnnamedSchemaRefB5f3bd1840490bc487ffef84567807b1]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    date_range: List[UnnamedSchemaRefBaac9d7da12de53e99142f8ecd3982e5] = FieldInfo(alias="dateRange")

    last_updated: str = FieldInfo(alias="lastUpdated")

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class MaliciousGetResponse(BaseModel):
    meta: Meta

    top_0: List[UnnamedSchemaRef2173d81a0b2d332c9e2ac46900fe8bb9]
