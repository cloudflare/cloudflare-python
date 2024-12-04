# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["TargetGetResponse", "IP", "IPIPV4", "IPIPV6"]


class IPIPV4(BaseModel):
    ip_addr: Optional[str] = None
    """IP address of the target"""

    virtual_network_id: Optional[str] = None
    """(optional) Private virtual network identifier for the target.

    If omitted, the default virtual network ID will be used.
    """


class IPIPV6(BaseModel):
    ip_addr: Optional[str] = None
    """IP address of the target"""

    virtual_network_id: Optional[str] = None
    """(optional) Private virtual network identifier for the target.

    If omitted, the default virtual network ID will be used.
    """


class IP(BaseModel):
    ipv4: Optional[IPIPV4] = None
    """The target's IPv4 address"""

    ipv6: Optional[IPIPV6] = None
    """The target's IPv6 address"""


class TargetGetResponse(BaseModel):
    id: str
    """Target identifier"""

    created_at: datetime
    """Date and time at which the target was created"""

    hostname: str
    """A non-unique field that refers to a target"""

    ip: IP
    """The IPv4/IPv6 address that identifies where to reach a target"""

    modified_at: datetime
    """Date and time at which the target was modified"""
