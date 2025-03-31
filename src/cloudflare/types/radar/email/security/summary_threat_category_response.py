# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["SummaryThreatCategoryResponse", "Meta", "MetaConfidenceInfo", "Summary0"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[object]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    date_range: List[object] = FieldInfo(alias="dateRange")

    last_updated: str = FieldInfo(alias="lastUpdated")

    normalization: str

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class Summary0(BaseModel):
    brand_impersonation: str = FieldInfo(alias="BrandImpersonation")

    credential_harvester: str = FieldInfo(alias="CredentialHarvester")

    identity_deception: str = FieldInfo(alias="IdentityDeception")

    link: str = FieldInfo(alias="Link")


class SummaryThreatCategoryResponse(BaseModel):
    meta: Meta

    summary_0: Summary0
