# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BulkGetParams"]


class BulkGetParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    domain: object
    """Accepts multiple values, i.e. `?domain=cloudflare.com&domain=example.com`."""
