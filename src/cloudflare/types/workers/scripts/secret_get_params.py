# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SecretGetParams"]


class SecretGetParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    script_name: Required[str]
    """Name of the script, used in URLs and route configuration."""

    url_encoded: bool
    """Flag that indicates whether the secret name is URL encoded."""
