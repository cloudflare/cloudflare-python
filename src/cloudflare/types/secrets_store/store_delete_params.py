# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["StoreDeleteParams"]


class StoreDeleteParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    force: bool
    """
    When true, cascade-deletes all secrets in the store before deleting the store
    itself. Required when deleting a non-empty store. Without this parameter,
    attempting to delete a non-empty store returns 409.
    """
