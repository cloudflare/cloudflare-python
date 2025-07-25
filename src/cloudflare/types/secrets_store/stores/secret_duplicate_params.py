# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["SecretDuplicateParams"]


class SecretDuplicateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    store_id: Required[str]
    """Store Identifier"""

    name: Required[str]
    """The name of the secret"""

    scopes: Required[List[str]]
    """The list of services that can use this secret."""

    comment: str
    """Freeform text describing the secret"""
