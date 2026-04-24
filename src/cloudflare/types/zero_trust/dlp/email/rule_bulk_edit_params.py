# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["RuleBulkEditParams"]


class RuleBulkEditParams(TypedDict, total=False):
    account_id: Required[str]

    new_priorities: Required[Dict[str, int]]
