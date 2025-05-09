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

    on_demand: OnDemand

    withdraw_if_no_route: bool
    """
    Controls whether the BGP prefix is automatically withdrawn when prefix is
    withdrawn from Magic routing table (for Magic Transit customers using Direct
    CNI)
    """


class OnDemand(TypedDict, total=False):
    advertised: bool
