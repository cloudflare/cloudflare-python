# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["UnrevokeCreateParams"]


class UnrevokeCreateParams(TypedDict, total=False):
    account_id: Required[object]

    body: Required[List[str]]
    """A list of device ids to unrevoke."""
