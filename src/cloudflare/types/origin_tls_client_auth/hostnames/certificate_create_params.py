# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CertificateCreateParams"]


class CertificateCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    certificate: Required[str]
    """The hostname certificate."""

    private_key: Required[str]
    """The hostname certificate's private key."""
