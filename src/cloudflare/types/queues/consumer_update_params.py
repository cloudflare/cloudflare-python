# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConsumerUpdateParams"]


class ConsumerUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    name: Required[str]

    body: Required[object]
