# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DNSSettingEditParams", "Nameservers"]


class DNSSettingEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    nameservers: Nameservers
    """
    Settings determining the nameservers through which the zone should be available.
    """


class Nameservers(TypedDict, total=False):
    type: Required[Literal["cloudflare.standard", "cloudflare.foundation_dns"]]
    """Nameserver type"""
