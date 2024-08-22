# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OriginTLSClientAuthCreateParams"]


class OriginTLSClientAuthCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    certificate: Required[str]
    """The zone's leaf certificate."""

    private_key: Required[str]
    """The zone's private key."""
