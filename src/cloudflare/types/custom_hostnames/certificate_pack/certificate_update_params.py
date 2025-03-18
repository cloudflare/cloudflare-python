# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CertificateUpdateParams"]


class CertificateUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    custom_hostname_id: Required[str]
    """Identifier"""

    certificate_pack_id: Required[str]
    """Identifier"""

    custom_certificate: Required[str]
    """If a custom uploaded certificate is used."""

    custom_key: Required[str]
    """The key for a custom uploaded certificate."""
