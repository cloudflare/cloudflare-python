# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConnectionDeleteParams"]


class ConnectionDeleteParams(TypedDict, total=False):
    account_id: str
    """Cloudflare account ID"""

    client_id: str
    """UUID of the Cloudflare Tunnel connector."""
