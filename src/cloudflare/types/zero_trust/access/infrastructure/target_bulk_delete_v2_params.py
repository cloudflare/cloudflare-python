# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["TargetBulkDeleteV2Params"]


class TargetBulkDeleteV2Params(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier"""

    target_ids: Required[List[str]]
    """List of target IDs to bulk delete"""
