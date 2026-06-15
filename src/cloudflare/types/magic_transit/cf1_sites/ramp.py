# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .ramp_type import RampType
from ...._models import BaseModel

__all__ = ["Ramp", "GRE", "GREInterconnect", "IPSEC", "Mconn", "MplsInterconnect"]


class GRE(BaseModel):
    managed_by: Optional[str] = None
    """URL reference to the source network resource that this ramp is managed by."""


class GREInterconnect(BaseModel):
    managed_by: Optional[str] = None
    """URL reference to the source network resource that this ramp is managed by."""


class IPSEC(BaseModel):
    managed_by: Optional[str] = None
    """URL reference to the source network resource that this ramp is managed by."""


class Mconn(BaseModel):
    managed_by: Optional[str] = None
    """URL reference to the source network resource that this ramp is managed by."""


class MplsInterconnect(BaseModel):
    managed_by: Optional[str] = None
    """URL reference to the source network resource that this ramp is managed by."""


class Ramp(BaseModel):
    id: str
    """Identifier"""

    created_on: datetime

    modified_on: datetime

    name: str
    """
    A human-provided name describing the ramp that should be unique within the CF1
    Site.
    """

    type: RampType
    """
    The type of network connection (ramp) linking a CF1 Site to Cloudflare's
    network.
    """

    description: Optional[str] = None
    """A human-provided description of the ramp."""

    gre: Optional[GRE] = None

    gre_interconnect: Optional[GREInterconnect] = None

    ipsec: Optional[IPSEC] = None

    mconn: Optional[Mconn] = None

    mpls_interconnect: Optional[MplsInterconnect] = None
