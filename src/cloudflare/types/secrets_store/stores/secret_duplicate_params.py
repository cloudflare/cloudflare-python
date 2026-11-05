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

    comment: str
    """Freeform text describing the secret."""

    scopes: List[Literal["workers", "ai_gateway", "dex", "access", "containers", "websearch"]]
    """The list of services that can use this secret.

    Omit it on create or duplicate to inherit the store's scopes. An empty list lets
    no service use the secret.
    """
