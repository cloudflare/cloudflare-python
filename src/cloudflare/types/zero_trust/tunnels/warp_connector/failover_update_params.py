# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FailoverUpdateParams"]


class FailoverUpdateParams(TypedDict, total=False):
    account_id: str
    """Cloudflare account ID"""

    client_id: Required[str]
    """UUID of the Cloudflare Tunnel connector."""
