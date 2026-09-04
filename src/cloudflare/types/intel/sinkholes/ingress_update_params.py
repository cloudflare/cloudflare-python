# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IngressUpdateParams"]


class IngressUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """An identifier for the resource."""

    sinkhole_id: Required[str]

    cidr: Required[str]
    """
    The CIDR block for the ingress rule in IPv4 or IPv6 notation (e.g.,
    192.0.2.0/24). Provide a Cloudflare BYOIP CIDR that your account owns.
    """
