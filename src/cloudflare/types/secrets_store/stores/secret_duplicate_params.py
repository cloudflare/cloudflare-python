# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SecretDuplicateParams"]


class SecretDuplicateParams(TypedDict, total=False):
    account_id: Required[str]

    store_id: Required[str]

    name: Required[str]
    """The name of the secret."""

    scopes: Required[List[Literal["workers", "ai_gateway", "dex", "access", "containers", "websearch"]]]
    """The list of services that can use this secret."""

    comment: str
    """Freeform text describing the secret."""
