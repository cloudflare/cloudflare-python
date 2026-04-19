# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["NamespaceUpdateParams"]


class NamespaceUpdateParams(TypedDict, total=False):
    account_id: str

    description: Optional[str]
    """Optional description for the namespace. Max 256 characters."""
