# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CustomCertificateSettingsParam"]


class CustomCertificateSettingsParam(TypedDict, total=False):
    enabled: Required[bool]
    """Enable use of custom certificate authority for signing Gateway traffic."""

    id: str
    """UUID of certificate (ID from MTLS certificate store)."""
