# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IngressCreateParams"]


class IngressCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    cidr: Required[str]
    """
    The CIDR block for the ingress rule in IPv4 or IPv6 notation (e.g.,
    192.0.2.0/24). Must be a Cloudflare BYOIP associated with your account.
    """
