# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["SecretEditParams"]


class SecretEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    store_id: Required[str]
    """Store Identifier"""

    comment: str
    """Freeform text describing the secret"""

    scopes: SequenceNotStr[str]
    """The list of services that can use this secret."""
