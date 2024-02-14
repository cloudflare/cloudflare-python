# File generated from our OpenAPI spec by Stainless.

from typing import Optional, Union

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

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
