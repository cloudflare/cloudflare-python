# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AddressMapEditParams"]


class AddressMapEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier of a Cloudflare account."""

    default_sni: Optional[str]
    """
    If you have legacy TLS clients which do not send the TLS server name indicator,
    then you can specify one default SNI on the map. If Cloudflare receives a TLS
    handshake from a client without an SNI, it will respond with the default SNI on
    those IPs. The default SNI can be any valid zone or subdomain owned by the
    account.
    """

    description: Optional[str]
    """
    An optional description field which may be used to describe the types of IPs or
    zones on the map.
    """

    enabled: Optional[bool]
    """Whether the Address Map is enabled or not.

    Cloudflare's DNS will not respond with IP addresses on an Address Map until the
    map is enabled.
    """
