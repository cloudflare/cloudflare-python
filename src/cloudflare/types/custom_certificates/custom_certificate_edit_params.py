# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .geo_restrictions_param import GeoRestrictionsParam

__all__ = ["CustomCertificateEditParams"]


class CustomCertificateEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    bundle_method: object

    certificate: str
    """The zone's SSL certificate or certificate and the intermediate(s)."""

    geo_restrictions: GeoRestrictionsParam
    """
    Specify the region where your private key can be held locally for optimal TLS
    performance. HTTPS connections to any excluded data center will still be fully
    encrypted, but will incur some latency while Keyless SSL is used to complete the
    handshake with the nearest allowed data center. Options allow distribution to
    only to U.S. data centers, only to E.U. data centers, or only to highest
    security data centers. Default distribution is to all Cloudflare datacenters,
    for optimal performance.
    """

    policy: str
    """
    Specify the policy that determines the region where your private key will be
    held locally. HTTPS connections to any excluded data center will still be fully
    encrypted, but will incur some latency while Keyless SSL is used to complete the
    handshake with the nearest allowed data center. Any combination of countries,
    specified by their two letter country code
    (https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements)
    can be chosen, such as 'country: IN', as well as 'region: EU' which refers to
    the EU region. If there are too few data centers satisfying the policy, it will
    be rejected.
    """

    private_key: str
    """The zone's private key."""
