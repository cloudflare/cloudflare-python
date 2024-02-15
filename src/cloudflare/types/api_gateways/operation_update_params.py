# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OperationUpdateParams"]


class OperationUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    state: Literal["review", "ignored"]
    """Mark state of operation in API Discovery

    - `review` - Mark operation as for review
    - `ignored` - Mark operation as ignored
    """
