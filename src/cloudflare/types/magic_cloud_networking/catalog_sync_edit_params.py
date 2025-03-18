# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CatalogSyncEditParams"]


class CatalogSyncEditParams(TypedDict, total=False):
    account_id: Required[str]

    description: str

    name: str

    policy: str

    update_mode: Literal["AUTO", "MANUAL"]
