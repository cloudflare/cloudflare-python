# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ...._types import SequenceNotStr

__all__ = ["BulkGetParams"]


class BulkGetParams(TypedDict, total=False):
    account_id: str
    """Identifier."""

    domain: SequenceNotStr[str]
    """Accepts multiple values like `?domain=cloudflare.com&domain=example.com`."""
