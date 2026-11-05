# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BasicAuthCredentialCreateParams"]


class BasicAuthCredentialCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID (32-character hexadecimal string)"""

    username: Required[str]
    """Login presented by the client. Printable ASCII only, excluding space and colon."""
