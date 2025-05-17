# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["BulkGetParams"]


class BulkGetParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    domain: List[str]
    """Accepts multiple values like `?domain=cloudflare.com&domain=example.com`."""
