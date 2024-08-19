# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["RevokeCreateParams"]


class RevokeCreateParams(TypedDict, total=False):
    account_id: Required[str]

    body: Required[List[str]]
    """A list of device ids to revoke."""
