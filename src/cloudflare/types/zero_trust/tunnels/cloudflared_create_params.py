# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CloudflaredCreateParams"]


class CloudflaredCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    name: Required[str]
    """A user-friendly name for a tunnel."""

    config_src: Literal["local", "cloudflare"]
    """Indicates if this is a locally or remotely configured tunnel.

    If `local`, manage the tunnel using a YAML file on the origin machine. If
    `cloudflare`, manage the tunnel on the Zero Trust dashboard.
    """

    tunnel_secret: str
    """Sets the password required to run a locally-managed tunnel.

    Must be at least 32 bytes and encoded as a base64 string.
    """
