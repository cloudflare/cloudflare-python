# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CustomCertificateSettingsParam"]


class CustomCertificateSettingsParam(TypedDict, total=False):
    """Specify custom certificate settings for BYO-PKI.

    This field is deprecated; use `certificate` instead.
    """

    enabled: Required[Optional[bool]]
    """
    Specify whether to enable a custom certificate authority for signing Gateway
    traffic.
    """

    id: str
    """Specify the UUID of the certificate (ID from MTLS certificate store)."""
