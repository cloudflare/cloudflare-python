# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SSLParam"]


class SSLParam(TypedDict, total=False):
    id: Literal["ssl"]
    """
    Control options for the SSL feature of the Edge Certificates tab in the
    Cloudflare SSL/TLS app.
    """

    value: Literal["off", "flexible", "full", "strict", "origin_pull"]
    """The encryption mode that Cloudflare uses to connect to your origin server."""
