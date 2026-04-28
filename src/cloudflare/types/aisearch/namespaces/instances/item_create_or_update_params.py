# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ItemCreateOrUpdateParams"]


class ItemCreateOrUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]

    key: Required[str]
    """Item key / filename. Must not exceed 128 characters."""

    next_action: Required[Literal["INDEX"]]

    wait_for_completion: bool
    """Wait for indexing to fully complete before responding.

    On RAGs with vector indexing enabled, this additionally waits for Vectorize
    ingestion confirmation (up to 40s) so the returned item reflects a queryable
    state. On timeout the item is returned in `running` state and the background
    alarm continues polling. Defaults to false.
    """
