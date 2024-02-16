# File generated from our OpenAPI spec by Stainless.

from typing import List, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "IPIPIntelligenceGetIPOverviewResponse",
    "IpipIntelligenceGetIPOverviewResponseItem",
    "IpipIntelligenceGetIPOverviewResponseItemBelongsToRef",
]


class IpipIntelligenceGetIPOverviewResponseItemBelongsToRef(BaseModel):
    id: Optional[object] = None

    country: Optional[str] = None

    description: Optional[str] = None

    type: Optional[Literal["hosting_provider", "isp", "organization"]] = None
    """Infrastructure type of this ASN."""

    value: Optional[str] = None


class IpipIntelligenceGetIPOverviewResponseItem(BaseModel):
    belongs_to_ref: Optional[IpipIntelligenceGetIPOverviewResponseItemBelongsToRef] = None
    """
    Specifies a reference to the autonomous systems (AS) that the IP address belongs
    to.
    """

    ip: Union[str, str, None] = None

    risk_types: Optional[object] = None


IPIPIntelligenceGetIPOverviewResponse = List[IpipIntelligenceGetIPOverviewResponseItem]
