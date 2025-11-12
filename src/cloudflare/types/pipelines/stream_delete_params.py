# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["StreamDeleteParams"]


class StreamDeleteParams(TypedDict, total=False):
    account_id: Required[str]
    """Specifies the public ID of the account."""

    force: str
    """Delete stream forcefully, including deleting any dependent pipelines."""
