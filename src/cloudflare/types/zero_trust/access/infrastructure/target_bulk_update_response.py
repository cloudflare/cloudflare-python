# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ....._models import BaseModel

__all__ = [
    "TargetBulkUpdateResponse",
    "TargetBulkUpdateResponseItem",
    "TargetBulkUpdateResponseItemIP",
    "TargetBulkUpdateResponseItemIPIPV4",
    "TargetBulkUpdateResponseItemIPIPV6",
]


class TargetBulkUpdateResponseItemIPIPV4(BaseModel):
    ip_addr: Optional[str] = None
    """IP address of the target"""

    virtual_network_id: Optional[str] = None
    """(optional) Private virtual network identifier for the target.

    If omitted, the default virtual network ID will be used.
    """


class TargetBulkUpdateResponseItemIPIPV6(BaseModel):
    ip_addr: Optional[str] = None
    """IP address of the target"""

    virtual_network_id: Optional[str] = None
    """(optional) Private virtual network identifier for the target.

    If omitted, the default virtual network ID will be used.
    """


class TargetBulkUpdateResponseItemIP(BaseModel):
    ipv4: Optional[TargetBulkUpdateResponseItemIPIPV4] = None
    """The target's IPv4 address"""

    ipv6: Optional[TargetBulkUpdateResponseItemIPIPV6] = None
    """The target's IPv6 address"""


class TargetBulkUpdateResponseItem(BaseModel):
    id: str
    """Target identifier"""

    created_at: datetime
    """Date and time at which the target was created"""

    hostname: str
    """A non-unique field that refers to a target"""

    ip: TargetBulkUpdateResponseItemIP
    """The IPv4/IPv6 address that identifies where to reach a target"""

    modified_at: datetime
    """Date and time at which the target was modified"""


TargetBulkUpdateResponse: TypeAlias = List[TargetBulkUpdateResponseItem]
