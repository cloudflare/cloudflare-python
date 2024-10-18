# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = [
    "BulkGetResponse",
    "BulkGetResponseItem",
    "BulkGetResponseItemAdditionalInformation",
    "BulkGetResponseItemApplication",
    "BulkGetResponseItemContentCategory",
    "BulkGetResponseItemInheritedContentCategory",
    "BulkGetResponseItemInheritedRiskType",
    "BulkGetResponseItemRiskType",
]


class BulkGetResponseItemAdditionalInformation(BaseModel):
    suspected_malware_family: Optional[str] = None
    """Suspected DGA malware family."""


class BulkGetResponseItemApplication(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None


class BulkGetResponseItemContentCategory(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

    super_category_id: Optional[int] = None


class BulkGetResponseItemInheritedContentCategory(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

    super_category_id: Optional[int] = None


class BulkGetResponseItemInheritedRiskType(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

    super_category_id: Optional[int] = None


class BulkGetResponseItemRiskType(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

    super_category_id: Optional[int] = None


class BulkGetResponseItem(BaseModel):
    additional_information: Optional[BulkGetResponseItemAdditionalInformation] = None
    """Additional information related to the host name."""

    application: Optional[BulkGetResponseItemApplication] = None
    """Application that the hostname belongs to."""

    content_categories: Optional[List[BulkGetResponseItemContentCategory]] = None

    domain: Optional[str] = None

    inherited_content_categories: Optional[List[BulkGetResponseItemInheritedContentCategory]] = None

    inherited_from: Optional[str] = None
    """
    Domain from which `inherited_content_categories` and `inherited_risk_types` are
    inherited, if applicable.
    """

    inherited_risk_types: Optional[List[BulkGetResponseItemInheritedRiskType]] = None

    popularity_rank: Optional[int] = None
    """
    Global Cloudflare 100k ranking for the last 30 days, if available for the
    hostname. The top ranked domain is 1, the lowest ranked domain is 100,000.
    """

    risk_score: Optional[float] = None
    """
    Hostname risk score, which is a value between 0 (lowest risk) to 1 (highest
    risk).
    """

    risk_types: Optional[List[BulkGetResponseItemRiskType]] = None


BulkGetResponse: TypeAlias = List[BulkGetResponseItem]
