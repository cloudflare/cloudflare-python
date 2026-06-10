# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DataTagCreateParams"]


class DataTagCreateParams(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]

    description: Optional[str]
