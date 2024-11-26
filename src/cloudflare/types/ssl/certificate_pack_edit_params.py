# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CertificatePackEditParams"]


class CertificatePackEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    cloudflare_branding: bool
    """Whether or not to add Cloudflare Branding for the order.

    This will add a subdomain of sni.cloudflaressl.com as the Common Name if set to
    true.
    """
