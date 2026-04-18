# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BGPPrefixEditParams", "OnDemand"]


class BGPPrefixEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier of a Cloudflare account."""

    prefix_id: Required[str]
    """Identifier of an IP Prefix."""

    asn_prepend_count: int
    """Number of times to prepend the Cloudflare ASN to the BGP AS-Path attribute"""

    auto_advertise_withdraw: bool
    """
    Determines if Cloudflare advertises a BYOIP BGP prefix even when there is no
    matching BGP prefix in the Magic routing table. When true, Cloudflare will
    automatically withdraw the BGP prefix when there are no matching BGP routes, and
    will resume advertising when there is at least one matching BGP route.
    """

    on_demand: OnDemand


class OnDemand(TypedDict, total=False):
    advertised: bool
