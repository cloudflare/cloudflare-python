# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["EventTagCreateParams"]


class EventTagCreateParams(TypedDict, total=False):
    account_id: Required[float]
    """Account ID"""

    tags: Required[List[str]]
