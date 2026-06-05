# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IdPFederationGrantCreateParams"]


class IdPFederationGrantCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    idp_id: Required[str]
    """UID of the identity provider to federate.

    Must be an existing identity provider in this account. One-time pin and
    Cloudflare-managed identity providers cannot be federated.
    """
