# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SinkDeleteParams"]


class SinkDeleteParams(TypedDict, total=False):
    account_id: Required[str]
    """Specifies the public ID of the account."""

    force: str
    """Delete sink forcefully, including deleting any dependent pipelines."""
