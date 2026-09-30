# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BasinCatalogDeleteParams"]


class BasinCatalogDeleteParams(TypedDict, total=False):
    account_id: Required[str]
    """Use this to identify the account."""

    force: bool
    """Remove child metadata before deleting the catalog."""
