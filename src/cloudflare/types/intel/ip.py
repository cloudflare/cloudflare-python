# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["IP", "BelongsToRef", "RiskType"]


class BelongsToRef(BaseModel):
    id: Optional[str] = None

    country: Optional[str] = None

    description: Optional[str] = None

    type: Optional[Literal["hosting_provider", "isp", "organization"]] = None
    """Infrastructure type of this ASN."""

    value: Optional[str] = None


class RiskType(BaseModel):
    id: Optional[float] = None

    name: Optional[str] = None

    super_category_id: Optional[float] = None


class IP(BaseModel):
    belongs_to_ref: Optional[BelongsToRef] = None
    """
    Specifies a reference to the autonomous systems (AS) that the IP address belongs
    to.
    """

    ip: Optional[str] = None

    risk_types: Optional[List[RiskType]] = None
