# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["AddressingAddressMaps"]


class AddressingAddressMaps(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    can_delete: Optional[bool] = None
    """If set to false, then the Address Map cannot be deleted via API.

    This is true for Cloudflare-managed maps.
    """

    can_modify_ips: Optional[bool] = None
    """If set to false, then the IPs on the Address Map cannot be modified via the API.

    This is true for Cloudflare-managed maps.
    """

    created_at: Optional[datetime] = None

    default_sni: Optional[str] = None
    """
    If you have legacy TLS clients which do not send the TLS server name indicator,
    then you can specify one default SNI on the map. If Cloudflare receives a TLS
    handshake from a client without an SNI, it will respond with the default SNI on
    those IPs. The default SNI can be any valid zone or subdomain owned by the
    account.
    """

    description: Optional[str] = None
    """
    An optional description field which may be used to describe the types of IPs or
    zones on the map.
    """

    enabled: Optional[bool] = None
    """Whether the Address Map is enabled or not.

    Cloudflare's DNS will not respond with IP addresses on an Address Map until the
    map is enabled.
    """

    modified_at: Optional[datetime] = None
