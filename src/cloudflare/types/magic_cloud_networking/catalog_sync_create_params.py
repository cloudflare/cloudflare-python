# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CatalogSyncCreateParams"]


class CatalogSyncCreateParams(TypedDict, total=False):
    account_id: Required[str]

    destination_type: Required[Literal["NONE", "ZERO_TRUST_LIST"]]

    name: Required[str]

    update_mode: Required[Literal["AUTO", "MANUAL"]]

    description: str

    policy: str

    forwarded: str
