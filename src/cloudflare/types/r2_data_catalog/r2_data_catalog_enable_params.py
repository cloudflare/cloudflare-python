# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["R2DataCatalogEnableParams", "Credential"]


class R2DataCatalogEnableParams(TypedDict, total=False):
    account_id: Required[str]
    """Use this to identify the account."""

    credential: Credential
    """Contains request to store catalog credentials."""


class Credential(TypedDict, total=False):
    """Contains request to store catalog credentials."""

    token: Required[str]
    """Provides the Cloudflare API token for accessing R2."""
