# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CredentialCreateParams"]


class CredentialCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Use this to identify the account."""

    token: Required[str]
    """Provides the Cloudflare API token for accessing R2."""
