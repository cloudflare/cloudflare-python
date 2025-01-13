# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MoveBulkParams"]


class MoveBulkParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    destination: Required[
        Literal["Inbox", "JunkEmail", "DeletedItems", "RecoverableItemsDeletions", "RecoverableItemsPurges"]
    ]

    postfix_ids: Required[List[str]]
