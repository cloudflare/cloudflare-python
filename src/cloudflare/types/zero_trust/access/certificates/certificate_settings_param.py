# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CertificateSettingsParam"]


class CertificateSettingsParam(TypedDict, total=False):
    china_network: Required[bool]
    """Request client certificates for this hostname in China.

    Can only be set to true if this zone is china network enabled.
    """

    client_certificate_forwarding: Required[bool]
    """
    Client Certificate Forwarding is a feature that takes the client cert provided
    by the eyeball to the edge, and forwards it to the origin as a HTTP header to
    allow logging on the origin.
    """

    hostname: Required[str]
    """The hostname that these settings apply to."""
