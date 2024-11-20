# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MoveCreateParams"]


class MoveCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    destination: Required[
        Literal["Inbox", "JunkEmail", "DeletedItems", "RecoverableItemsDeletions", "RecoverableItemsPurges"]
    ]
