# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ItemSyncParams"]


class ItemSyncParams(TypedDict, total=False):
    account_id: Required[str]

    namespace: Required[str]

    id: Required[str]
    """AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores."""

    next_action: Required[Literal["INDEX"]]

    wait_for_completion: bool
    """Wait for indexing before responding.

    After processing, vector-indexed instances use any time remaining in a 25s wait
    budget to confirm Vectorize ingestion. Processing itself continues uninterrupted
    and can exceed that budget. If confirmation times out, the response returns the
    current item state and background indexing continues. Defaults to false.
    """
