# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OperationEditParams"]


class OperationEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    state: Literal["review", "ignored"]
    """Mark state of operation in API Discovery

    - `review` - Mark operation as for review
    - `ignored` - Mark operation as ignored
    """
