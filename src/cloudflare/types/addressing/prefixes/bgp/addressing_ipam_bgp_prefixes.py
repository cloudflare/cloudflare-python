# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["AddressingIpamBGPPrefixes", "BGPSignalOpts", "OnDemand"]


class BGPSignalOpts(BaseModel):
    enabled: Optional[bool] = None
    """
    Whether control of advertisement of the prefix to the Internet is enabled to be
    performed via BGP signal
    """

    modified_at: Optional[datetime] = None
    """Last time BGP signaling control was toggled.

    This field is null if BGP signaling has never been enabled.
    """


class OnDemand(BaseModel):
    advertised: Optional[bool] = None
    """Prefix advertisement status to the Internet.

    This field is only not 'null' if on demand is enabled.
    """

    advertised_modified_at: Optional[datetime] = None
    """Last time the advertisement status was changed.

    This field is only not 'null' if on demand is enabled.
    """

    on_demand_enabled: Optional[bool] = None
    """
    Whether advertisement of the prefix to the Internet may be dynamically enabled
    or disabled.
    """

    on_demand_locked: Optional[bool] = None
    """
    Whether advertisement status of the prefix is locked, meaning it cannot be
    changed.
    """


class AddressingIpamBGPPrefixes(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    asn: Optional[int] = None
    """Autonomous System Number (ASN) the prefix will be advertised under."""

    bgp_signal_opts: Optional[BGPSignalOpts] = None

    cidr: Optional[str] = None
    """IP Prefix in Classless Inter-Domain Routing format."""

    created_at: Optional[datetime] = None

    modified_at: Optional[datetime] = None

    on_demand: Optional[OnDemand] = None
