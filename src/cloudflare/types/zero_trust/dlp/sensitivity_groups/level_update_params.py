# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["LevelUpdateParams"]


class LevelUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    sensitivity_group_id: Required[str]

    description: Optional[str]

    name: Optional[str]
