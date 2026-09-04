# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SecretCreateParams", "Body"]


class SecretCreateParams(TypedDict, total=False):
    account_id: Required[str]

    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    name: Required[str]
    """The name of the secret."""

    scopes: Required[List[Literal["workers", "ai_gateway", "dex", "access", "containers", "websearch"]]]
    """The list of services that can use this secret."""

    value: Required[str]
    """The value of the secret.

    Maximum 64 KiB (65,536 bytes). Note that this is 'write only' - the API never
    returns this value; it exists only to create or modify secrets.
    """

    comment: str
    """Freeform text describing the secret."""
