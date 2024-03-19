# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TunnelCreateParams"]


class TunnelCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    name: Required[str]
    """A user-friendly name for the tunnel."""

    tunnel_secret: Required[object]
    """Sets the password required to run the tunnel.

    Must be at least 32 bytes and encoded as a base64 string.
    """
