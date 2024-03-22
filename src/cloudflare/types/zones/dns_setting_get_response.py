# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DNSSettingGetResponse", "Nameservers"]


class Nameservers(BaseModel):
    type: Literal["cloudflare.standard", "cloudflare.foundation_dns"]
    """Nameserver type"""


class DNSSettingGetResponse(BaseModel):
    nameservers: Optional[Nameservers] = None
    """
    Settings determining the nameservers through which the zone should be available.
    """
