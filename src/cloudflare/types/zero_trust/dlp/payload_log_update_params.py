# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PayloadLogUpdateParams"]


class PayloadLogUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    public_key: Optional[str]
